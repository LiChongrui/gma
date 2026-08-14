---
title: moving\_average
date: 2026-08-14
sidebar: true
---
# gma.math.smooth.moving_average


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">moving_average</span><span style="font-style: italic; color: black;font-size: 130%;">(data, window_size = <span style="color:#48566B">5</span>, times = <span style="color:#48566B">1</span>, edge_mode = <span style="color:#48566B">"interp"</span>, axis = <span style="color:#48566B">0</span>):</span></span>

Data smoothing based on moving average method.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code>array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Data that needs smoothing.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>window_size  = </b> <code>int</code>. <span style="color:#48566B;">Default 5.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Smoothing window size. Must be a positive odd number.</p><p style="text-indent: 1em;"><b>times  = </b> <code>int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Smoothing times.</p><p style="text-indent: 1em;"><b>edge_mode  = </b> <code>str</code>. <span style="color:#48566B;">Default 'interp'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Edge data processing methods. Supported methods include: 'nearest', 'mirror', 'interp', 'wrap'.</p><p style="text-indent: 1em;"><b>axis  = </b> <code>int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The axis to use for data smoothing. </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>array</code>.</p>

---