---
title: RMI
date: 2026-08-15
sidebar: true
---
# gma.climet.index.RMI


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">RMI</span><span style="font-style: italic; color: black;font-size: 130%;">(pre, pet, axis = <span style="color:#48566B">None</span>, scale = <span style="color:#48566B">1</span>):</span></span>

Calculate Relative Moisture Index.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>pre: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Precipitation (mm).</p><p style="text-indent: 1em;"><b>pet: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Potential evapotranspiration (mm).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>axis  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p><p style="text-indent: 1em;"><b>scale  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Time scale. For example: 1, 3 or others.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p><p style="text-indent: 1em;"><b>References</b>.</p><p style="text-indent: 1em;"><b>https: </b> <code style="text-indent: 0">//image.data.cma.cn/staticDry/article/20170927151824947.pdf</code>.</p>

---