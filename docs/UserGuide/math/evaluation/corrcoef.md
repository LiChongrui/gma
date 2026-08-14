---
title: corrcoef
date: 2026-08-14
sidebar: true
---
# gma.math.evaluation.corrcoef


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">corrcoef</span><span style="font-style: italic; color: black;font-size: 130%;">(real, pred, method = <span style="color:#48566B">"pearson"</span>, axis = <span style="color:#48566B">0</span>):</span></span>

Correlation coefficient and significance.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>real: </b> <code>array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Measured data.</p><p style="text-indent: 1em;"><b>pred: </b> <code>array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Simulation data.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>method  = </b> <code>str</code>. <span style="color:#48566B;">Default 'pearson'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Supported methods include: 'pearson', 'kendall', 'spearman'.</p><p style="text-indent: 1em;"><b>axis  = </b> <code>int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The axis to use for calculations.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>namedtuple</code>.</p>

---