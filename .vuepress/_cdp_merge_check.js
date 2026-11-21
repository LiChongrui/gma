/* 验证 ProjMethods 单页整合:总览页结构(签名卡/参数表/索引表/34小节)、侧栏 10 条目、旧方法页 404 */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9358; /* 复用后台任务启动的无头实例 */
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfMerge';
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
function getStatus(url) {
  return new Promise((resolve, reject) => {
    http.get(url, r => { r.resume(); resolve({ status: r.statusCode }); }).on('error', reject);
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
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

    // ---- 总览页结构 ----
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/crs/ProjMethods.html` });
    await sleep(8000);
    const page = await evalJs(`(() => {
      const md = document.querySelector('.theme-reco-md-content');
      if (!md) return { err: 'no md-content' };
      const h2s = [...md.querySelectorAll('h2')].map(h => h.textContent.trim().replace(/#$/, ''));
      const h3s = [...md.querySelectorAll('h3')].map(h => h.textContent.trim().replace(/#$/, ''));
      const tables = [...md.querySelectorAll('table')].map(t => ({ rows: t.querySelectorAll('tbody tr').length }));
      const t0 = md.querySelector('table');
      const headCells = t0 ? [...t0.querySelectorAll('thead th')].map(th => th.textContent.trim()) : [];
      const tableCols = headCells.length;
      const rangeCells = t0 ? [...t0.querySelectorAll('tbody tr')].map(tr => tr.querySelector('td:nth-child(2)')?.textContent.trim()) : [];
      const pathline = !!md.querySelector('p[style*="font-size:120%"][style*="font-weight:bold"]');
      const constSig = md.textContent.includes('[const]');
      const classSigs = [...md.querySelectorAll('span')].filter(s => s.textContent.trim() === '[class]').length;
      const anchorLinks = [...md.querySelectorAll('table a')].filter(a => (a.getAttribute('href') || '').startsWith('#')).length;
      const catalog = [...document.querySelectorAll('.page-catalog-container a')].map(a => a.textContent.trim());
      return {
        h2s, h3Count: h3s.length, h3First: h3s[0], h3Last: h3s[h3s.length - 1],
        tableRows: tables, pathline, constSig, classSigs, anchorLinks,
        tableCols, headCells, rangeCells,
        catalogCount: catalog.length, catalogFirst: catalog[0], catalogLast: catalog[catalog.length - 1]
      };
    })()`);

    // ---- 侧栏结构(crs 组) ----
    const sidebar = await evalJs(`(() => {
      const container = document.querySelector('.series-container');
      if (!container) return { err: 'no series-container' };
      const items = [...container.querySelectorAll('a.series-item')].map(a => a.textContent.trim()).filter(t => t !== 'Contents');
      const h5heads = [...container.querySelectorAll('h5.series-heading')].map(h => h.textContent.trim());
      const h6heads = [...container.querySelectorAll('h6.series-heading')].map(h => h.textContent.trim());
      const arrows = container.querySelectorAll('.arrow').length;
      const actives = [...container.querySelectorAll('a.series-item.active, h6.series-heading.active')].map(a => a.textContent.trim());
      const routerActive = [...container.querySelectorAll('a.series-item.router-link-active')].map(a => a.textContent.trim());
      const pmClasses = [...container.querySelectorAll('a.series-item')].find(a => a.textContent.trim() === 'ProjMethods')?.className;
      return { h5heads, h6Count: h6heads.length, arrows, items, actives, routerActive, pmClasses };
    })()`);

    // ---- 旧方法页 URL:客户端是否渲染 404(dev 模式 SPA fallback 恒 200,须看页面内容) ----
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/crs/ProjMethods/Mercator.html` });
    await sleep(6000);
    const oldPageCheck = await evalJs(`(() => ({
      title: document.title,
      h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : null,
      is404: /404|not found/i.test(document.title + ' ' + document.body.textContent.slice(0, 3000))
    }))()`);

    // ---- 回到总览页截图 ----
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/crs/ProjMethods.html` });
    await sleep(6000);
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('D:/github/gma/.vuepress/_shots/merge_check.png', Buffer.from(shot.result.data, 'base64'));

    const ok = (c, label) => `${c ? 'PASS' : 'FAIL'} ${label}`;
    const checks = [
      ok(page.pathline && page.constSig, '路径行 + [const] 签名卡'),
      ok(page.h2s?.join(',') === 'Parameters', `h2 仅剩 Parameters(${(page.h2s || []).join(', ')})`),
      ok(page.tableRows?.length === 1 && page.tableRows?.[0]?.rows === 9, `仅 1 张表 9 行(索引表已删)(实测 ${(page.tableRows || []).map(t => t.rows).join('/')})`),
      ok(page.tableCols === 3 && page.headCells?.join(',') === 'Parameter,Range,Description', `Parameters 表 3 列含 Range(${(page.headCells || []).join(',')})`),
      ok(page.rangeCells?.includes('[-180°, 180°]') && page.rangeCells?.includes('[-90°, 90°]') && page.rangeCells?.filter(r => r === '—').length === 3, `Range 值正确(${(page.rangeCells || []).join(' ')})`),
      ok(page.h3Count === 34, `方法小节 h3 × 34(实测 ${page.h3Count})`),
      ok(page.classSigs === 34, `方法签名卡 [class] × 34(实测 ${page.classSigs})`),
      ok(page.h3First === 'Aitoff' && page.h3Last === 'WinkelTripel', `小节字母序(${page.h3First} → ${page.h3Last})`),
      ok(sidebar.h5heads?.join(',') === 'Start,crs', `侧栏一级组(${(sidebar.h5heads || []).join(',')})`),
      ok(sidebar.h6Count === 0 && sidebar.arrows === 2, `无嵌套组、箭头仅 2 个(一级组)(h6=${sidebar.h6Count}, arrows=${sidebar.arrows})`),
      ok(sidebar.items?.length === 10, `crs 组 10 条目(实测 ${sidebar.items?.length})`),
      ok(sidebar.items?.length > 0 && sidebar.items[sidebar.items.length - 1] === 'ProjMethods', `ProjMethods 为 crs 组最后一项(末项=${sidebar.items ? sidebar.items[sidebar.items.length - 1] : '?'})`),
      ok((sidebar.actives || []).includes('ProjMethods') || (sidebar.routerActive || []).includes('ProjMethods'), `当前条目高亮(active=${JSON.stringify(sidebar.actives)}, routerActive=${JSON.stringify(sidebar.routerActive)})`),
      ok(oldPageCheck.is404, `旧方法页显示 404(${oldPageCheck.title})`),
    ];
    console.log(JSON.stringify({ page, sidebar, oldPageCheck }, null, 1));
    console.log('\n===== 断言 =====\n' + checks.join('\n'));
    ws.close();
  } finally {
    /* 复用外部实例,不杀进程 */
  }
})();
