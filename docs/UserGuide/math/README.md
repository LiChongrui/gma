---
title: Contents
date: 2026-08-15
---
All items(functions/classes/consts) in this module are as follows:
|No.|item|type|introduce|
|---|---|---|---|
|1|[math.correction.gamma](/docs/UserGuide/math/correction/gamma.html)|function|Gamma transform. Reference equation: Out = constant * ((data - vvmin) / vptp) ** gamma_v) * vptp.|
|2|[math.correction.log](/docs/UserGuide/math/correction/log.html)|function|Logarithmic transformation. Reference equation: Out = log2(1 + (data - vmin) / vptp) * vptp * constant.|
|3|[math.correction.sigmoid](/docs/UserGuide/math/correction/sigmoid.html)|function|S-shaped curve function transformation. Reference equation: Out = 1 / (1 + exp(constant * (cutoff - (data - vmin) / vptp))) * vptp.|
|4|[math.evaluation.D](/docs/UserGuide/math/evaluation/D.html)|function|D index.|
|5|[math.evaluation.MAE](/docs/UserGuide/math/evaluation/MAE.html)|function|Maximum absolute error.|
|6|[math.evaluation.NRMSE](/docs/UserGuide/math/evaluation/NRMSE.html)|function|NRMSE.|
|7|[math.evaluation.R2](/docs/UserGuide/math/evaluation/R2.html)|function|Coefficient of determination.|
|8|[math.evaluation.RMSE](/docs/UserGuide/math/evaluation/RMSE.html)|function|RMSE.|
|9|[math.evaluation.corrcoef](/docs/UserGuide/math/evaluation/corrcoef.html)|function|Correlation coefficient and significance.|
|10|[math.kernel.aggregate](/docs/UserGuide/math/kernel/aggregate.html)|function|Aggregate array.|
|11|[math.prepro.fill_nodata](/docs/UserGuide/math/prepro/fill_nodata.html)|function|Interpolate missing or abnormal values.|
|12|[math.prepro.to_numeric_array](/docs/UserGuide/math/prepro/to_numeric_array.html)|function|Forces the input data to be converted to a numeric array, values that cannot be converted will be modified to nan.|
|13|[math.smooth.moving_average](/docs/UserGuide/math/smooth/moving_average.html)|function|Data smoothing based on moving average method.|
|14|[math.smooth.savitzky_golay](/docs/UserGuide/math/smooth/savitzky_golay.html)|function|Data smoothing based on Savitzky-Golay method.|
|15|[math.stretch.hist_equalize](/docs/UserGuide/math/stretch/hist_equalize.html)|function|Apply non-linear contrast stretching, where the values are distributed within the bit depth range.|
|16|[math.stretch.max_min](/docs/UserGuide/math/stretch/max_min.html)|function|Use linear stretching with the minimum and maximum output pixel values as the endpoints of the histogram.|
|17|[math.stretch.percentage](/docs/UserGuide/math/stretch/percentage.html)|function|Truncates the array based on the percentage interval entered. Then stretch it to the specified range.|
|18|[math.stretch.std](/docs/UserGuide/math/stretch/std.html)|function|Standard deviation stretch. This method is used to emphasize how much feature values vary from the mean value; it is best when used on normally distributed data.|
