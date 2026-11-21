---
title: AngleUnits
date: 2026-11-20
---

<p style="font-size: 120%;font-weight: bold;">gma.crs.AngleUnits</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AngleUnits</span></span>

<p>Angle units object. Conversion factors relative to the radian.</p>
<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>

```python
from gma import crs
crs.AngleUnits.DEGREE
```

<p>crs.AngleUnits.DEGREE --> <code style="text-indent: 0em;">0.017453292519943278</code></p>

## Constants

| Constant | Value (to radian) |
| --- | --- |
| `ARC_MINUTE` | 0.0002908882086657213 |
| `ARC_SECOND` | 4.848136811095355e-06 |
| `CENTESIMAL_MINUTE` | 0.0001570796326794895 |
| `CENTESIMAL_SECOND` | 1.570796326794895e-06 |
| `DEGREE` | 0.017453292519943278 |
| `GON` | 0.01570796326794895 |
| `GRAD` | 0.01570796326794895 |
| `MICRORADIAN` | 1e-06 |
| `MILLIARC_SECOND` | 4.848136811095355e-09 |
| `MIL_6400` | 0.0009817477042468094 |
| `RADIAN` | 1.0 |
