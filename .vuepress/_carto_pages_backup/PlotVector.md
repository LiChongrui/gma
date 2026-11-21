---
title: PlotVector
date: 2026-11-20
---


<p style="font-size: 120%;font-weight: bold;">gma.carto.vector.PlotVector</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">PlotVector</span><span style="font-style: italic; color: black;font-size: 130%;">(vector, map_frame):</span></span>

<p>An object for plotting vector (Layer/Feature/Geometry).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>vector</b>: <code style="text-indent: 0em;">Layer, Feature or Geometry</code>. </p>
<p style="margin-left: 4em;">A vector object to be plotted.</p>
<p style="margin-left: 2em;"><b>map_frame</b>: <code style="text-indent: 0em;">MapFrame</code>. </p>
<p style="margin-left: 4em;">The map frame to be plotted on.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">PlotVector</code>. </p>

## Method

### plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(style = None)</span>

<p>Add a map vector(Layer/Feature/Geometry) to this map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>style</b> = <code style="text-indent: 0em;">None or styles.GeometryStyles</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Plotting Styles. For more, see: ~styles.GeometryStyles</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other plotting parameters when style = None. For more, see:</p>
<p style="margin-left: 4em;">~.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">list of PolyCollection/LineCollection/PointCollection</code>. </p>

### add_legend<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(labels = None, fields = None, connector = "", title = None)</span>

<p>Place a legend of the vector on the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>labels</b> = <code style="text-indent: 0em;">str, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Manually set the feature labels. The number should be the same as the number of layer features.</p>
<p style="margin-left: 4em;">Otherwise, the shortfall will be assigned as null. Default(None) no labels.</p>
<p style="margin-left: 2em;"><b>fields</b> = <code style="text-indent: 0em;">list, str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Layer field used to configure the label. If 'fields' is configured, 'label' will be disabled.</p>
<p style="margin-left: 4em;">Default(None) no labels.</p>
<p style="margin-left: 2em;"><b>connector</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default ''</span>. </p>
<p style="margin-left: 4em;">If 'fields' configures more than one field, the fields are connected with this symbol.</p>
<p style="margin-left: 2em;"><b>title</b> = <code style="text-indent: 0em;">str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Legend Name. Default(None) vector's name.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.legend.Legend.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib.legend.Legend</code>. </p>

### add_labels<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(labels = None, fields = None, connector = "", selects = 0, family = None, color = None, weight = None, size = None)</span>

<p>Add label of the vector to the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>labels</b> = <code style="text-indent: 0em;">str, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Manually set the labels. The number should be the same as the number of plotted items.</p>
<p style="margin-left: 4em;">Otherwise, the shortfall will be assigned as null. Default(None) no labels.</p>
<p style="margin-left: 2em;"><b>fields</b> = <code style="text-indent: 0em;">list, str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Field used to configure the label. If 'fields' is configured, 'labels' will be disabled.</p>
<p style="margin-left: 4em;">Default(None) no labels.</p>
<p style="margin-left: 2em;"><b>connector</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default ''</span>. </p>
<p style="margin-left: 4em;">If 'FieldName' configures more than one field, the fields are connected with this symbol.</p>
<p style="margin-left: 2em;"><b>selects</b> = <code style="text-indent: 0em;">list or int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">If there are multiple geometries in an feature. Then label in these geometry.(Sorted by</p>
<p style="margin-left: 4em;">area in descending order.)</p>
<p style="margin-left: 2em;"><b>family</b> = <code style="text-indent: 0em;">str, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The font of the label. If it is a list, assign a different font to each label.</p>
<p style="margin-left: 4em;">Default(None) matplotlib.pyplot.rcParams['font.family']</p>
<p style="margin-left: 2em;"><b>color</b> = <code style="text-indent: 0em;">str, list, tuple or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The label color. If it is a list, assign a different color to each label. If None,</p>
<p style="margin-left: 4em;">a random color will be generated. Default(None) matplotlib.pyplot.rcParams['text.color']</p>
<p style="margin-left: 2em;"><b>weight</b> = <code style="text-indent: 0em;">str, list, tuple or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">A numeric value in the range 0-1000 or one of 'ultralight', 'light', 'normal', 'regular',</p>
<p style="margin-left: 4em;">'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy',</p>
<p style="margin-left: 4em;">'extra bold', 'black'. Default(None) matplotlib.pyplot.rcParams['font.weight']</p>
<p style="margin-left: 2em;"><b>size</b> = <code style="text-indent: 0em;">float or list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The font size of the label. If it is a list, assign a different font size to each label.</p>
<p style="margin-left: 4em;">Default(None) matplotlib.pyplot.rcParams['font.size']</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.text.Text.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">list of matplotlib.text.Text</code>. </p>
