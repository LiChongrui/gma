---
title: inres
date: 2026-11-20
---

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">inres</span></span>

<p>The mapping elements resource module. Provides built-in cartographic elements: compass (Composs), scale bar (ScaleBar), marker paths (MarkerPath), and default world layers and datasets (WorldLayer, WorldDataset).</p>

### Composs

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres.Composs</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Composs</span></span>

<p>Built-in compass elements.</p>

| Element | Description |
| --- | --- |
| <code style="text-indent: 0em;">Normal1</code> | Built-in compass style 1. |
| <code style="text-indent: 0em;">Normal2</code> | Built-in compass style 2. |
| <code style="text-indent: 0em;">Normal3</code> | Built-in compass style 3. |

### ScaleBar

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres.ScaleBar</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">ScaleBar</span></span>

<p>Built-in scale bar elements.</p>

| Element | Description |
| --- | --- |
| <code style="text-indent: 0em;">Normal1</code> | Built-in scale bar style 1. |

### MarkerPath

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres.MarkerPath</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">MarkerPath</span><span style="font-style: italic; color: black;font-size: 130%;">():</span></span>

<p>Create custom marker shapes (SVG path markers).</p>
<p>Built-in shapes include: <b>Flower</b>, <b>Spiral</b>, <b>Heart</b>, <b>Gear</b>, <b>Infinity</b>.</p>

### WorldLayer

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres.WorldLayer</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WorldLayer</span><span style="font-style: italic; color: black;font-size: 130%;">():</span></span>

<p>Open the world Layer provided by gma.</p>

| Element | Description |
| --- | --- |
| <code style="text-indent: 0em;">Country</code> | Get gma default world country Layer. |
| <code style="text-indent: 0em;">Land</code> | Get gma default world land Layer. |
| <code style="text-indent: 0em;">Ocean</code> | Get gma default world ocean Layer. |
| <code style="text-indent: 0em;">River</code> | Get gma default world river Layer. |
| <code style="text-indent: 0em;">Lake</code> | Get gma default world lake Layer. |

### WorldDataset

<p style="font-size: 120%;font-weight: bold;">gma.carto.inres.WorldDataset</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WorldDataset</span><span style="font-style: italic; color: black;font-size: 130%;">():</span></span>

<p>Open the world Dataset provided by gma.</p>

| Element | Description |
| --- | --- |
| <code style="text-indent: 0em;">DEM</code> | Get gma default world DEM Dataset. |
| <code style="text-indent: 0em;">NaturalEarth</code> | Get gma default world natural earth (Cross-blended Hypsometric Tints) Dataset. |
