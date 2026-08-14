---
title: Pettitt
date: 2026-08-14
sidebar: true
---
# gma.climet.diagnosis.Pettitt


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Pettitt</span><span style="font-style: italic; color: black;font-size: 130%;">(data, axis = <span style="color:#48566B">None</span>):</span></span>

Checks homogeneity test using A. N. Pettitt's (1979) method.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code>array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Data to be tested.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>axis  = </b> <code>int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>namedtuple</code>.</p><p style="padding-left: 1em;text-indent: 1em;">u_max: Maximum of absolute Pettitt's U Statistics.</p><p style="padding-left: 1em;text-indent: 1em;">loc: Probable change point location index (Start from 1).</p><p style="padding-left: 1em;text-indent: 1em;">p: p-value of the significance test.</p>

---