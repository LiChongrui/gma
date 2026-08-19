---
title: PenmanMonteith
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.et0.PenmanMonteith</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">PenmanMonteith</span><span style="font-style: italic; color: black;font-size: 120%;">(prs, win, tmax, tmin, rhu, ssh, lat, Day, ele):</span></span>

<p>Calculate daily crop reference evapotranspiration based on the Penman-Monteith (FAO-56) method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>prs</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Daily mean air pressure (hPa).</p>
<p style="margin-left: 2em;"><b>win</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Average daily wind speed of 10m (m/s).</p>
<p style="margin-left: 2em;"><b>tmax</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Daily maximum temperature (¡æ).</p>
<p style="margin-left: 2em;"><b>tmin</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Daily minimum temperature (¡æ).</p>
<p style="margin-left: 2em;"><b>rhu</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Average daily relative humidity (%).</p>
<p style="margin-left: 2em;"><b>ssh</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Hours of sunshine (hr).</p>
<p style="margin-left: 2em;"><b>lat</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Latitude (¡ã).</p>
<p style="margin-left: 2em;"><b>Day</b>: <code style="text-indent: 0em;">int||array</code>. </p>
<p style="margin-left: 4em;">Day of year. 1-365 (normal year) or 366 (leap year).</p>
<p style="margin-left: 2em;"><b>ele</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Altitude (m).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">float||array</code>. </p>
