/* CDP 真实 hover 验证（Node 版，复用项目内 ws 包）
   1) 悬停 h3 成员标题 -> # 淡入（a::before opacity=1）+ 竖条淡出（h3::before opacity=0）
   2) 竖条几何居中：h3 盒中心 vs 标题文字首行中心差值
   3) hover 态局部截图 */
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const WebSocket = require('ws');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9346;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfHover';
const URL = 'http://localhost:8080/docs/UserGuide/crs/Ellipsoid.html';
const SHOT = 'D:/github/gma/.vuepress/_shots/hover_state.png';

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, r => {
      let d = '';
      r.on('data', c => (d += c));
      r.on('end', () => { try { resolve(JSON.parse(d)); } catch (e) { reject(e); } });
    }).on('error', reject);
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const proc = spawn(EDGE, [
    '--headless', '--disable-gpu',
    '--blink-settings=preferredColorScheme=1',
    `--remote-debugging-port=${PORT}`,
    `--user-data-dir=${PROFILE}`,
    '--window-size=1600,1400', 'about:blank'
  ], { stdio: 'ignore' });

  try {
    let wsUrl = null;
    for (let i = 0; i < 30; i++) {
      await sleep(500);
      try {
        const tabs = await getJson(`http://127.0.0.1:${PORT}/json`);
        const page = tabs.find(t => t.type === 'page');
        if (page) { wsUrl = page.webSocketDebuggerUrl; break; }
      } catch (e) { /* retry */ }
    }
    if (!wsUrl) throw new Error('devtools endpoint not reachable');

    const ws = new WebSocket(wsUrl);
    await new Promise((res, rej) => { ws.on('open', res); ws.on('error', rej); });

    let mid = 0;
    const pending = new Map();
    ws.on('message', m => {
      const msg = JSON.parse(m);
      if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg); pending.delete(msg.id); }
    });
    const send = (method, params = {}) => new Promise(res => {
      mid += 1; pending.set(mid, res);
      ws.send(JSON.stringify({ id: mid, method, params }));
    });
    const evalJs = async expr => {
      const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r.result.result.value;
    };

    await send('Page.enable');
    await send('Page.navigate', { url: URL });
    await sleep(7000);

    const pos = await evalJs(`(() => {
      const h = document.querySelector('.theme-reco-md-content h3');
      if (!h) return {err: 'no h3'};
      h.scrollIntoView({block: 'center', behavior: 'instant'});
      const r = h.getBoundingClientRect();
      return {x: r.x + r.width / 2, y: r.y + r.height / 2};
    })()`);
    if (!pos || pos.err) { console.log('FAIL', pos); process.exit(1); }

    await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: pos.x, y: pos.y });
    await sleep(800);

    const res = await evalJs(`(() => {
      const h = document.querySelector('.theme-reco-md-content h3');
      const a = h.querySelector('a.header-anchor');
      const csB = getComputedStyle(h, '::before');
      const csH = getComputedStyle(a, '::before');
      const span = a.querySelector('span') || a;
      const tr = span.getClientRects()[0];
      const hr = h.getBoundingClientRect();
      return {
        bar_opacity: csB.opacity,
        hash_opacity: csH.opacity,
        hash_content: csH.content,
        hash_color: csH.color,
        bar_center_y: hr.top + hr.height / 2,
        text_center_y: tr.top + tr.height / 2
      };
    })()`);
    console.log(JSON.stringify(res, null, 1));

    const okHash = res.hash_opacity === '1' && (res.hash_content || '').includes('#');
    const okBar = res.bar_opacity === '0';
    const diff = Math.abs(res.bar_center_y - res.text_center_y);
    console.log('ASSERT hash shown (opacity=1):', okHash);
    console.log('ASSERT bar faded (opacity=0):', okBar);
    console.log('ASSERT bar/text vertical center diff: ' + diff.toFixed(2) + ' px (expect < 2)');

    const shot = await send('Page.captureScreenshot', {
      format: 'png',
      clip: { x: Math.max(0, pos.x - 480), y: pos.y - 42, width: 960, height: 92, scale: 2 }
    });
    fs.writeFileSync(SHOT, Buffer.from(shot.result.data, 'base64'));
    console.log('shot saved ->', SHOT);
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* already gone */ }
  }
})();
