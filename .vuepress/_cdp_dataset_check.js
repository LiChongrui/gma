// CDP 验证 Dataset.md 方法级 Example 渲染
const http = require('http');
const WebSocket = require('D:/github/gma/node_modules/ws');

const PORT = 9361;
const BASE = 'http://localhost:8080';

const sleep = ms => new Promise(r => setTimeout(r, ms));
function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, r => { let d = ''; r.on('data', c => d += c); r.on('end', () => resolve(JSON.parse(d))); }).on('error', reject);
  });
}

(async () => {
  const tabs = await getJson(`http://127.0.0.1:${PORT}/json`);
  const page = tabs.find(t => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl, { maxPayload: 50 * 1024 * 1024 });
  let id = 0; const pend = {};
  ws.on('message', m => { const d = JSON.parse(m); if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; } });
  const send = (method, params = {}) => new Promise(res => { const i = ++id; pend[i] = res; ws.send(JSON.stringify({ id: i, method, params })); });
  await sleep(500);

  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/gio/Dataset.html` });
  await sleep(2500);

  const r = await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
    const md = document.querySelector('.theme-reco-md-content');
    if (!md) return { err: 'no md content' };
    const h3s = [...md.querySelectorAll('h3')].map(h => h.textContent.trim().split('(')[0].trim());
    // 方法级 Example 标签数
    const exLabels = [...md.querySelectorAll('p')].filter(p => p.textContent.trim() === 'Example:' && p.style.color).length;
    const rsLabels = [...md.querySelectorAll('p')].filter(p => p.textContent.trim() === 'Result:' && p.style.color).length;
    // text 结果块
    const textBlocks = [...md.querySelectorAll('div[class*=language-text]')].length;
    // 每个方法段(h3)后是否紧跟 Example 标签(在下一个 h3 前)
    const h3Els = [...md.querySelectorAll('h3')];
    const methodsWithEx = h3Els.filter(h3 => {
      let el = h3.nextElementSibling;
      while (el && el.tagName !== 'H3') {
        if (el.tagName === 'P' && el.textContent.trim() === 'Example:') return true;
        el = el.nextElementSibling;
      }
      return false;
    }).length;
    return {
      h3Count: h3s.length,
      exLabels, rsLabels, textBlocks,
      methodsWithEx,
      first3: h3s.slice(0, 3),
      hasClassExample: [...md.querySelectorAll('h2')].some(h => h.textContent.trim() === 'Example')
    };
  })()` });

  const v = r.result.result.value;
  console.log(JSON.stringify(v, null, 1));
  const checks = [
    ['h3 总数 39(24 方法 + 15 Property)', v.h3Count === 39],
    ['24 个 Example 标签', v.exLabels === 24],
    ['24 个 Result 标签', v.rsLabels === 24],
    ['24 个 text 结果块', v.textBlocks >= 24],
    ['24 个方法段全部含 Example', v.methodsWithEx === 24],
    ['类级 ## Example 存在', v.hasClassExample],
  ];
  let bad = 0;
  checks.forEach(([name, pass]) => { console.log((pass ? '[OK]' : '[FAIL]') + ' ' + name); if (!pass) bad++; });
  console.log(bad === 0 ? 'ALL RENDER OK' : bad + ' FAILED');
  ws.close();
  process.exit(bad === 0 ? 0 : 1);
})();
