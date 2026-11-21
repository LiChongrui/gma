/* 验证 crs 侧栏:ProjMethods 嵌套组位于字母序位置、无箭头、34 项常驻展开 */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9353;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfSidebar';
const URL = 'http://localhost:8080/docs/UserGuide/crs/ProjMethods.html';

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
    await sleep(7000);
    const res = await evalJs(`(() => {
      const container = document.querySelector('.series-container');
      if (!container) return { err: 'no series-container' };
      const heads = [...container.querySelectorAll('h5.series-heading, h6.series-heading')].map(h => ({
        tag: h.tagName, text: h.textContent.trim(),
        hasArrow: !!h.querySelector('.arrow'),
        hasLink: !!h.querySelector('a.link'),
        active: h.classList.contains('active')
      }));
      const groups = [...container.querySelectorAll(':scope > section.series-group')].map(g => {
        const head = g.querySelector(':scope > .series-heading');
        const ul = g.querySelector(':scope > ul');
        const kids = ul ? [...ul.children].map(li => {
          const sub = li.querySelector(':scope > section.series-group');
          if (sub) {
            const sh = sub.querySelector(':scope > .series-heading');
            const su = sub.querySelector(':scope > ul');
            const links = su ? [...su.querySelectorAll('a.series-item')] : [];
            return {
              kind: 'nested-group',
              text: sh ? sh.textContent.trim() : null,
              headHasArrow: sh ? !!sh.querySelector('.arrow') : null,
              headHasLink: sh ? !!sh.querySelector('a.link') : null,
              headActive: sh ? sh.classList.contains('active') : null,
              itemCount: links.length,
              firstItem: links.length ? links[0].textContent.trim() : null,
              lastItem: links.length ? links[links.length - 1].textContent.trim() : null,
              listDisplay: su ? getComputedStyle(su).display : null
            };
          }
          const a = li.querySelector(':scope > a.series-item');
          return a ? { kind: 'link', text: a.textContent.trim() } : { kind: 'other' };
        }) : [];
        return { head: head ? head.textContent.trim() : null, children: kids };
      });
      return { heads, groups, totalArrows: container.querySelectorAll('.arrow').length };
    })()`);
    console.log(JSON.stringify(res, null, 1));
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('D:/github/gma/.vuepress/_shots/sidebar_check.png', Buffer.from(shot.result.data, 'base64'));
    console.log('screenshot saved');
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* gone */ }
  }
})();
