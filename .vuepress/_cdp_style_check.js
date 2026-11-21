/* 确认路径标题行样式生效 + h3 底条/竖条状态（非 hover 态） */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9347;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfH';
const URL = 'http://localhost:8080/docs/UserGuide/driver/DriveStatistics.html';

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
    if (!wsUrl) throw new Error('no devtools');
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
    await sleep(6000);
    const res = await evalJs(`(() => {
      const md = document.querySelector('.theme-reco-md-content');
      const ps = [...md.querySelectorAll('p')];
      const path = ps.find(p => /^gma\\./.test(p.textContent.trim()));
      const pcs = path ? getComputedStyle(path) : null;
      const grp = ps.find(p => (p.getAttribute('style') || '').startsWith('margin-left:2em'));
      const gcs = grp ? getComputedStyle(grp) : null;
      const big = md.querySelector('span[style*="background-color:#EFF0FC"] > span[style*="font-size:150%"]');
      const bcs = big ? getComputedStyle(big) : null;
      const h3 = document.querySelector('.theme-reco-md-content h3');
      const csB = getComputedStyle(h3, '::before');
      const item = document.querySelector('.series-container a.series-item');
      const ics = item ? getComputedStyle(item) : null;
      return {
        path_font: pcs ? pcs.fontFamily.split(',')[0] : null,
        path_size: pcs ? pcs.fontSize : null,
        path_color: pcs ? pcs.color : null,
        grp_margin_top: gcs ? gcs.marginTop : null,
        grp_margin_bottom: gcs ? gcs.marginBottom : null,
        sig_inner_size: bcs ? bcs.fontSize : null,
        h3_bar_opacity: csB.opacity,
        h3_bar_height: csB.height,
        side_padding: ics ? ics.paddingTop + ' / ' + ics.paddingBottom : null,
        side_lineheight: ics ? ics.lineHeight : null,
        side_item_h: item ? item.offsetHeight : null
      };
    })()`);
    console.log(JSON.stringify(res, null, 1));
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    require('fs').writeFileSync('D:/github/gma/.vuepress/_shots/style_check.png', Buffer.from(shot.result.data, 'base64'));
    console.log('screenshot saved');
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* gone */ }
  }
})();
