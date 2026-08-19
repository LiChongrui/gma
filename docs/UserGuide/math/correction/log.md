---
title: log
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.math.correction.log</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">log</span><span style="font-style: italic; color: black;font-size: 120%;">(data, constant = <span style="color:#48566B">1</span>, ignore_value = <span style="color:#48566B">None</span>, inverse = <span style="color:#48566B">False</span>):</span></span>

<p>Logarithmic transformation. Reference equation: Out = log2(1 + (data - vmin) / vptp) * vptp * constant.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">The data to be corrected.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>constant </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">The constant term of the correction factor.</p>
<p style="margin-left: 2em;"><b>ignore_value </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The value that is not involved in the calculation.</p>
<p style="margin-left: 2em;"><b>inverse </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to perform the inverse change.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
