---
title: extract_values
date: 2026-08-15
sidebar: true
---
# gma.smc.extraction.extract_values


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">extract_values</span><span style="font-style: italic; color: black;font-size: 130%;">(points, in_ds):</span></span>

Extracting data from raster dataset based on point coordinates.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>points: </b> <code style="text-indent: 0">list||tuple||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The X (longitude), Y (latitude) coordinates of the point to be transformed.</p><p style="padding-left: 1em;text-indent: 1em;">For example: Points = [(130.1, 45.2), (131.5, 40.2)]</p><p style="text-indent: 1em;"><b>in_ds: </b> <code style="text-indent: 0">Dataset</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A gma raster dataset.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">DataFrame</code>.</p>

---