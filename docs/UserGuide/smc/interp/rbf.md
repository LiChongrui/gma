---
title: rbf
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.interp.rbf</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">rbf</span><span style="font-style: italic; color: black;font-size: 120%;">(points, values, bounds = <span style="color:#48566B">None</span>, resolution = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, kernel = <span style="color:#48566B">"thin_plate_spline"</span>, search_radius = <span style="color:#48566B">12</span>, **kwargs):</span></span>

<p>Use Radial Basis Function method to interpolate points into a 2D array.</p>
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
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem.</p>
<p style="margin-left: 2em;"><b>kernel </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'thin_plate_spline'</span>. </p>
<p style="margin-left: 4em;">Type of RBF. This should be one of:</p>
<p style="margin-left: 6em;">'linear'               : -r.</p>
<p style="margin-left: 6em;">'thin_plate_spline'    : r**2 * log(r).</p>
<p style="margin-left: 6em;">'cubic'                : r**3.</p>
<p style="margin-left: 6em;">'quintic'              : -r**5.</p>
<p style="margin-left: 6em;">'multiquadric'         : -sqrt(1 + r**2).</p>
<p style="margin-left: 6em;">'inverse_multiquadric' : 1/sqrt(1 + r**2).</p>
<p style="margin-left: 6em;">'inverse_quadratic'    : 1/(1 + r**2).</p>
<p style="margin-left: 6em;">'gaussian'             : exp(-r**2).</p>
<p style="margin-left: 2em;"><b>search_radius </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 12</span>. </p>
<p style="margin-left: 4em;">The value of the interpolant at each evaluation point will be computed using only this many nearest data points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">Contains data (data) and affine transformation (geo_transform).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">[1] Fasshauer, G., 2007. Meshfree Approximation Methods with Matlab. World Scientific Publishing Co.</p>
<p style="text-indent: 2em;">[2] http://amadeus.math.iit.edu/~fass/603_ch3.pdf</p>
<p style="text-indent: 2em;">[3] Wahba, G., 1990. Spline Models for Observational Data. SIAM.</p>
<p style="text-indent: 2em;">[4] http://pages.stat.wisc.edu/~wahba/stat860public/lect/lect8/lect8.pdf</p>
