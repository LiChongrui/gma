<template><div><p>All items(functions/classes/consts) in this module are as follows:</p>
<table>
<thead>
<tr>
<th>No.</th>
<th>item</th>
<th>type</th>
<th>introduce</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><RouteLink to="/docs/UserGuide/math/correction/gamma.html">math.correction.gamma</RouteLink></td>
<td>function</td>
<td>Gamma transform. Reference equation: Out = constant * ((data - vvmin) / vptp) ** gamma_v) * vptp.</td>
</tr>
<tr>
<td>2</td>
<td><RouteLink to="/docs/UserGuide/math/correction/log.html">math.correction.log</RouteLink></td>
<td>function</td>
<td>Logarithmic transformation. Reference equation: Out = log2(1 + (data - vmin) / vptp) * vptp * constant.</td>
</tr>
<tr>
<td>3</td>
<td><RouteLink to="/docs/UserGuide/math/correction/sigmoid.html">math.correction.sigmoid</RouteLink></td>
<td>function</td>
<td>S-shaped curve function transformation. Reference equation: Out = 1 / (1 + exp(constant * (cutoff - (data - vmin) / vptp))) * vptp.</td>
</tr>
<tr>
<td>4</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/D.html">math.evaluation.D</RouteLink></td>
<td>function</td>
<td>D index.</td>
</tr>
<tr>
<td>5</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/MAE.html">math.evaluation.MAE</RouteLink></td>
<td>function</td>
<td>Maximum absolute error.</td>
</tr>
<tr>
<td>6</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/NRMSE.html">math.evaluation.NRMSE</RouteLink></td>
<td>function</td>
<td>NRMSE.</td>
</tr>
<tr>
<td>7</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/R2.html">math.evaluation.R2</RouteLink></td>
<td>function</td>
<td>Coefficient of determination.</td>
</tr>
<tr>
<td>8</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/RMSE.html">math.evaluation.RMSE</RouteLink></td>
<td>function</td>
<td>RMSE.</td>
</tr>
<tr>
<td>9</td>
<td><RouteLink to="/docs/UserGuide/math/evaluation/corrcoef.html">math.evaluation.corrcoef</RouteLink></td>
<td>function</td>
<td>Correlation coefficient and significance.</td>
</tr>
<tr>
<td>10</td>
<td><RouteLink to="/docs/UserGuide/math/kernel/aggregate.html">math.kernel.aggregate</RouteLink></td>
<td>function</td>
<td>Aggregate array.</td>
</tr>
<tr>
<td>11</td>
<td><RouteLink to="/docs/UserGuide/math/prepro/fill_nodata.html">math.prepro.fill_nodata</RouteLink></td>
<td>function</td>
<td>Interpolate missing or abnormal values.</td>
</tr>
<tr>
<td>12</td>
<td><RouteLink to="/docs/UserGuide/math/prepro/to_numeric_array.html">math.prepro.to_numeric_array</RouteLink></td>
<td>function</td>
<td>Forces the input data to be converted to a numeric array, values that cannot be converted will be modified to nan.</td>
</tr>
<tr>
<td>13</td>
<td><RouteLink to="/docs/UserGuide/math/smooth/moving_average.html">math.smooth.moving_average</RouteLink></td>
<td>function</td>
<td>Data smoothing based on moving average method.</td>
</tr>
<tr>
<td>14</td>
<td><RouteLink to="/docs/UserGuide/math/smooth/savitzky_golay.html">math.smooth.savitzky_golay</RouteLink></td>
<td>function</td>
<td>Data smoothing based on Savitzky-Golay method.</td>
</tr>
<tr>
<td>15</td>
<td><RouteLink to="/docs/UserGuide/math/stretch/hist_equalize.html">math.stretch.hist_equalize</RouteLink></td>
<td>function</td>
<td>Apply non-linear contrast stretching, where the values are distributed within the bit depth range.</td>
</tr>
<tr>
<td>16</td>
<td><RouteLink to="/docs/UserGuide/math/stretch/max_min.html">math.stretch.max_min</RouteLink></td>
<td>function</td>
<td>Use linear stretching with the minimum and maximum output pixel values as the endpoints of the histogram.</td>
</tr>
<tr>
<td>17</td>
<td><RouteLink to="/docs/UserGuide/math/stretch/percentage.html">math.stretch.percentage</RouteLink></td>
<td>function</td>
<td>Truncates the array based on the percentage interval entered. Then stretch it to the specified range.</td>
</tr>
<tr>
<td>18</td>
<td><RouteLink to="/docs/UserGuide/math/stretch/std.html">math.stretch.std</RouteLink></td>
<td>function</td>
<td>Standard deviation stretch. This method is used to emphasize how much feature values vary from the mean value; it is best when used on normally distributed data.</td>
</tr>
</tbody>
</table>
</div></template>


