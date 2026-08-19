---
title: aggregate
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.math.kernel.aggregate</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">aggregate</span><span style="font-style: italic; color: black;font-size: 120%;">(data, size = <span style="color:#48566B">3</span>, nodata = <span style="color:#48566B">None</span>, axis = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"Max"</span>):</span></span>

<p>Aggregate array.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Data to be calculated.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 3</span>. </p>
<p style="margin-left: 4em;">Zoom factor. The output array is scaled by a factor of size.</p>
<p style="margin-left: 2em;"><b>nodata </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Invalid value in input array. This value will not participate in the aggregation calculation and is automatically set by default (None).</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. Automatically expand to all axis by default (None).</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Max'</span>. </p>
<p style="margin-left: 4em;">Aggregation method. Indicate how the value of each output cell is determined.</p>
<p style="margin-left: 4em;">Supported methods include:</p>
<p style="margin-left: 4em;">'Mean', 'Max', 'Min', 'Sum', 'Median'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
