---
title: std
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.math.stretch.std</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">std</span><span style="font-style: italic; color: black;font-size: 130%;">(data, min_label = <span style="color:#48566B">None</span>, max_label = <span style="color:#48566B">None</span>, ignore_value = <span style="color:#48566B">None</span>, num_of_std = <span style="color:#48566B">2</span>):</span></span>

Standard deviation stretch. This method is used to emphasize how much feature values vary from the mean value; it is best when used on normally distributed data.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The data to be stretched.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>min_label  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Minimum value after stretching. Default(None) is the minimum value of the input data.</p><p style="text-indent: 1em;"><b>max_label  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Maximum value after stretching. Default(None) is the maximum value of the input data.</p><p style="text-indent: 1em;"><b>ignore_value  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The value that is not involved in the calculation.</p><p style="text-indent: 1em;"><b>num_of_std  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 2.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of standard deviation.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p>

---