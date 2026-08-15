---
title: gamma
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.math.correction.gamma</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">gamma</span><span style="font-style: italic; color: black;font-size: 130%;">(data, constant = <span style="color:#48566B">1</span>, ignore_value = <span style="color:#48566B">None</span>, gamma_v = <span style="color:#48566B">1</span>):</span></span>

Gamma transform. Reference equation: Out = constant * ((data - vvmin) / vptp) ** gamma_v) * vptp.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The data to be corrected.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>constant  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The constant term of the correction factor.</p><p style="text-indent: 1em;"><b>ignore_value  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The value that is not involved in the calculation.</p><p style="text-indent: 1em;"><b>gamma_v  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Gamma value.</p><p style="text-indent: 1em;"><b>**Note</b>.</p><p style="text-indent: 1em;"><b>If the input data type is uint8, the data will be transformed between 0 ~ 255.</b>.</p><p style="text-indent: 1em;"><b>Otherwise, it will transform between the maximum and vminimum values of the input array.</b>.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p>

---