---
title: Hargreaves
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.et0.Hargreaves</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">Hargreaves</span><span style="font-style: italic; color: black;font-size: 120%;">(tmax, tmin, lat = <span style="color:#48566B">34.6</span>, TMean = <span style="color:#48566B">None</span>, axis = <span style="color:#48566B">None</span>, start_year = <span style="color:#48566B">1992</span>, start_day_of_year = <span style="color:#48566B">1</span>):</span></span>

<p>Calculate daily potential evapotranspiration based on the Hargreaves (1998) method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>tmax</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Daily maximum temperature (¡æ).</p>
<p style="margin-left: 2em;"><b>tmin</b>: <code style="text-indent: 0em;">float||array</code>. </p>
<p style="margin-left: 4em;">Daily minimum temperature (¡æ).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>lat </b> = <code style="text-indent: 0em;">float||array</code>. <span style="color:#48566B;"> Default 34.6¡ã N</span>. </p>
<p style="margin-left: 4em;">Data latitude value (¡ã).</p>
<p style="margin-left: 4em;">*Note: If lat is an array, it should have the same shape as the input data on the non-computed axis!</p>
<p style="margin-left: 2em;"><b>TMean </b> = <code style="text-indent: 0em;">float||array</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Daily maximum temperature (¡æ). The default (None) is (tmax + tmin) * 0.5.</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>start_year </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1992</span>. </p>
<p style="margin-left: 4em;">Data start year.</p>
<p style="margin-left: 2em;"><b>start_day_of_year </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Data start day of year.</p>
<p style="margin-left: 4em;">*Note: start_year, start_month are based on calculated axis!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">Allen, Richard et al (1998) Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56 ISBN 92-5-104219-5</p>
