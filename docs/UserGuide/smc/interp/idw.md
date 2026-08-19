---
title: idw
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.interp.idw</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">idw</span><span style="font-style: italic; color: black;font-size: 120%;">(points, values, bounds = <span style="color:#48566B">None</span>, resolution = <span style="color:#48566B">None</span>, power = <span style="color:#48566B">2.0</span>, search_radius = <span style="color:#48566B">12</span>, crs = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Use IDW method to interpolate points into a 2D array.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>points</b>: <code style="text-indent: 0em;">list||tuple||array</code>. </p>
<p style="margin-left: 4em;">Interpolate point X (longitude), Y (latitude) coordinates. There must be at least 4 coordinate points.</p>
<p style="margin-left: 2em;"><b>values</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">The data value corresponding to the coordinate point, which is the same as the number of points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>bounds </b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The four boundaries of the interpolation result are the minimum longitude (left), the minimum latitude (bottom), the maximum longitude (right), and the maximum latitude (top). The default (None) is to extract the range from the input coordinate points.</p>
<p style="margin-left: 2em;"><b>resolution </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The resolution of the interpolation result. The default (None) is 1/10 of the minimum bounds X and Y difference.</p>
<p style="margin-left: 2em;"><b>power </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 2.0</span>. </p>
<p style="margin-left: 4em;">Distance exponent (power). Used to control the saliency of points around the interpolation.</p>
<p style="margin-left: 2em;"><b>search_radius </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 12</span>. </p>
<p style="margin-left: 4em;">Specifies the number of nearest input sample points to use to perform interpolation.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">Contains data (data) and affine transformation (geo_transform).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">[1] Philip, G. M., and D. F. Watson. A Precise Method for Determining Contoured Surfaces. Australian Petroleum Exploration Association Journal 22: 205-212. 1982.</p>
<p style="text-indent: 2em;">[2] Watson, D. F., and G. M. Philip. A Refinement of Inverse Distance Weighted Interpolation. Geoprocessing 2:315-327. 1985.</p>
