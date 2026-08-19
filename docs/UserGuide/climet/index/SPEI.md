---
title: SPEI
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.index.SPEI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">SPEI</span><span style="font-style: italic; color: black;font-size: 120%;">(pre, pet, axis = <span style="color:#48566B">None</span>, scale = <span style="color:#48566B">1</span>, periodicity = <span style="color:#48566B">12</span>, distribution = <span style="color:#48566B">"LogLogistic"</span>, fit_method = <span style="color:#48566B">"LMoment"</span>, calibration = <span style="color:#48566B">None</span>):</span></span>

<p>Calculate the Standardized Precipitation Evapotranspiration Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>pre</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Precipitation (mm).</p>
<p style="margin-left: 2em;"><b>pet</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Potential evapotranspiration (mm).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>scale </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Time scale. For example: 1, 3 or others.</p>
<p style="margin-left: 2em;"><b>periodicity </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 12</span>. </p>
<p style="margin-left: 4em;">Periodicity of data. For example: the monthly scale can have a period of 12.</p>
<p style="margin-left: 2em;"><b>distribution </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'LogLogistic'</span>. </p>
<p style="margin-left: 4em;">Distribution type to be used for the internal fitting/transform computation.</p>
<p style="margin-left: 4em;">Supported distributions include:</p>
<p style="margin-left: 6em;">'Gamma', 'LogLogistic', 'Pearson3'.</p>
<p style="margin-left: 2em;"><b>fit_method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'LMoment'</span>. </p>
<p style="margin-left: 4em;">Fitting methods for distribution parameters.</p>
<p style="margin-left: 4em;">Supported method include:</p>
<p style="margin-left: 6em;">'MLE': Maximum Likelihood Estimation, 'LMoment': L-Moment Estimation(PWD), 'LMoment2': L-Moment Estimation.</p>
<p style="margin-left: 2em;"><b>calibration </b> = <code style="text-indent: 0em;">list||slice||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Fit the calibration interval of distribution parameter data, Based on the periodicity.</p>
<p style="margin-left: 4em;">Default(None) using all data. For example:</p>
<p style="margin-left: 6em;">Select the data from 1-5 periodicity to fit parameters:</p>
<p style="margin-left: 8em;">calibration = [0, 5]</p>
<p style="margin-left: 6em;">Then apply the parameter fitting results to all data.</p>
<p style="margin-left: 2em;"><b>*Note</b>: <code style="text-indent: 0em;">scale||periodicity||Calibration are based on calculated axis!</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">Vicente-Serrano S M , S Beguer¨ªa, JI L¨®pez-Moreno. A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index[J]. Journal of Climate, 2010, 23(7):1696-1718.</p>
