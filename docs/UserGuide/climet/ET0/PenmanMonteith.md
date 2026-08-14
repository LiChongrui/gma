---
title: PenmanMonteith
date: 2026-08-14
sidebar: true
---
# gma.climet.et0.PenmanMonteith


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">PenmanMonteith</span><span style="font-style: italic; color: black;font-size: 130%;">(prs, win, tmax, tmin, rhu, ssh, lat, Day, ele):</span></span>

Calculate daily crop reference evapotranspiration based on the Penman-Monteith (FAO-56) method.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>prs: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Daily mean air pressure (hPa).</p><p style="text-indent: 1em;"><b>win: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Average daily wind speed of 10m (m/s).</p><p style="text-indent: 1em;"><b>tmax: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Daily maximum temperature (¡æ).</p><p style="text-indent: 1em;"><b>tmin: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Daily minimum temperature (¡æ).</p><p style="text-indent: 1em;"><b>rhu: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Average daily relative humidity (%).</p><p style="text-indent: 1em;"><b>ssh: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Hours of sunshine (hr).</p><p style="text-indent: 1em;"><b>lat: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Latitude (¡ã).</p><p style="text-indent: 1em;"><b>Day: </b> <code>int||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Day of year. 1-365 (normal year) or 366 (leap year).</p><p style="text-indent: 1em;"><b>ele: </b> <code>float||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Altitude (m).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>float||array</code>.</p>

---