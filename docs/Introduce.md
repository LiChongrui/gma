---
title: Introduce
date: 2023-08-20
subSidebar: false
---
<p style = "text-indent: 2em;"><strong  style = "color:#616AE5; size=3.5;">Geographic and Meteorological Analysis (gma)</strong>
 is a Python-based function package for rapid processing and analysis of geographic and meteorological data, as well as geospatial mapping. Its development draws on the operational logic and features of ArcGIS and QGIS, while incorporating numerous original and unique functionalities with a distinctive code architecture philosophy.</p>

## Included Features

> + **gio(Raster/Vector Data I/O Module)**  
> Includes data opening, information viewing, conversion, extraction, and in-memory raster/vector data creation.
> 
> + **crs(Spatial Reference System)**  
> Includes geographic/projection coordinate system creation, datum/ellipsoid creation, projection method configuration, and initialization of > existing spatial references.
> 
> + **smc(Spatial Miscellaneous Calculations)**  
> Includes spatial queries (length measurement, coordinate conversion, etc.) and spatial interpolation (Inverse Distance Weighting, Kriging, etc.).
> 
> + **etools(Extension Tools)**  
> Includes surface analysis (slope, aspect, etc.), raster mosaicking, image correction, mosaicking, merging, and more.
> 
> + **carto(Geospatial Mapping)**  
> Includes raster and vector data plotting, as well as generation of north arrows, scale bars, etc.
> 
> + **math(Mathematical Operations)**  
> Includes data smoothing, evaluation, filtering, stretching, enhancement, transformation, and more.
> 
> + **climet(Climatic and Meteorological Index Calculation)**  
> Includes climate indices (SPEI, SPI, etc.), various potential evapotranspiration algorithms (Penman-Monteith method, etc.), climate diagnostics (Mann-Kendall mutation test, etc.), and other related algorithms (sun–earth relative distance, etc.).
> 
> + **rsvi(Remote Sensing Vegetation Indices)**  
> Includes calculation of remote sensing vegetation indices such as NDVI, EVI, TVDI, and more.

## Original Intent

&emsp;&emsp;For most researchers in geoscience or meteorology, data processing is a massive undertaking, often taking hours or even days. Without proper tools or methods, it becomes extremely challenging to handle multi-temporal datasets (e.g., time-series remote sensing data) or large-scale studies (e.g., national-level analysis).

&emsp;&emsp;Thus, the original purpose of building gma was to address these challenges. As the library has evolved through successive versions, its capabilities have grown increasingly rich and robust, enabling it to solve an ever-widening range of problems.

## Development Goals

  As gma continues to evolve through iterative updates, its development philosophy and goals have become increasingly clear:

  **(1) Data Processing**

&emsp;&emsp;Built on GDAL (OGR/OSR), simplifying and optimizing user interaction logic to build faster, more convenient, and more practical Python methods for geographic and meteorological data processing and analysis.

  **(2) Climate and Meteorology**

&emsp;&emsp;Based on the NumPy ecosystem, covering the entire process from data preprocessing and extraction to climate applications, fully encapsulating complex mathematical methods to simplify usage and lower the barrier to entry.

  **(3) Geospatial Mapping**

&emsp;&emsp;Using ArcGIS interaction logic as a reference template, building a Python geospatial mapping system independent of cartopy.

  **(4) Domestic Open-Source GIS Applications**

&emsp;&emsp;Drawing inspiration from ArcGIS Toolbox functionality, striving to become the most feature-rich Python open-source geospatial processing toolkit in China.



