/* 查继承卡按钮的计算样式与命中规则 */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9355;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfL';
const URL = 'http://localhost:8080/docs/UserGuide/gio/VirtualVectorGeoDatabase.html';

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
    '--window-size=1600,900', 'about:blank'
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
      const btn = document.querySelector('.inherit-card__btn');
      if (!btn) return { err: 'no btn' };
      const cs = getComputedStyle(btn);
      return {
        color: cs.color,
        bg: cs.backgroundColor,
        text: btn.textContent.trim(),
        font: cs.fontSize
      };
    })()`);
    console.log(JSON.stringify(res, null, 1));
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* gone */ }
  }
})();
