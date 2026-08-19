---
title: SWAP
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.index.SWAP</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">SWAP</span><span style="font-style: italic; color: black;font-size: 120%;">(pre, a = <span style="color:#48566B">0.9</span>, n = <span style="color:#48566B">44</span>, axis = <span style="color:#48566B">None</span>, scale = <span style="color:#48566B">1</span>, periodicity = <span style="color:#48566B">365</span>, distribution = <span style="color:#48566B">"Gamma"</span>, fit_method = <span style="color:#48566B">"MLE"</span>, calibration = <span style="color:#48566B">None</span>):</span></span>

<p>Calculate the Standardized Weighted Average of Precipitation.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>pre</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Precipitation (mm).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>a </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.9</span>. </p>
<p style="margin-left: 4em;">The parameter of weight decay over time.</p>
<p style="margin-left: 2em;"><b>N </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 44</span>. </p>
<p style="margin-left: 4em;">Days of Impact in the Early Stage.</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>scale </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Time scale. For example: 1, 3 or others.</p>
<p style="margin-left: 2em;"><b>periodicity </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 365</span>. </p>
<p style="margin-left: 4em;">periodicity of data. For example: the monthly scale can have a period of 12.</p>
<p style="margin-left: 2em;"><b>distribution </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Gamma'</span>. </p>
<p style="margin-left: 4em;">Distribution type to be used for the internal fitting/transform computation.</p>
<p style="margin-left: 4em;">Supported distributions include:</p>
<p style="margin-left: 6em;">'Gamma', 'LogLogistic', 'Pearson3'.</p>
<p style="margin-left: 2em;"><b>fit_method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'MLE'</span>. </p>
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
<p style="text-indent: 2em;">J2009-Determining the start, duration, and strength of flood and drought with daily precipitation: Rational J2014-The day-to-day monitoring of the 2011 severe drought in China. GB/T 20481¡ª201¡Á Grades of meteorological drought.</p>
