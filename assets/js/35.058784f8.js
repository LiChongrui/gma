(window.webpackJsonp=window.webpackJsonp||[]).push([[35],{582:function(t,v,a){"use strict";a.r(v);var _=a(9),e=Object(_.a)({},(function(){var t=this,v=t.$createElement,a=t._self._c||v;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("div",{staticClass:"custom-block warning"},[a("p",{staticClass:"title"},[t._v("注意")]),a("p",[t._v("自 "),a("Badge",{attrs:{text:"1.0.7",vertical:"middle"}}),t._v("  版本开始，gma 内各个函数生成 GTiff 文件时 "),a("strong",[t._v("不在默认")]),t._v(" 生成 .ovr 金字塔。")],1)]),a("p",[a("i",{staticClass:"fas fa-box"}),t._v(" "),a("strong",[t._v("引入包：")])]),t._v(" "),a("div",{staticClass:"custom-block theorem"},[a("p",{staticClass:"title"}),a("p",[a("strong",[t._v("引入 "),a("RouterLink",{attrs:{to:"/UserGuide/Instructions/Function.html#栅格分析"}},[t._v("raa")]),t._v(" 函数包。")],1),t._v(" 提供栅格数据分析功能！")]),t._v(" "),a("p",[a("strong",[t._v("引入 "),a("RouterLink",{attrs:{to:"/UserGuide/Instructions/Function.html#高级配置"}},[t._v("config")]),t._v(" 函数包。")],1),t._v(" 提供栅格高级参数配置查询功能！")])]),a("p",[a("font",{attrs:{color:"#616AE5"}},[a("i",{staticClass:"fas fa-award"})]),t._v(" "),a("strong",[t._v("新增：")])],1),t._v(" "),a("p",[t._v(" 　1、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/Roughness.html"}},[t._v("Roughness")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算粗糙度！引用：gma.raa.DEM.Roughness。")]),t._v(" "),a("p",[t._v(" 　2、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/HillShade.html"}},[t._v("HillShade")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算山体阴影！引用：gma.raa.DEM.HillShade。")]),t._v(" "),a("p",[t._v(" 　3、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/Slope.html"}},[t._v("Slope")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算坡度！引用：gma.raa.DEM.Slope。")]),t._v(" "),a("p",[t._v(" 　4、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/Aspect.html"}},[t._v("Aspect")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算坡向！引用：gma.raa.DEM.Aspect。")]),t._v(" "),a("p",[t._v(" 　5、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/TRI.html"}},[t._v("TRI")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算地形耐用度指数！引用：gma.raa.DEM.TRI。")]),t._v(" "),a("p",[t._v(" 　6、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/raa/DEM/TPI.html"}},[t._v("TPI")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　从任何支持的 DEM 栅格文件计算地形位置指数！引用：gma.raa.DEM.TPI。")]),t._v(" "),a("p",[t._v(" 　7、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/GetRACreationOption.html"}},[t._v("GetRACreationOption")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　获取栅格驱动格式支持的高级创建选项！引用：gma.config.GetRACreationOption。")]),t._v(" "),a("p",[t._v(" 　8、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/GetRasterFormat.html"}},[t._v("GetRasterFormat")]),t._v("】类")],1),t._v(" "),a("p",[t._v(" 　　实现针对某一栅格驱动详细信息的获取！引用：gma.config.GetRasterFormat。类支持的属性包括：")]),t._v(" "),a("p",[t._v(" 　　a. ColorTableDataType： 色彩映射表支持的数据类型。")]),t._v(" "),a("p",[t._v(" 　　b. CompressMode：支持的压缩方式。")]),t._v(" "),a("p",[t._v(" 　　c. CreationDataType：支持创建的数据类型。")]),t._v(" "),a("p",[t._v(" 　　d. Details：详细信息。")]),t._v(" "),a("p",[t._v(" 　　e. GeoReferencing：地理参考支持。")]),t._v(" "),a("p",[t._v(" 　　f. LongName：驱动长名称。")]),t._v(" "),a("p",[t._v(" 　　g. Multiband：多波段支持。")]),t._v(" "),a("p",[t._v(" 　　h. Update：更新支持。")]),t._v(" "),a("p",[t._v(" 　　i. Extension：驱动扩展名。")]),t._v(" "),a("p",[t._v(" 　9、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/GetVectorFormat.html"}},[t._v("GetVectorFormat")]),t._v("】类")],1),t._v(" "),a("p",[t._v(" 　　实现针对某一矢量驱动详细信息的获取！引用：gma.config.GetVectorFormat。类支持的属性包括：")]),t._v(" "),a("p",[t._v(" 　　a. CreationFieldDataType：支持创建属性表字段类型。")]),t._v(" "),a("p",[t._v(" 　　b. Details：详细信息。")]),t._v(" "),a("p",[t._v(" 　　c. Extension：驱动扩展名。")]),t._v(" "),a("p",[t._v(" 　　d. GeoReferencing：地理参考支持。")]),t._v(" "),a("p",[t._v(" 　　e. LongName：驱动长名称。")]),t._v(" "),a("p",[t._v(" 　　f. MultiLayer：多图层支持。")]),t._v(" "),a("p",[t._v(" 　　g. Update：更新支持。")]),t._v(" "),a("p",[t._v(" 　10、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/GetVELayerCreationOption.html"}},[t._v("GetVELayerCreationOption")]),t._v("】函数")],1),t._v(" "),a("p",[t._v(" 　　获取矢量驱动格式支持的图层高级创建选项！引用：gma.config.GetVELayerCreationOption。")]),t._v(" "),a("p",[t._v(" 　11、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/RasterFormatInfo.html"}},[t._v("RasterFormatInfo")]),t._v("】类")],1),t._v(" "),a("p",[t._v(" 　　获取所有栅格驱动格式分类的详细信息！引用：gma.config.RasterFormatInfo。类支持的属性包括：")]),t._v(" "),a("p",[t._v(" 　　a. AddableColorTableFormats：支持色彩映射表的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　b. CompressibleFormats：支持压缩的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　c. CopyableFormats：支持复制的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　d. CreatableFormats：支持创建的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　e. MultibandFormats：支持多波段的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　f. ReadableFormats：支持读取的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　g. TransformableFormats：支持转换的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　h. UpdatableFormats：支持更新的驱动格式。")]),t._v(" "),a("p",[t._v(" 　12、增加【"),a("RouterLink",{attrs:{to:"/UserGuide/config/VectorFormatInfo.html"}},[t._v("VectorFormatInfo")]),t._v("】类")],1),t._v(" "),a("p",[t._v(" 　　获取所有矢量驱动格式分类的详细信息！引用：gma.config.VectorFormatInfo。类支持的属性包括：")]),t._v(" "),a("p",[t._v(" 　　a. CopyableFormats：支持复制的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　b. CreatableFormats：支持创建的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　c. MultiLayerFormats：支持多图层的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　d. ReadableFormats：支持读取的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　e. TransformableFormats：支持转换的驱动格式。")]),t._v(" "),a("p",[t._v(" 　　f. UpdatableFormats：支持更新的驱动格式。")]),t._v(" "),a("p",[a("font",{attrs:{color:"#3CB371"}},[a("i",{staticClass:"fab fa-superpowers"})]),t._v(" "),a("strong",[t._v("优化：")])],1),t._v(" "),a("p",[t._v(" 　1、将 栅格/矢量 生成过程中的高级 "),a("strong",[t._v("创建参数外置")]),t._v("。在未来的几个版本，栅格/矢量生成过程的高级配置参数会逐步开放设置。")]),t._v(" "),a("p",[t._v(" 　2、基于外置的创建参数，对所有 "),a("strong",[t._v("栅格处理函数")]),t._v(" 进行 "),a("strong",[t._v("第二次重构")]),t._v("，以实现所有的栅格处理函数在底层隶属于一个整体，而不仅仅是许多单独的函数的集合。")]),t._v(" "),a("p",[t._v(" 　3、rasp.Clip")]),t._v(" "),a("p",[t._v(" 　　移除 MaskBoundary 参数，增加 LayerID （掩膜矢量图层 ID）、FeatureID （掩膜图层要素 ID）参数。")]),t._v(" "),a("p",[t._v(" 　4、rasp.GenerateOVR")]),t._v(" "),a("p",[t._v(" 　　增加 Compress（压缩方式）、Resample（重采样方法）、BlockSize（分块大小）参数。")]),t._v(" "),a("p",[t._v(" 　5、rasp.Fusion")]),t._v(" "),a("p",[t._v(" 　　移除了 Fusion 类初始化参数，初始化内容合并到类内函数。")]),t._v(" "),a("p",[t._v(" 　6、rasp.Fusion.Pansharpen")]),t._v(" "),a("p",[t._v(" 　　承接 Fusion 初始化参数。优化内部生成逻辑，使源代码更简洁。")]),t._v(" "),a("p",[t._v(" 　7、relation.key")]),t._v(" "),a("p",[t._v(" 　　调整并优化了与外置的高级创建参数内容重复的内容。")]),t._v(" "),a("p",[t._v(" 　8、vesp.FixGeometry")]),t._v(" "),a("p",[t._v(" 　　面积或长度值小于 0.00000001 的要素将会被清除。")])])}),[],!1,null,null,null);v.default=e.exports}}]);