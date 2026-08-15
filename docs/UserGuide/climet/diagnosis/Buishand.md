---
title: Buishand
date: 2026-08-15
sidebar: true
---
# gma.climet.diagnosis.Buishand


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Buishand</span><span style="font-style: italic; color: black;font-size: 130%;">(data, axis = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"Q"</span>):</span></span>

Checks homogeneity test using Buishand's methods proposed in T. A. Buishand (1982).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Data to be tested.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>axis  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Q'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Buishand's method. Supported methods include: 'Q', 'Range', 'LL Ration', 'U'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">namedtuple</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Statistic: R('Range'): Buishand's Q Statistics range divided by squire root of sample size [R/sqrt(n)].</p><p style="padding-left: 1em;text-indent: 1em;">Q('Q'): Maximum of absolute Buishand's Q Statistics divided by squire root of sample size [Q/sqrt(n)].</p><p style="padding-left: 1em;text-indent: 1em;">V('LL Ration'): Maximum of absolute Buishand's weighted adjusted partial sum S.</p><p style="padding-left: 1em;text-indent: 1em;">U('U'): Buishand's U Statistics.</p><p style="padding-left: 1em;text-indent: 1em;">loc: Probable change point location index (Start from 1).</p>

---