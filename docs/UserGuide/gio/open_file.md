---
title: open_file
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.open_file</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">open_file</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, flag = <span style="color:#48566B">None</span>, allowed_drivers = <span style="color:#48566B">[]</span>, open_options = <span style="color:#48566B">[]</span>, sibling_files = <span style="color:#48566B">[]</span>):</span></span>

<p>Open a raster or vector file as a Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Name of the file to open.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>flag </b> = <code style="text-indent: 0em;">int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Flag controlling how the Dataset is opened. None for auto.</p>
<p style="margin-left: 2em;"><b>allowed_drivers </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A list of the names of drivers that may attempt to open.</p>
<p style="margin-left: 2em;"><b>open_options </b> = <code style="text-indent: 0em;">dict/list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A dict or list of name=value driver-specific opening options.</p>
<p style="margin-left: 2em;"><b>sibling_files </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">A list of filenames that are auxiliary to the main filename.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">GeoDatabase</code>. </p>
