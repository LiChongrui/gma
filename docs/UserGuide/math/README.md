---
title: Contents
date: 2026-08-14
sidebar: false
---
All items(functions/classes/consts) in this module are as follows:
|No.|item|type|introduce|
|---|---|---|---|
|1|[math.correction.gamma](/UserGuide/math/correction/gamma.html)|function|Gamma transform.Reference equation: Out = constant * ((data - vvmin) / vptp) ** gamma_v) * vptp.|
|2|[math.correction.log](/UserGuide/math/correction/log.html)|function|Logarithmic transformation.Reference equation: Out = log2(1 + (data - vmin) / vptp) * vptp * constant.|
|3|[math.correction.sigmoid](/UserGuide/math/correction/sigmoid.html)|function|S-shaped curve function transformation.Reference equation: Out = 1 / (1 + exp(constant * (cutoff - (data - vmin) / vptp))) * vptp.|
|4|[math.evaluation.MAE](/UserGuide/math/evaluation/MAE.html)|function|Maximum Absolute Error.|
|5|[math.evaluation.NRMSE](/UserGuide/math/evaluation/NRMSE.html)|function|Normalized Root Mean Square Error.|
|6|[math.evaluation.R2](/UserGuide/math/evaluation/R2.html)|function|Coefficient of determination.|
|7|[math.evaluation.RMSE](/UserGuide/math/evaluation/RMSE.html)|function|Root Mean Square Error.|
|8|[math.evaluation.corrcoef](/UserGuide/math/evaluation/corrcoef.html)|function|Correlation coefficient and significance.|
|9|[math.kernel.aggregate](/UserGuide/math/kernel/aggregate.html)|function|Aggregate array.|
|10|[math.prepro.fill_nodata](/UserGuide/math/prepro/fill_nodata.html)|function|Interpolate missing or abnormal values.|
|11|[math.prepro.to_numeric_array](/UserGuide/math/prepro/to_numeric_array.html)|function|Forces the input data to be converted to a numeric array, values that cannotbe converted will be modified to nan.|
|12|[math.smooth.moving_average](/UserGuide/math/smooth/moving_average.html)|function|Data smoothing based on moving average method.|
|13|[math.smooth.savitzky_golay](/UserGuide/math/smooth/savitzky_golay.html)|function|Data smoothing based on Savitzky-Golay method.|
|14|[math.stretch.hist_equalize](/UserGuide/math/stretch/hist_equalize.html)|function|Apply non-linear contrast stretching, where the values are distributed within the bit depth range.|
|15|[math.stretch.max_min](/UserGuide/math/stretch/max_min.html)|function|Use linear stretching with the minimum and maximum output pixel values as the endpoints of the histogram.|
|16|[math.stretch.percentage](/UserGuide/math/stretch/percentage.html)|function|Truncates the array based on the percentage interval entered.Then stretch it to the specified range.|
|17|[math.stretch.std](/UserGuide/math/stretch/std.html)|function|Standard deviation stretch. This method is used to emphasize how much feature values vary from the mean value;it is best when used on normally distributed data.|
