---
title: pansharpen
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.etools.pansharpen</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">pansharpen</span><span style="font-style: italic; color: black;font-size: 120%;">(in_pan, in_multi, out_dst, resample = <span style="color:#48566B">"Cubic"</span>, spat_adjust = <span style="color:#48566B">"Union"</span>, bands = <span style="color:#48566B">None</span>, threads = <span style="color:#48566B">None</span>, bit_depth = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Fusion of panchromatic and multispectral images based on Pansharpen method.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_pan</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The panchromatic image path.</p>
<p style="margin-left: 2em;"><b>in_multi</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The multispectral image path.</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output raster file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>resample</b>: <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Cubic'</span>. </p>
<p style="margin-left: 4em;">Resampling method. Supported resampling methods include:</p>
<p style="margin-left: 4em;">'Nearest', 'Bilinear', 'Cubic', 'CubicSpline', 'Lanczos', 'Average'.</p>
<p style="margin-left: 2em;"><b>spat_adjust</b>: <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Union'</span>. </p>
<p style="margin-left: 4em;">Space coordinate system adjustment. Supported adjustments methods include:</p>
<p style="margin-left: 4em;">'Union', 'Intersection', 'None', 'NoneWithoutWarning'.</p>
<p style="margin-left: 2em;"><b>bands </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">List of fused multispectral bands. For example [1,2...], the band count starts at 1.</p>
<p style="margin-left: 4em;">The default is to fuse all bands of the input multispectral data (None).</p>
<p style="margin-left: 4em;">***The weight value ('weights') for each band is the same, determined by the number of Bands, which is 1 / len(Bands).</p>
<p style="margin-left: 2em;"><b>threads </b> = <code style="text-indent: 0em;">int||'ALL_CPUS'||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The number of threads that converge on the computer's CPU. Multithreading is not used by default (None).</p>
<p style="margin-left: 2em;"><b>bit_depth </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The amount of information used to represent each pixel or sample.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
