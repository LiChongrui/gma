---
title: Ellips
date: 2026-11-20
---

<p style="font-size: 120%;font-weight: bold;">gma.crs.Ellips</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Ellips</span></span>

<p>Default ellipsoids. Built from the PROJ database when created.</p>
<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>

```python
from gma import crs
crs.Ellips.WGS_84
```

<p>crs.Ellips.WGS_84 --> <code style="text-indent: 0em;">{'semi_major': 6378137.0, 'inv_flattening': 298.257223563}</code></p>

## Constants

| Constant | Semi-major axis (m) | Inverse flattening |
| --- | --- | --- |
| `AIRY_1830` | 6377563.396 | 299.3249646 |
| `BESSEL_1841` | 6377397.155 | 299.1528128 |
| `BESSEL_MODIFIED` | 6377492.018 | 299.1528128 |
| `BESSEL_NAMIBIA` | 6377483.865 | 299.1528128 |
| `CGCS2000` | 6378137.0 | 298.257222101 |
| `DANISH_1876` | 6377019.27 | 300.0 |
| `FISCHER_1960` | 6378166.0 | 298.3 |
| `FISCHER_1968` | 6378150.0 | 298.3 |
| `FISCHER_MODIFIED` | 6378155.0 | 298.3 |
| `GEM_10C` | 6378137.0 | 298.257223563 |
| `GRS_1967` | 6378160.0 | 298.247167427 |
| `GRS_1980` | 6378137.0 | 298.257222101 |
| `GSK2011` | 6378136.5 | 298.2564151 |
| `HELMERT_1906` | 6378200.0 | 298.3 |
| `HOUGH_1960` | 6378270.0 | 297.0 |
| `IAG_1975` | 6378140.0 | 298.257 |
| `INTERNATIONAL_1924` | 6378388.0 | 297.0 |
| `INTERNATIONAL_1967` | 6378160.0 | 298.25 |
| `KAULA_1961` | 6378163.0 | 298.24 |
| `KRASSOWSKY_1940` | 6378245.0 | 298.3 |
| `LERCH_1979` | 6378139.0 | 298.257 |
| `MAUPERTIUS_1738` | 6397300.0 | 191.0 |
| `MERIT_1983` | 6378137.0 | 298.257 |
| `NWL_10D` | 6378135.0 | 298.26 |
| `NWL_9D` | 6378145.0 | 298.25 |
| `OSU86F` | 6378136.2 | 298.257223563 |
| `OSU91A` | 6378136.3 | 298.257223563 |
| `PLESSIS_1817` | 6376523.0 | 308.64 |
| `PZ90` | 6378136.0 | 298.257839303 |
| `STRUVE_1860` | 6378298.3 | 294.73 |
| `WALBECK` | 6376896.0 | 302.78 |
| `WAR_OFFICE` | 6378300.0 | 296.0 |
| `WGS_1966` | 6378145.0 | 298.25 |
| `WGS_60` | 6378165.0 | 298.3 |
| `WGS_72` | 6378135.0 | 298.26 |
| `WGS_84` | 6378137.0 | 298.257223563 |
| `ZACH_1812` | 6376045.0 | 310.0 |
