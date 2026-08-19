---
title: open_raster
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.open_raster</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">open_raster</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, name_or_id = <span style="color:#48566B">0</span>, allowed_drivers = <span style="color:#48566B">[]</span>, open_options = <span style="color:#48566B">[]</span>, sibling_files = <span style="color:#48566B">[]</span>):</span></span>

<p>Open a raster or vector file as a Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Name of the file to open.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int||str</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Dataset id or name in the GeoDatabase to get.</p>
<p style="margin-left: 2em;"><b>allowed_drivers </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A list of the names of drivers that may attempt to open.</p>
<p style="margin-left: 2em;"><b>open_options </b> = <code style="text-indent: 0em;">dict/list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A dict or list of name=value driver-specific opening options.</p>
<p style="margin-left: 2em;"><b>sibling_files </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A list of filenames that are auxiliary to the main filename.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
