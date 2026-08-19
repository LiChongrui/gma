---
title: SNHT
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.diagnosis.SNHT</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">SNHT</span><span style="font-style: italic; color: black;font-size: 120%;">(data, axis = <span style="color:#48566B">None</span>):</span></span>

<p>Checks homogeneity test using H. Alexandersson (1986) method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Data to be tested.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">MAXT: Maximum of SNHT T Statistics.</p>
<p style="margin-left: 4em;">loc: Probable change point location index (Start from 1).</p>
