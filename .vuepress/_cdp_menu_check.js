/* 量 navbar 下拉菜单（API reference）各层条目的真实盒模型 */
const { spawn } = require('child_process');
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9352;
const PROFILE = 'D:/github/gma/.vuepress/_shots/pfMenu';
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
    // 强制展开第一个下拉菜单（API reference），绕过 hover 逻辑
    const res = await evalJs(`(() => {
      const dd = document.querySelector('.dropdown-link');
      if (!dd) return { err: 'no dropdown' };
      dd.classList.add('open');
      const ul = dd.querySelector('.dropdown-link__container');
      const items = [...dd.querySelectorAll(':scope .dropdown-link__item')].slice(0, 4);
      const subs = [...dd.querySelectorAll(':scope .dropdown-link__subitem .link')].slice(0, 4);
      const liSub = dd.querySelector(':scope .dropdown-link__subitem');
      const liCs = liSub ? getComputedStyle(liSub) : null;
      const itemCs = items[1] ? getComputedStyle(items[1]) : null;
      const sub1 = subs[0] ? getComputedStyle(subs[0]) : null;
      const sub2 = subs[1] ? getComputedStyle(subs[1]) : null;
      const r1 = subs[0] ? subs[0].getBoundingClientRect() : null;
      const r2 = subs[1] ? subs[1].getBoundingClientRect() : null;
      const subtitle = dd.querySelector('.dropdown-link__subtitle');
      const scs = subtitle ? getComputedStyle(subtitle) : null;
      return {
        n_items: dd.querySelectorAll(':scope .dropdown-link__item').length,
        n_subs: dd.querySelectorAll(':scope .dropdown-link__subitem').length,
        sub_font: sub1 ? sub1.fontSize : null,
        sub_lineheight: sub1 ? sub1.lineHeight : null,
        sub_padding: sub1 ? sub1.paddingTop + '/' + sub1.paddingBottom : null,
        sub_margin: sub1 ? sub1.marginTop + '/' + sub1.marginBottom : null,
        sub_display: sub1 ? sub1.display : null,
        li_lineheight: liCs ? liCs.lineHeight : null,
        li_padding: liCs ? liCs.paddingTop + '/' + liCs.paddingBottom : null,
        li_margin: liCs ? liCs.marginTop + '/' + liCs.marginBottom : null,
        item_lineheight: itemCs ? itemCs.lineHeight : null,
        sub_h: r1 ? Math.round(r1.height) : null,
        gap_between_subs: (r1 && r2) ? Math.round(r2.top - r1.bottom) : null,
        subtitle_margin: scs ? scs.marginTop + '/' + scs.marginBottom : null,
        subtitle_padding: scs ? scs.paddingTop + '/' + scs.paddingBottom : null,
        subtitle_lineheight: scs ? scs.lineHeight : null
      };
    })()`);
    console.log(JSON.stringify(res, null, 1));
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('D:/github/gma/.vuepress/_shots/menu_open.png', Buffer.from(shot.result.data, 'base64'));
    console.log('screenshot saved');
    ws.close();
  } finally {
    try { process.kill(proc.pid); } catch (e) { /* gone */ }
  }
})();
