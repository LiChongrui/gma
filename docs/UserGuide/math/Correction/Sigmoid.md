---
title: sigmoid
date: 2026-08-15
sidebar: true
---
# gma.math.correction.sigmoid


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">sigmoid</span><span style="font-style: italic; color: black;font-size: 130%;">(data, constant = <span style="color:#48566B">1</span>, ignore_value = <span style="color:#48566B">None</span>, inverse = <span style="color:#48566B">False</span>, cutoff = <span style="color:#48566B">0.5</span>):</span></span>

S-shaped curve function transformation. Reference equation: Out = 1 / (1 + exp(constant * (cutoff - (data - vmin) / vptp))) * vptp.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The data to be corrected.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>constant  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The constant term of the correction factor.</p><p style="text-indent: 1em;"><b>ignore_value  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The value that is not involved in the calculation.</p><p style="text-indent: 1em;"><b>inverse  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to perform the inverse change.</p><p style="text-indent: 1em;"><b>cutoff  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default 0.5.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The intercept point of the S-curve. The default is the midpoint (0.5).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p>

---