---
title: Install
date: 2026-08-14 
---

## Required

 + System: <Badge text="Windows 10+" vertical='middle'/> 64-bit (amd64),<Badge text="8 GB+" vertical='middle'/> RAM.

::: warning Note
**gma** is currently <u>*not supported MacOS, Linux or other platforms*</u>.
:::

 + Python Version: <Badge text="3.12 ~ 3.14" vertical='middle'/>

 + Third-party library: [NumPy<Badge text="2.4.0+"/>](https://numpy.org/), [Pandas<Badge text="3.0.4+"/>](https://pandas.pydata.org/), [SciPy<Badge text="1.18.0+ "/>](https://scipy.org/), [Matplotlib<Badge text="3.10.0+"/>](https://matplotlib.org/).

::: info

[GDAL<Badge text="3.12.4"/>](https://gdal.org/en/stable/) is built into GMA by default, so no additional installation is required.
:::

## Installation

```bash
pip install gma
```

::: tip 
PyPi Project: [https://pypi.org/project/gma/](https://pypi.org/project/gma/)
:::

## Verifying

```python
## Import version info
from gma import __version__

## Import selected modules
from gma import climet, crs, driver, gio, math, rsvi, smc, etools, env, const

## Spatial plotting and built-in data
from gma.carto import plot, inres
```
