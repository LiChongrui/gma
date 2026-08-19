---
title: max_min
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.math.stretch.max_min</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">max_min</span><span style="font-style: italic; color: black;font-size: 120%;">(data, min_label = <span style="color:#48566B">None</span>, max_label = <span style="color:#48566B">None</span>, ignore_value = <span style="color:#48566B">None</span>, MinV = <span style="color:#48566B">None</span>, MaxV = <span style="color:#48566B">None</span>):</span></span>

<p>Use linear stretching with the minimum and maximum output pixel values as the endpoints of the histogram.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">The data to be stretched.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>min_label </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Minimum value after stretching. Default(None) is the minimum value of the input data.</p>
<p style="margin-left: 2em;"><b>max_label </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Maximum value after stretching. Default(None) is the maximum value of the input data.</p>
<p style="margin-left: 2em;"><b>ignore_value </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The value that is not involved in the calculation.</p>
<p style="margin-left: 2em;"><b>MinV </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Minimum value. Default(None) is the minimum value of the input data.</p>
<p style="margin-left: 2em;"><b>MaxV </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Maximum value. Default(None) is the minimum value of the input data.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
