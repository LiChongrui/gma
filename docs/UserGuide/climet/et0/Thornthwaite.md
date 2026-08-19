---
title: Thornthwaite
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.et0.Thornthwaite</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">Thornthwaite</span><span style="font-style: italic; color: black;font-size: 120%;">(tem, lat = <span style="color:#48566B">34.6</span>, axis = <span style="color:#48566B">None</span>, start_year = <span style="color:#48566B">1992</span>, start_month = <span style="color:#48566B">1</span>):</span></span>

<p>Calculate monthly potential evapotranspiration based on the Thornthwaite (1948) method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>tem</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Monthly mean temperature (¡æ).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>lat </b> = <code style="text-indent: 0em;">float||array</code>. <span style="color:#48566B;"> Default 34.6¡ã N</span>. </p>
<p style="margin-left: 4em;">Data latitude value (¡ã).</p>
<p style="margin-left: 4em;">*Note: If lat is an array, it should have the same shape as the input data on the non-computed axis!</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>start_year </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1992</span>. </p>
<p style="margin-left: 4em;">Data start year.</p>
<p style="margin-left: 2em;"><b>start_month </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Defaults 1</span>. </p>
<p style="margin-left: 4em;">Data start month of year.</p>
<p style="margin-left: 2em;"><b>*Note</b>: <code style="text-indent: 0em;">start_year||start_month are based on calculated axis!</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">Thornthwaite, C.W. (1948) An approach toward a rational classification of climate. Geographical Review, Vol. 38, 55-94.</p>
