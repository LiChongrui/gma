<template><div><p style="font-size: 120%;font-weight: bold;">gma.carto.appearance.MapAppearance</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">MapAppearance</span><span style="font-style: italic; color: black;font-size: 130%;">(map_app, map_frame, loc = <span style="color:#48566B">(0, 0)</span>, size = <span style="color:#48566B">0.1</span>):</span></span>
<p>Add a map appearance (ScaleBar or Compass) to the map frame.</p>
<p>Usually created via MapFrame.add_appearance().</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>map_app</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Map appearance type. Supported types include:</p>
<p style="margin-left: 4em;">'ScaleBarNormal1', 'CompassNormal1', 'CompassNormal2', 'CompassNormal3'.</p>
<p style="margin-left: 2em;"><b>map_frame</b>: <code style="text-indent: 0em;">MapFrame</code>. </p>
<p style="margin-left: 4em;">The map frame that the appearance is attached to.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>loc</b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default (0, 0)</span>. </p>
<p style="margin-left: 4em;">The location of the map appearance. The coordinate system is the same as the map frame.</p>
<p style="margin-left: 2em;"><b>size</b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.1</span>. </p>
<p style="margin-left: 4em;">The size of the map appearance. The unit is the same as the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">MapAppearance</code>. </p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="plot" tabindex="-1"><a class="header-anchor" href="#plot"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Plot the map appearance on the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">text_prop_{group}: dict.</p>
<p style="margin-left: 4em;">Text properties for the matplotlib.~.Text. {group} is in self._items['texts'] keys.</p>
<p style="margin-left: 4em;">e.g., text_prop_unit = {'fontsize': 10, 'color': 'red'}</p>
<p style="margin-left: 4em;">coll_prop_{group}: dict.</p>
<p style="margin-left: 4em;">Collection properties for matplotlib.~.Collection. {group} is in self._items['colls'] keys.</p>
<p style="margin-left: 4em;">e.g., coll_prop_main = {'facecolors': 'blue', 'edgecolors': 'black'}</p>
</div></template>


