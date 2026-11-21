// CDP 验证 gio 各页 Example 渲染(h2 标题 + 代码块 + 语法高亮)
const http = require('http');
const WebSocket = require('D:/github/gma/node_modules/ws');
const fs = require('fs');

const PORT = 9360;
const BASE = 'http://localhost:8080';
const PAGES = ['open_file', 'open_vector', 'open_raster', 'read_dataframe',
  'GeoDatabase', 'Layer', 'Feature', 'Geometry',
  'VirtualVectorGeoDatabase', 'VirtualRasterDataset', 'FieldType', 'FieldTypes', 'Dataset'];

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

  const results = [];
  for (const p of PAGES) {
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/gio/${p}.html` });
    await sleep(1600);
    const r = await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
      const md = document.querySelector('.theme-reco-md-content');
      if (!md) return { err: 'no md content' };
      const h2s = [...md.querySelectorAll('h2')].map(h => h.textContent.trim());
      const blocks = [...md.querySelectorAll('div[class*=language-python], div[class*=language-py], .language-python, pre[class*=language]')];
      const allPres = [...md.querySelectorAll('pre')];
      const exIdx = h2s.indexOf('Example');
      // Example 之后的代码块
      let exBlocks = [];
      if (exIdx >= 0) {
        const h2 = [...md.querySelectorAll('h2')][exIdx];
        let el = h2.nextElementSibling;
        while (el) {
          const pre = el.querySelector('pre');
          if (pre && el.className.includes('language')) exBlocks.push(el.className);
          el = el.nextElementSibling;
        }
      }
      // 签名卡检查(页面完整性)
      const sig = !!md.querySelector('span[style*="background-color"]');
      return {
        h2s: h2s.join('|'),
        hasExample: exIdx >= 0,
        pyBlockCount: allPres.length,
        exBlockClasses: exBlocks.join(' / '),
        sig
      };
    })()` });
    results.push({ page: p, value: r.result && r.result.result && r.result.result.value });
  }

  console.log(JSON.stringify(results.map(r => ({ page: r.page, v: r.value })), null, 1));
  // 断言
  let bad = 0;
  for (const r of results) {
    const v = r.value || {};
    if (v.err || !v.hasExample || v.exBlockClasses === '') {
      console.log(`[FAIL] ${r.page}: err=${v.err || '-'} hasExample=${v.hasExample} blocks=${v.exBlockClasses}`);
      bad++;
    } else {
      console.log(`[OK] ${r.page}: Example h2 + python 块 ✓ 签名卡 ${v.sig}`);
    }
  }
  console.log(bad === 0 ? 'ALL RENDER OK' : `${bad} FAILED`);
  ws.close();
  process.exit(bad === 0 ? 0 : 1);
})();
