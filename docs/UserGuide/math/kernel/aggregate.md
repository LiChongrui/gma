---
title: aggregate
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.math.kernel.aggregate</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">aggregate</span><span style="font-style: italic; color: black;font-size: 130%;">(data, size = <span style="color:#48566B">3</span>, nodata = <span style="color:#48566B">None</span>, axis = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"Max"</span>):</span></span>

Aggregate array.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Data to be calculated.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>size  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 3.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Zoom factor. The output array is scaled by a factor of size.</p><p style="text-indent: 1em;"><b>nodata  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Invalid value in input array. This value will not participate in the aggregation calculation and is automatically set by default (None).</p><p style="text-indent: 1em;"><b>axis  = </b> <code style="text-indent: 0">int||list</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Calculation axis. Automatically expand to all axis by default (None).</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Max'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Aggregation method. Indicate how the value of each output cell is determined.</p><p style="padding-left: 1em;text-indent: 1em;">Supported methods include: 'Mean', 'Max', 'Min', 'Sum', 'Median'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p>

---