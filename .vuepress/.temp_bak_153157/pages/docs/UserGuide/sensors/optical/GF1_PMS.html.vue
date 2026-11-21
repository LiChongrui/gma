<template><div><p style="font-size: 120%;font-weight: bold;">gma.sensors.optical.GF1_PMS</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GF1_PMS</span><span style="font-style: italic; color: black;font-size: 130%;">(infile):</span></span>
<p>The image must be accompanied by an XML metadata file (the same name as the image, with a <code>.xml</code> extension, in the same path) for radiometric calibration.</p>
<p>Create a GF-1 PMS sensor object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>infile</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The GF-1 PMS image file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to gma.gio.open_raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">GF1_PMS</code>. </p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="radiometric-calibration-out-file-none" tabindex="-1"><a class="header-anchor" href="#radiometric-calibration-out-file-none"><span>radiometric_calibration<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_file = None)</span></span></a></h3>
<p>Radiometric calibration based on the XML metadata of the GF-1 PMS image.</p>
<p>The gain and offset are read from the XML metadata ('AbsCeof' and 'AOffset') by default, and can be overridden by AGain and AOffset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>out_file</b> = <code style="text-indent: 0em;">str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The output raster file path. If not set (None), a memory file is created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">AGain = float or list. Absolute calibration gain for each band. Default is read from XML ('AbsCeof').</p>
<p style="margin-left: 4em;">AOffset = float or list. Absolute calibration offset for each band. Default is read from XML ('AOffset').</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
<h3 id="orthorectification-out-file-none-dem-none" tabindex="-1"><a class="header-anchor" href="#orthorectification-out-file-none-dem-none"><span>orthorectification<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_file = None, dem = None)</span></span></a></h3>
<p>Orthorectify the image based on RPC (Rational Polynomial Coefficients) metadata.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>out_file</b> = <code style="text-indent: 0em;">str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The output raster file path. If not set (None), a memory file is created.</p>
<p style="margin-left: 2em;"><b>dem</b> = <code style="text-indent: 0em;">str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The DEM file path used for RPC calculations.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to gma.etools.orthorectification.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
</div></template>


