---
title: PCI
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.climet.index.PCI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">PCI</span><span style="font-style: italic; color: black;font-size: 120%;">(pre, axis = <span style="color:#48566B">None</span>, scale = <span style="color:#48566B">1</span>, periodicity = <span style="color:#48566B">12</span>):</span></span>

<p>Calculate Precipitation Concentration Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>pre</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Precipitation (mm).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>axis </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculation axis. If not set (None), multidimensional data will be expanded to 1 dimension for calculation.</p>
<p style="margin-left: 2em;"><b>scale </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Time scale. For example: 1, 3 or others.</p>
<p style="margin-left: 2em;"><b>periodicity </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 12</span>. </p>
<p style="margin-left: 4em;">Periodicity of data. For example: the monthly scale can have a period of 12.</p>
<p style="margin-left: 2em;"><b>*Note</b>: <code style="text-indent: 0em;">scale||periodicity are based on calculated axis!</code>. </p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 2em;"><b>*Note</b>: </p>
<p style="margin-left: 4em;">1.The PCI index scales down the amount of axis data. On axis,</p>
<p style="margin-left: 2em;"><b>there is only one set of results per periodicity.</b></p>
<p style="margin-left: 4em;">2.Data on axis with less than one periodicity will not be computed!.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">De Luis M, Gonz¨¢lez-Hidalgo J C, Ravent¨®s J, et al. 1997. Distribucion espacial de la concentracion y agresividad de la lluvia en el territorio de la Comunidad Valenciana [J]. Cuaternario y Geomorfologia, 11: 33¨C44. Oliver J E. 1980. Monthly precipitation distribution: A comparative index [J]. Professional Geographer, 32: 300¨C309.</p>
