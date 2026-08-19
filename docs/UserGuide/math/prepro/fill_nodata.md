---
title: fill_nodata
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.math.prepro.fill_nodata</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">fill_nodata</span><span style="font-style: italic; color: black;font-size: 120%;">(data, nodatas = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"linear"</span>, axis = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Interpolate missing or abnormal values.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">list||tuple||Series||DataFrame||array</code>. </p>
<p style="margin-left: 4em;">Data to be filled.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>nodatas </b> = <code style="text-indent: 0em;">float||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Flags missing values that need to be filled. Can be a number (float) or a list of numbers (list).</p>
<p style="margin-left: 4em;">Note: 1. When nodatas is a list, all values in the list will be interpolated.</p>
<p style="margin-left: 4em;">2. The original NAN, INF, strings that cannot be converted into numbers and other abnormal values in the data will also be interpolated.</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'linear'</span>. </p>
<p style="margin-left: 4em;">Interpolation method. Supported methods include:</p>
<p style="margin-left: 4em;">'index', 'values', 'pad', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'spline', 'barycentric', 'polynomial', 'from_derivatives', 'krogh', 'piecewise_polynomial','pchip', 'akima', 'cubicspline', 'linear'.</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Axis used for data interpolation. By default (None), if the data is less than 3 dimensions, the first dimension is the axis; if the data is higher than 3 dimensions, the penultimate dimension is the axis.</p>
<p style="margin-left: 2em;"><b>**kwargs. Additional arguments to pass to the interpolation function.</b></p>
<p style="margin-left: 4em;">For example: method is 'polynomial' or 'spline', you need to set order (order), the default order is 3.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Series||DataFrame returns the input type; list||tuple||array returns an array</code>. </p>
