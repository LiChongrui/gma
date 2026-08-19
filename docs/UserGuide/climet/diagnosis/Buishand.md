---
title: Buishand
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.diagnosis.Buishand</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">Buishand</span><span style="font-style: italic; color: black;font-size: 120%;">(data, axis = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"Q"</span>):</span></span>

<p>Checks homogeneity test using Buishand's methods proposed in T. A. Buishand (1982).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Data to be tested.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Q'</span>. </p>
<p style="margin-left: 4em;">Buishand's method. Supported methods include:</p>
<p style="margin-left: 4em;">'Q', 'Range', 'LL Ration', 'U'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">Statistic:</p>
<p style="margin-left: 6em;">R('Range'): Buishand's Q Statistics range divided by squire root of sample size [R/sqrt(n)].</p>
<p style="margin-left: 6em;">Q('Q'): Maximum of absolute Buishand's Q Statistics divided by squire root of sample size [Q/sqrt(n)].</p>
<p style="margin-left: 6em;">V('LL Ration'): Maximum of absolute Buishand's weighted adjusted partial sum S.</p>
<p style="margin-left: 6em;">U('U'): Buishand's U Statistics.</p>
<p style="margin-left: 4em;">loc: Probable change point location index (Start from 1).</p>
