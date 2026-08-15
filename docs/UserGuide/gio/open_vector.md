---
title: open_vector
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.gio.open_vector</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">open_vector</span><span style="font-style: italic; color: black;font-size: 130%;">(in_src, name_or_id = <span style="color:#48566B">0</span>, allowed_drivers = <span style="color:#48566B">[]</span>, open_options = <span style="color:#48566B">[]</span>, sibling_files = <span style="color:#48566B">[]</span>):</span></span>

Open a raster or vector file as a Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Name of the file to open.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name_or_id  = </b> <code style="text-indent: 0">int||str</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Layer id or name in the GeoDatabase to get.</p><p style="text-indent: 1em;"><b>allowed_drivers: </b> <code style="text-indent: 0">list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A list of the names of drivers that may attempt to open.</p><p style="text-indent: 1em;"><b>open_options: </b> <code style="text-indent: 0">dict/list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A dict or list of name=value driver-specific opening options.</p><p style="text-indent: 1em;"><b>sibling_files: </b> <code style="text-indent: 0">list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A list of filenames that are auxiliary to the main filename.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---