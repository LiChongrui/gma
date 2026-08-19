---
title: kriging
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.interp.kriging</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">kriging</span><span style="font-style: italic; color: black;font-size: 120%;">(points, values, bounds = <span style="color:#48566B">None</span>, resolution = <span style="color:#48566B">None</span>, search_radius = <span style="color:#48566B">12</span>, crs = <span style="color:#48566B">None</span>, variogram_model = <span style="color:#48566B">"Linear"</span>, variogram_parameters = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"Ordinary"</span>, **kwargs):</span></span>

<p>Use Ordinary Kriging or Universal Kriging method to interpolate points into a 2D array.</p>
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
<p style="margin-left: 2em;"><b>search_radius </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 12</span>. </p>
<p style="margin-left: 4em;">Specifies the number of nearest input sample points to use to perform interpolation.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem.</p>
<p style="margin-left: 2em;"><b>variogram_model </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Linear'</span>. </p>
<p style="margin-left: 4em;">Semivariogram model.</p>
<p style="margin-left: 2em;"><b>variogram_parameters </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Semivariate model parameters. By default, the least squares method is used to automatically calculate the variogram model parameters (None).</p>
<p style="margin-left: 4em;">Supported models and configurable parameters include:</p>
<p style="margin-left: 6em;">'Linear': 'Slope', 'Nugget' 'power': 'Scale', 'Exponent', 'Nugget' 'Gaussian': 'PSill', 'Range', 'Nugget' 'Spherical': 'PSill', 'Range', 'Nugget' 'Exponential': 'PSill', 'Range', 'Nugget' 'HoleEffect': 'PSill', 'Range', 'Nugget'</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Ordinary'</span>. </p>
<p style="margin-left: 4em;">Kriging method. Include 'Ordinary' or 'Universal'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Other parameters(Effective when variogram_parameters = None):</p>
<p style="margin-left: 2em;"><b>n_lags </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 6</span>. </p>
<p style="margin-left: 4em;">The mean number of bins for the semivariogram.</p>
<p style="margin-left: 2em;"><b>weight </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Specifies whether the semivariance for smaller lags should be weighted.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">namedtuple</code>. </p>
<p style="margin-left: 4em;">Contains data (data),  variance at specified grid points or at the specified set of points (sigma_sq) and affine transformation (geo_transform).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">References:</p>
<p style="text-indent: 2em;">[1] P.K. Kitanidis, Introduction to Geostatistcs: Applications in Hydrogeology, Cambridge University Press, 1997(p272).</p>
<p style="text-indent: 2em;">[2] N. Cressie, Statistics for spatial data, Wiley Series in Probability and Statistics, 1993(p137).</p>
