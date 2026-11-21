<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.FieldType</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldType</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">"UNKNOWN"</span>):</span></span>
<p>Create a FieldType object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the field. None for dtype name.</p>
<p style="margin-left: 2em;"><b>dtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'UNKNOWN'</span>. </p>
<p style="margin-left: 4em;">The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="set-precision-precision" tabindex="-1"><a class="header-anchor" href="#set-precision-precision"><span>set_precision<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(precision)</span></span></a></h3>
<p>Set the formatting precision for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new precision.</p>
<h3 id="set-type-f-dtype" tabindex="-1"><a class="header-anchor" href="#set-type-f-dtype"><span>set_type<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(f_dtype)</span></span></a></h3>
<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>f_dtype</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">the new field data type</p>
<h3 id="set-width-width" tabindex="-1"><a class="header-anchor" href="#set-width-width"><span>set_width<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(width)</span></span></a></h3>
<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>width</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new width</p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="default" tabindex="-1"><a class="header-anchor" href="#default"><span>default</span></a></h3>
<p style="margin-left: 2em;">Field default value. --> <code style="text-indent: 0em;">str/int/float/...</code></p>
<h3 id="ftype" tabindex="-1"><a class="header-anchor" href="#ftype"><span>ftype</span></a></h3>
<p style="margin-left: 2em;">Field data type. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<p style="margin-left: 2em;">Field name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="precision" tabindex="-1"><a class="header-anchor" href="#precision"><span>precision</span></a></h3>
<p style="margin-left: 2em;">Field precision. --> <code style="text-indent: 0em;">int</code></p>
<h3 id="width" tabindex="-1"><a class="header-anchor" href="#width"><span>width</span></a></h3>
<p style="margin-left: 2em;">Field width. --> <code style="text-indent: 0em;">int</code></p>
</div></template>


