---
title: CWDI
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.index.CWDI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">CWDI</span><span style="font-style: italic; color: black;font-size: 120%;">(pre, etc, axis = <span style="color:#48566B">None</span>, weights = <span style="color:#48566B">[0.1, 0.15, 0.2, 0.25, 0.3]</span>, duration_per_weight = <span style="color:#48566B">10</span>):</span></span>

<p>Calculate Crop Water Deficit Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>pre</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Precipitation (mm).</p>
<p style="margin-left: 2em;"><b>etc</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Crop water requirements (mm).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>weights </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default [0.1, 0.15, 0.2, 0.25, 0.3]</span>. </p>
<p style="margin-left: 4em;">Weighting factors. The length of weights determines the number of weighting factors, and the sum of weights should be 1. Date from oldest to newest.</p>
<p style="margin-left: 2em;"><b>duration_per_weight </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 10</span>. </p>
<p style="margin-left: 4em;">The length of water deficit corresponding to each weighting factor.</p>
<p style="margin-left: 2em;"><b>*Note</b>: <code style="text-indent: 0em;">The data used in calculating each CWDI is len(weights) ¡Á duration_per_weight</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array(%)</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">Li Chongrui, You Songcai, Wu Yongfeng, Wang Yihao. Improved crop water deficit index for monitoring drought disaster change process of spring maize in the Northeast China[J]. Transactions of the Chinese Society of Agricultural Engineering (Transactions of the CSAE), 2019, 35(21): 175-185. DOI: 10.11975/j.issn.1002-6819.2019.21.021</p>
