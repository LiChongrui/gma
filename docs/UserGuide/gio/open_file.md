---
title: open_file
date: 2026-08-15
sidebar: true
---
# gma.gio.open_file


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">open_file</span><span style="font-style: italic; color: black;font-size: 130%;">(in_src, flag = <span style="color:#48566B">None</span>, allowed_drivers = <span style="color:#48566B">[]</span>, open_options = <span style="color:#48566B">[]</span>, sibling_files = <span style="color:#48566B">[]</span>):</span></span>

Open a raster or vector file as a Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Name of the file to open.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>flag: </b> <code style="text-indent: 0">int||None</code>. <span style="color:#48566B;">Default = None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Flag controlling how the Dataset is opened. None for auto.</p><p style="text-indent: 1em;"><b>allowed_drivers: </b> <code style="text-indent: 0">list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A list of the names of drivers that may attempt to open.</p><p style="text-indent: 1em;"><b>open_options: </b> <code style="text-indent: 0">dict/list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A dict or list of name=value driver-specific opening options.</p><p style="text-indent: 1em;"><b>sibling_files: </b> <code style="text-indent: 0">list</code>. <span style="color:#48566B;">Default = [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    A list of filenames that are auxiliary to the main filename.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">GeoDatabase</code>.</p>

---