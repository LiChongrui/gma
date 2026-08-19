---
title: RMI
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.index.RMI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">RMI</span><span style="font-style: italic; color: black;font-size: 120%;">(pre, pet, axis = <span style="color:#48566B">None</span>, scale = <span style="color:#48566B">1</span>):</span></span>

<p>Calculate Relative Moisture Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>pre</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Precipitation (mm).</p>
<p style="margin-left: 2em;"><b>pet</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Potential evapotranspiration (mm).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>scale </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Time scale. For example: 1, 3 or others.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">https://image.data.cma.cn/staticDry/article/20170927151824947.pdf</p>
