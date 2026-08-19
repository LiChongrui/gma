---
title: moving_average
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.math.smooth.moving_average</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">moving_average</span><span style="font-style: italic; color: black;font-size: 120%;">(data, window_size = <span style="color:#48566B">5</span>, times = <span style="color:#48566B">1</span>, edge_mode = <span style="color:#48566B">"interp"</span>, axis = <span style="color:#48566B">0</span>):</span></span>

<p>Data smoothing based on moving average method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>data</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Data that needs smoothing.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>window_size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 5</span>. </p>
<p style="margin-left: 4em;">Smoothing window size. Must be a positive odd number.</p>
<p style="margin-left: 2em;"><b>times </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Smoothing times.</p>
<p style="margin-left: 2em;"><b>edge_mode </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'interp'</span>. </p>
<p style="margin-left: 4em;">Edge data processing methods. Supported methods include:</p>
<p style="margin-left: 4em;">'nearest', 'mirror', 'interp', 'wrap'.</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The axis to use for data smoothing.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
