---
title: b_spline
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.interp.b_spline</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">b_spline</span><span style="font-style: italic; color: black;font-size: 120%;">(points, values, bounds = <span style="color:#48566B">None</span>, resolution = <span style="color:#48566B">None</span>, weights = <span style="color:#48566B">0.1</span>, crs = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Use B-Spline method to interpolate points into a 2D array.</p>
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
<p style="margin-left: 2em;"><b>weights </b> = <code style="text-indent: 0em;">float||list</code>. </p>
<p style="margin-left: 4em;">Rank-1 array of weights.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">Contains data (data) and affine transformation (geo_transform).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">[1] Dierckx P. An algorithm for surface fitting with spline functions Ima J. Numer. Anal. 1 (1981) 267-283.</p>
<p style="text-indent: 2em;">[2] Dierckx P. An algorithm for surface fitting with spline functions report tw50, Dept. Computer Science,K.U.Leuven, 1980.</p>
<p style="text-indent: 2em;">[3] Dierckx P. Curve and surface fitting with splines, Monographs on Numerical Analysis, Oxford University Press, 1993.</p>
