---
title: 【GeoDataBase】
sidebar: false
---

&emsp;　**示例：** *（下载 [示例地理数据库（GPKG）](/io/GeoDataBase.gpkg)）*

```python
from gma import io
GDB = io.Open("GeoDataBase.gpkg")
# GDB = io.Open("GeoDataBase.gpkg", nOpenFlags = 1)  # 可修改模式
```

::: warning 注意

如果期望修改数据库（例如添加/删除图层等），请传入参数 nOpenFlags = 1。

:::


 **GeoDataBase** 具有如下所列的 方法/属性：


| 序号 | 名称                                                         | 描述                          | 返回值类型             | 实例                | 示例返回值           |
| :--- | :----------------------------------------------------------- | :---------------------------- | :--------------------- | :------------------ | ------------------- |
| M.1  | [AddLayer](#addlayer)  | 添加矢量图层 |  | GDB.AddLayer() |  |
| M.2  | [DeleteLayer](#deletelayer)  | 删除矢量图层 |  | GDB.DeleteLayer() |  |
| M.3  | [GetDataSet](#getdataset)  | 获取栅格数据集 | `DataSet` | GDB.GetDataSet() |  |
| M.4  | [GetLayer](#getlayer)  | 获取栅格数据集 | `Layer` | GDB.GetLayer() |  |
| M.5  | [SQLQuery](#sqlquery)  | 执行 SQL 查询语句 | `Layer` | GDB.SQLQuery() |  |
| P.1 | DataSetCount| 栅格数据集数量   | `int`      | GDB.DataSetCount        | 0       |
| P.2 | DataSetNames | 栅格数据集名称                       | `list`                  | GDB.DataSetNames            | []        |
| P.3  | Driver                                                    | 数据库驱动                     | `str`                 | GDB.Driver       | 'GPKG' |
| P.4  | Info                                                         | 栅格信息                      | `DataFrame`                 | GDB.Info             | [点击跳转](#在-jupyter-notebook-中查看地理数据库信息-与-info-属性一致) |
| P.5  | LayerCount                                                      | 矢量图层数量                          | `int`                | GDB.LayerCount       | 8      |
| P.6  | LayerNames                                                    | 矢量图层名称                         | `list`                  | GDB.LayerNames       | ['Bridge',  'Gates',  ...] |
| P.7  | Metadata                                                   | 元数据                         | `dict`               | GDB.Metadata       | {}     |


## AddLayer(*GMALayer*)

**功能：**【向数据库添加矢量图层】。

**参数：**

 &emsp;GMALayer：`Layer`。一个矢量图层。


**示例：** [请参考：CreateDataBase](CreateGeoDataBase.html)。


## DeleteLayer(*LayerName*)

**功能：**【删除数据库中的一个矢量图层】。

**参数：**

 &emsp;LayerName：`str`。矢量图层名称。

**示例：**

```python
GDB.DeleteLayer('Gates') # 删除数据库中名称为 Gates 的图层。
```

## GetDataSet(*DSIDOrName=0*）

**功能：**【获取数据库中的栅格数据集】。

**参数：**

 &emsp;DSIDOrName：`str||int`。数据集名称或序号。

**返回：**`DataSet`。

::: tip 提示

可通过 Info 属性，获得数据库中所有 栅格数据集的 名称 和 ID。

:::


## GetLayer(*LYIDOrName=0*）

**功能：**【获取数据库中的矢量图层】。

**参数：**

 &emsp;LYIDOrName：`str||int`。图层名称或序号。

**返回：**`Layer`。


::: tip 提示

可通过 Info 属性，获得数据库中所有 矢量图层的 名称 和 ID。

:::

**示例：**

```python
Bridge = GDB.GetLayer('Bridge') # 获取数据库中名称为 Bridge 的图层。
```

## SQLQuery(*SQLExpr*)

**功能：**【执行 SQL(ite)  查询语句】。

**参数：**

 &emsp;SQLExpr：`str`。SQL(ite) 表达式。

**返回：**`Layer`。

**示例：**

```python
# 筛选 Bridge 图层中属性表字段“桥”的值为“天津桥”的数据。
SQLLayer = GDB.SQLQuery('SELECT * FROM "Bridge" WHERE "桥" = "天津桥"')  
```


## 在  jupyter notebook 中查看地理数据库信息（与 Info 属性一致）
```jupyter notebook
GDB
```

|  Name            | Type  |   ID |
| :----------- | :---- | ---: |
| **Bridge**       | Layer |    0 |
| **Gates**        | Layer |    1 |
| **LuoShui**      | Layer |    2 |
| **Market**       | Layer |    3 |
| **Neighborhood** | Layer |    4 |
| **Taiwei**      | Layer |    5 |
| **Wall**       | Layer |    6 |
| **Ziwei**      | Layer |    7 |





