/* 验证 crs 侧栏折叠交互:默认折叠(1行) → 点箭头展开(34项) → 箭头/组标题位置不变 → 收起恢复 → 总览页自动展开 */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9354;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfCollapse';
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

// 提取嵌套组状态:箭头方向、列表可见性、子项数、组标题/容器几何(container 内坐标)
const STATE_JS = `(() => {
  const container = document.querySelector('.series-container');
  if (!container) return { err: 'no series-container' };
  const nested = [...container.querySelectorAll('li > section.series-group')].find(g => {
    const h = g.querySelector(':scope > h6.series-heading');
    return h && h.textContent.includes('ProjMethods');
  });
  if (!nested) return { err: 'no nested ProjMethods group' };
  const head = nested.querySelector(':scope > h6.series-heading');
  const arrow = head.querySelector('.arrow');
  const ul = nested.querySelector(':scope > ul');
  const links = ul ? [...ul.querySelectorAll(':scope a.series-item')] : [];
  const cr = container.getBoundingClientRect();
  const hr = head.getBoundingClientRect();
  return {
    arrowCls: arrow ? arrow.className : null,
    arrowVisible: arrow ? arrow.offsetWidth > 0 && arrow.offsetHeight > 0 : false,
    listDisplay: ul ? getComputedStyle(ul).display : null,
    visibleItems: links.filter(a => a.offsetWidth > 0).length,
    headActive: head.classList.contains('active'),
    headTopInContainer: hr.top - cr.top + container.scrollTop,
    containerWidth: Math.round(cr.width),
    containerScrollHeight: container.scrollHeight,
    containerClientHeight: container.clientHeight,
    url: location.pathname
  };
})()`;

(async () => {
  const proc = spawn(EDGE, [
    '--headless', '--disable-gpu',
    '--blink-settings=preferredColorScheme=1',
    `--remote-debugging-port=${PORT}`,
    `--user-data-dir=${PROFILE}`,
    '--window-size=1600,1400', 'about:blank'
  ], { stdio: 'ignore' });
  const out = [];
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

    // ---- 场景 1:AngleUnits 页(非方法页)默认折叠态 ----
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/crs/AngleUnits.html` });
    await sleep(7000);
    const collapsed = await evalJs(STATE_JS);
    out.push({ step: '1 默认折叠态(AngleUnits页)', collapsed });

    // 记录箭头点击坐标(视口坐标)
    const arrowPt = await evalJs(`(() => {
      const container = document.querySelector('.series-container');
      const nested = [...container.querySelectorAll('li > section.series-group')].find(g =>
        g.querySelector(':scope > h6.series-heading')?.textContent.includes('ProjMethods'));
      const a = nested.querySelector(':scope > h6.series-heading .arrow');
      const r = a.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    })()`);

    // ---- 场景 2:点击箭头展开 ----
    await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: arrowPt.x, y: arrowPt.y, button: 'left', clickCount: 1 });
    await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: arrowPt.x, y: arrowPt.y, button: 'left', clickCount: 1 });
    await sleep(600);
    const expanded = await evalJs(STATE_JS);
    out.push({ step: '2 点击箭头展开', expanded });

    // ---- 场景 3:再点一次收起 ----
    await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: arrowPt.x, y: arrowPt.y, button: 'left', clickCount: 1 });
    await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: arrowPt.x, y: arrowPt.y, button: 'left', clickCount: 1 });
    await sleep(600);
    const recollapsed = await evalJs(STATE_JS);
    out.push({ step: '3 再点收起', recollapsed });

    // 折叠态截图(AngleUnits 页)
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('D:/github/gma/.vuepress/_shots/collapse_check.png', Buffer.from(shot.result.data, 'base64'));

    // ---- 场景 4:ProjMethods 总览页自动展开 ----
    await send('Page.navigate', { url: `${BASE}/docs/UserGuide/crs/ProjMethods.html` });
    await sleep(7000);
    const auto = await evalJs(STATE_JS);
    out.push({ step: '4 总览页自动展开', auto });

    // ---- 断言汇总 ----
    const ok = (c, label) => `${c ? 'PASS' : 'FAIL'} ${label}`;
    const checks = [
      ok(collapsed.arrowCls?.includes('right') && !collapsed.arrowCls?.includes('down'), '折叠态箭头朝右'),
      ok(collapsed.listDisplay === 'none' && collapsed.visibleItems === 0, '折叠态34项不可见'),
      ok(collapsed.arrowVisible, '折叠态箭头可见'),
      ok(expanded.arrowCls?.includes('down'), '展开态箭头朝下'),
      ok(expanded.listDisplay === 'block' && expanded.visibleItems === 34, `展开态34项可见(实测${expanded.visibleItems})`),
      ok(Math.abs(expanded.headTopInContainer - collapsed.headTopInContainer) < 1, `展开前后组标题位置不变(${collapsed.headTopInContainer?.toFixed(1)} → ${expanded.headTopInContainer?.toFixed(1)})`),
      ok(expanded.containerWidth === collapsed.containerWidth, `展开前后侧栏内容宽度不变(gutter stable, ${collapsed.containerWidth}px)`),
      ok(recollapsed.listDisplay === 'none', '再点收起恢复'),
      ok(auto.headActive && auto.listDisplay === 'block' && auto.visibleItems === 34, '总览页激活自动展开+组标题高亮'),
      ok(collapsed.containerScrollHeight <= collapsed.containerClientHeight, '折叠态无滚动条'),
    ];
    console.log(JSON.stringify(out, null, 1));
    console.log('\n===== 断言 =====\n' + checks.join('\n'));
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* gone */ }
  }
})();
