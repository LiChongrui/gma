---
title: GetRACreationOption
date: 2022-04-17
sidebar: false
---

## gma.config.**GetRACreationOption**(*Format*)

---

**功能：**【栅格创建选项】。获取栅格驱动格式支持的高级创建选项！

**参数：** 

&emsp;Format：`str`。栅格驱动格式名称。

**返回：**`DataFrame`。

---

**示例：**
```python
import gma

# 获取 gma 创建 GTiff 文件时的高级参数及配置信息
gma.config.GetRACreationOption('GTiff')
```

|    | name                           | type          | description                                                                                                              | default     | Value                                                                                                  |
|---:|:-------------------------------|:--------------|:-------------------------------------------------------------------------------------------------------------------------|:------------|:-------------------------------------------------------------------------------------------------------|
|  0 | COMPRESS                       | string-select |                                                                                                                       | DEFLATE     | NONE LZW PACKBITS JPEG CCITTRLE CCITTFAX3 CCITTFAX4 DEFLATE LZMA ZSTD WEBP LERC LERC_DEFLATE LERC_ZSTD |
|  1 | PREDICTOR                      | int           | Predictor Type (1=default, 2=horizontal differencing, 3=floating point prediction)                                       | 2           |                                                                                                     |
|  2 | DISCARD_LSB                    | string        | Number of least-significant bits to set to clear as a single value or comma-separated list of values for per-band values |          |                                                                                                     |
|  3 | JPEG_QUALITY                   | int           | JPEG quality 1-100                                                                                                       | 75          |                                                                                                     |
|  4 | JPEGTABLESMODE                 | int           | Content of JPEGTABLES tag. 0=no JPEGTABLES tag, 1=Quantization tables only, 2=Huffman tables only, 3=Both                | 1           |                                                                                                     |
|  5 | ZLEVEL                         | int           | DEFLATE compression level 1-12                                                                                           | 12          |                                                                                                     |
|  6 | LZMA_PRESET                    | int           | LZMA compression level 0(fast)-9(slow)                                                                                   | 6           |                                                                                                     |
|  7 | ZSTD_LEVEL                     | int           | ZSTD compression level 1(fast)-22(slow)                                                                                  | 9           |                                                                                                     |
|  8 | MAX_Z_ERROR                    | float         | Maximum error for LERC compression                                                                                       |          |                                                                                                     |
|  9 | WEBP_LEVEL                     | int           | WEBP quality level. Low values result in higher compression ratios                                                       |          |                                                                                                     |
| 10 | NUM_THREADS                    | string        | Number of worker threads for compression. Can be set to ALL_CPUS                                                         | ALL_CPUS    |                                                                                                     |
| 11 | NBITS                          | int           | BITS for sub-byte files (1-7), sub-uint16_t (9-15), sub-uint32_t (17-31), or float32 (16)                                |          |                                                                                                     |
| 12 | INTERLEAVE                     | string-select |                                                                                                                       | PIXEL       | BAND PIXEL                                                                                             |
| 13 | TILED                          | boolean       | Switch to tiled format                                                                                                   | Yes         |                                                                                                     |
| 14 | TFW                            | boolean       | Write out world file                                                                                                     |          |                                                                                                     |
| 15 | RPB                            | boolean       | Write out .RPB (RPC) file                                                                                                |          |                                                                                                     |
| 16 | RPCTXT                         | boolean       | Write out _RPC.TXT file                                                                                                  |          |                                                                                                     |
| 17 | BLOCKXSIZE                     | int           | Tile Width                                                                                                               |          |                                                                                                     |
| 18 | BLOCKYSIZE                     | int           | Tile/Strip Height                                                                                                        |          |                                                                                                     |
| 19 | PHOTOMETRIC                    | string-select |                                                                                                                       |          | MINISBLACK MINISWHITE PALETTE RGB CMYK YCBCR CIELAB ICCLAB ITULAB                                      |
| 20 | SPARSE_OK                      | boolean       | Should empty blocks be omitted on disk?                                                                                  | FALSE       |                                                                                                     |
| 21 | ALPHA                          | string-select | Mark first extrasample as being alpha                                                                                    |          | NO                                                                                                     |
| 22 | PROFILE                        | string-select |                                                                                                                       | GDALGeoTIFF | GDALGeoTIFF GeoTIFF BASELINE                                                                           |
| 23 | PIXELTYPE                      | string-select |                                                                                                                       |          | DEFAULT SIGNEDBYTE                                                                                     |
| 24 | BIGTIFF                        | string-select | Force creation of BigTIFF file                                                                                           | IF_SAFER    | YES NO IF_NEEDED IF_SAFER                                                                              |
| 25 | ENDIANNESS                     | string-select | Force endianness of created file. For DEBUG purpose mostly                                                               | NATIVE      | NATIVE INVERTED LITTLE BIG                                                                             |
| 26 | COPY_SRC_OVERVIEWS             | boolean       | Force copy of overviews of source dataset (CreateCopy())                                                                 |          |                                                                                                     |
| 27 | SOURCE_ICC_PROFILE             | string        | ICC profile                                                                                                              |          |                                                                                                     |
| 28 | SOURCE_PRIMARIES_RED           | string        | x,y,1.0 (xyY) red chromaticity                                                                                           |          |                                                                                                     |
| 29 | SOURCE_PRIMARIES_GREEN         | string        | x,y,1.0 (xyY) green chromaticity                                                                                         |          |                                                                                                     |
| 30 | SOURCE_PRIMARIES_BLUE          | string        | x,y,1.0 (xyY) blue chromaticity                                                                                          |          |                                                                                                     |
| 31 | SOURCE_WHITEPOINT              | string        | x,y,1.0 (xyY) whitepoint                                                                                                 |          |                                                                                                     |
| 32 | TIFFTAG_TRANSFERFUNCTION_RED   | string        | Transfer function for red                                                                                                |          |                                                                                                     |
| 33 | TIFFTAG_TRANSFERFUNCTION_GREEN | string        | Transfer function for green                                                                                              |          |                                                                                                     |
| 34 | TIFFTAG_TRANSFERFUNCTION_BLUE  | string        | Transfer function for blue                                                                                               |          |                                                                                                     |
| 35 | TIFFTAG_TRANSFERRANGE_BLACK    | string        | Transfer range for black                                                                                                 |          |                                                                                                     |
| 36 | TIFFTAG_TRANSFERRANGE_WHITE    | string        | Transfer range for white                                                                                                 |          |                                                                                                     |
| 37 | STREAMABLE_OUTPUT              | boolean       | Enforce a mode compatible with a streamable file                                                                         | NO          |                                                                                                     |
| 38 | GEOTIFF_KEYS_FLAVOR            | string-select | Which flavor of GeoTIFF keys must be used                                                                                | STANDARD    | STANDARD ESRI_PE                                                                                       |
| 39 | GEOTIFF_VERSION                | string-select | Which version of GeoTIFF must be used                                                                                    |          | AUTO 1.0 1.1                                                                                           |