---
title: ToOtherFormat
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**ToOtherFormat**(*InFile, OutFile, OutFormat = 'GTiff'*)

---

**功能：**【格式转换】。一种栅格格式转换为另一种栅格格式。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str||class`。输出栅格文件格式，默认为 GTiff。

::: tip 其他支持格式

AAIGrid, ADRG, ARG, BAG, BLX, BMP, BT, BYN, CALS, CEOS, COG, CTable2, DDS, DTED, EHdr, ELAS, ENVI, ERS, EXR, FIT, FITS, GIF, GPKG, GS7BG, GSBG, GTiff, HDF4Image, HF2, HFA, ILWIS, ISCE, ISIS2, ISIS3, JP2OpenJPEG, JPEG, KMLSuperoverlay, KRO, LCP, Leveller, MBTiles, MEM, MFF, MFF2, MRF, NITF, NTv2, NWT_GRD, PAux, netCDF, PCIDSK, PCRaster, PDF, PDS4, PNG, PNM, PostGISRaster, R, RMF, ROI_PAC, RRASTER, RST, Rasterlite, SAGA, SGI, SIGDEM, SQLite, Terragen, USGSDEM, VICAR, VRT, WEBP, WMS, XPM, XYZ, ZMAP, Zarr

:::

::: tip 高级格式配置

OutFormat 可以为一个 gma.gft.RasterFormat 类，用以实现例如压缩格式，分块大小等高级参数配置。详见 **地理驱动-gft**。

:::

---

**示例：**

*netCDF(.nc) 转 GTiff(.tif)（下载 [示例数据](/rasp/HRCLDAS_Test.nc)）*
```python
from gma import rasp

InFile = 'HRCLDAS_Test.nc'
OutFile = 'HRCLDAS_Test.tif'

rasp.Basic.ToOtherFormat(InFile, OutFile, OutFormat = 'GTiff')
```