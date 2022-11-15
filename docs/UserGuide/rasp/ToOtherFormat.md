---
title: ToOtherFormat
date: 2021-10-30
sidebar: false
---

## gma.rasp.**ToOtherFormat**(*InFile, OutFile, OutFormat = 'GTiff'*)

---

**功能：**【格式转换】。一种栅格格式转换为另一种栅格格式。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式，默认为 GTiff。

::: tip 其他支持格式

AAIGrid, ADRG, ARG, BAG, BLX, BMP, BT, BYN, CALS, CEOS, COG, CTable2, DDS, DTED, EHdr, ELAS, ENVI, ERS, EXR, FIT, FITS, GIF, GPKG, GS7BG, GSBG, GTiff, HDF4Image, HF2, HFA, ILWIS, ISCE, ISIS2, ISIS3, JP2OpenJPEG, JPEG, KMLSuperoverlay, KRO, LCP, Leveller, MBTiles, MEM, MFF, MFF2, MRF, NITF, NTv2, NWT_GRD, PAux, netCDF, PCIDSK, PCRaster, PDF, PDS4, PNG, PNM, PostGISRaster, R, RMF, ROI_PAC, RRASTER, RST, Rasterlite, SAGA, SGI, SIGDEM, SQLite, Terragen, USGSDEM, VICAR, VRT, WEBP, WMS, XPM, XYZ, ZMAP, Zarr

:::

::: warning 注意

含有**多个子数据**的 netCDF, HDF4Image 等格式转出请使用 MultiSDSToTif 函数。

:::

---

**示例：**

*netCDF(.nc) 转 GTiff(.tif)（下载 [示例数据](/rasp/HRCLDAS_Test.nc)）*
```python
import gma

InFile = 'HRCLDAS_Test.nc'
OutFile = 'HRCLDAS_Test.tif'
gma.rasp.ToOtherFormat(InFile, OutFile, OutFormat = 'GTiff')

# 查看输出文件驱动
print(gma.Open(OutFile).Driver)
```
> \>>> GTiff