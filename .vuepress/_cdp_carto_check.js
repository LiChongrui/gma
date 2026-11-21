/* 验证 carto 重组:inres 页(5小节4表)、MapFrame 页(plot 全名+4方法)、侧栏 2 条目、旧页 404 */
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const PORT = 9359;
const BASE = 'http://localhost:8080';

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

  const PAGE_JS = `(() => {
    const md = document.querySelector('.theme-reco-md-content');
    if (!md) return { err: 'no md-content' };
    const h3s = [...md.querySelectorAll('h3')].map(h => h.textContent.trim().replace(/#$/, '').split('(')[0].trim());
    return {
      pathline: (md.querySelector('p[style*="font-size:120%"][style*="font-weight:bold"]') || {}).textContent || null,
      constSigs: [...md.querySelectorAll('span')].filter(s => s.textContent.trim() === '[const]').length,
      classSigs: [...md.querySelectorAll('span')].filter(s => s.textContent.trim() === '[class]').length,
      h3s,
      tables: md.querySelectorAll('table').length,
      tableRows: [...md.querySelectorAll('table')].map(t => t.querySelectorAll('tbody tr').length)
    };
  })()`;

  // ---- inres 页 ----
  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/carto/inres.html` });
  await sleep(7000);
  const inres = await evalJs(PAGE_JS);

  // ---- MapFrame 页 ----
  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/carto/MapFrame.html` });
  await sleep(7000);
  const mapframe = await evalJs(PAGE_JS);

  // ---- 侧栏(carto 组) ----
  const sidebar = await evalJs(`(() => {
    const container = document.querySelector('.series-container');
    if (!container) return { err: 'no series-container' };
    const cartoLi = [...container.querySelectorAll(':scope > section.series-group')].find(g =>
      g.querySelector(':scope > h5.series-heading')?.textContent.includes('carto'));
    if (!cartoLi) return { err: 'no carto group' };
    const links = [...cartoLi.querySelectorAll(':scope ul a.series-item')].map(a => a.textContent.trim());
    return { links, routerActive: [...cartoLi.querySelectorAll('a.series-item.router-link-active')].map(a => a.textContent.trim()) };
  })()`);

  // ---- README 表 ----
  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/carto/` });
  await sleep(7000);
  const readme = await evalJs(`(() => {
    const md = document.querySelector('.theme-reco-md-content');
    if (!md) return { err: 'no md-content' };
    const t = md.querySelector('table');
    return t ? { rows: t.querySelectorAll('tbody tr').length, texts: [...t.querySelectorAll('tbody tr')].map(tr => tr.textContent.trim().slice(0, 60)) } : { err: 'no table' };
  })()`);

  // ---- 旧页 404 ----
  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/carto/GeometryStyles.html` });
  await sleep(6000);
  const oldPage = await evalJs(`(() => ({
    is404: /404|not found/i.test((document.querySelector('h1') || {}).textContent || '')
  }))()`);

  // ---- inres 页截图 ----
  await send('Page.navigate', { url: `${BASE}/docs/UserGuide/carto/inres.html` });
  await sleep(6000);
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('D:/github/gma/.vuepress/_shots/carto_check.png', Buffer.from(shot.result.data, 'base64'));

  const ok = (c, label) => `${c ? 'PASS' : 'FAIL'} ${label}`;
  const checks = [
    ok(inres.pathline === 'gma.carto.inres', `inres 路径行(${inres.pathline})`),
    ok(inres.constSigs === 3, `inres 页 [const] × 3(头部+Composs+ScaleBar)(实测 ${inres.constSigs})`),
    ok(inres.classSigs === 3, `inres 页 [class] × 3(MarkerPath/WorldLayer/WorldDataset)(实测 ${inres.classSigs})`),
    ok(inres.h3s?.join(',') === 'Composs,ScaleBar,MarkerPath,WorldLayer,WorldDataset', `inres 小节(${(inres.h3s || []).join(',')})`),
    ok(inres.tables === 4 && inres.tableRows?.join('/') === '3/1/5/2', `4 张成员表(3/1/5/2)(实测 ${inres.tables} 张: ${(inres.tableRows || []).join('/')})`),
    ok(mapframe.pathline === 'gma.carto.plot.MapFrame', `MapFrame 路径行(${mapframe.pathline})`),
    ok(mapframe.h3s?.length === 4 && mapframe.h3s?.[0] === 'add_appearance' && mapframe.h3s?.[3] === 'add_raster', `MapFrame 4 方法(${(mapframe.h3s || []).join(',')})`),
    ok(sidebar.links?.join(',') === 'MapFrame,inres', `侧栏 carto 组 2 条目(${(sidebar.links || []).join(',')})`),
    ok((sidebar.routerActive || []).includes('MapFrame'), `当前条目高亮(${JSON.stringify(sidebar.routerActive)})`),
    ok(readme.rows === 2, `README 表 2 行(实测 ${readme.rows})`),
    ok(oldPage.is404, `旧页(GeometryStyles)显示 404`),
  ];
  console.log(JSON.stringify({ inres, mapframe, sidebar, readme, oldPage }, null, 1));
  console.log('\n===== 断言 =====\n' + checks.join('\n'));
  ws.close();
})();
