// 截取当前 Dataset 页方法示例区域的渲染效果（只读分析用）
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');
const WebSocket = require('D:/github/gma/node_modules/ws');

const PORT = 9365;
const BASE = 'http://localhost:8080';
const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PROFILE = 'D:/github/gma/.vuepress/_edge_design';
const OUT = 'D:/github/gma/.vuepress/_shots';

const sleep = ms => new Promise(r => setTimeout(r, ms));
function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, r => { let d = ''; r.on('data', c => d += c); r.on('end', () => resolve(JSON.parse(d))); }).on('error', reject);
  });
}
async function waitEdge() {
  for (let i = 0; i < 30; i++) {
    try { await getJson(`http://127.0.0.1:${PORT}/json/version`); return true; } catch (e) { await sleep(500); }
  }
  return false;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const edge = spawn(EDGE, [
    '--headless=new', `--remote-debugging-port=${PORT}`,
    `--user-data-dir=${PROFILE}`, '--no-first-run', '--window-size=1400,2400',
    'about:blank'
  ], { stdio: 'ignore' });
  if (!await waitEdge()) { console.log('EDGE FAIL'); edge.kill(); process.exit(1); }

  const tabs = await getJson(`http://127.0.0.1:${PORT}/json`);
  const page = tabs.find(t => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl, { maxPayload: 50 * 1024 * 1024 });
  let id = 0; const pend = {};
  ws.on('message', m => { const d = JSON.parse(m); if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; } });
  const send = (method, params = {}) => new Promise(res => { const i = ++id; pend[i] = res; ws.send(JSON.stringify({ id: i, method, params })); });
  await sleep(500);

  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/gio/Dataset.html` });
  await sleep(3500);

  // 找到 algebraic 方法段的 Example 区域并滚动截图
  const loc = await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
    const md = document.querySelector('.theme-reco-md-content');
    const h3 = [...md.querySelectorAll('h3')].find(h => h.textContent.includes('algebraic'));
    h3.scrollIntoView();
    const rect = h3.getBoundingClientRect();
    return { y: rect.top, id: h3.id };
  })()` });
  console.log('LOC:', JSON.stringify(loc.result.result.value));
  await sleep(600);
  await send('Page.captureScreenshot', { format: 'png' }).then(d => {
    fs.writeFileSync(path.join(OUT, 'design_current_algebraic.png'), Buffer.from(d.result.data, 'base64'));
  });

  // set_metadata 段（有 {...} 占位符的 Result）
  await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
    const h3 = [...document.querySelectorAll('.theme-reco-md-content h3')].find(h => h.textContent.includes('set_metadata'));
    h3.scrollIntoView(); return true;
  })()` });
  await sleep(600);
  await send('Page.captureScreenshot', { format: 'png' }).then(d => {
    fs.writeFileSync(path.join(OUT, 'design_current_setmeta.png'), Buffer.from(d.result.data, 'base64'));
  });

  // 类级 Example（页尾）
  await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
    const h2 = [...document.querySelectorAll('.theme-reco-md-content h2')].find(h => h.textContent.trim() === 'Example');
    h2.scrollIntoView(); return true;
  })()` });
  await sleep(600);
  await send('Page.captureScreenshot', { format: 'png' }).then(d => {
    fs.writeFileSync(path.join(OUT, 'design_current_classex.png'), Buffer.from(d.result.data, 'base64'));
  });

  console.log('DONE');
  ws.close(); edge.kill();
  process.exit(0);
})();
