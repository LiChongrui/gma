(window.webpackJsonp=window.webpackJsonp||[]).push([[197],{736:function(t,s,a){"use strict";a.r(s);var n=a(9),e=Object(n.a)({},(function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h2",{attrs:{id:"gma-smc-interpolate-idw-points-values-boundary-none-resolution-none-power-2-searchradius-12-inprojection-wgs84"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#gma-smc-interpolate-idw-points-values-boundary-none-resolution-none-power-2-searchradius-12-inprojection-wgs84"}},[t._v("#")]),t._v(" gma.smc.Interpolate."),a("strong",[t._v("IDW")]),t._v("("),a("em",[t._v("Points, Values, Boundary = None, Resolution = None, Power = 2, SearchRadius = 12, InProjection = 'WGS84'")]),t._v(")"),a("Badge",{attrs:{text:"1.1.0 +"}})],1),t._v(" "),a("hr"),t._v(" "),a("p",[a("strong",[t._v("功能：")]),t._v(" 【反距离权重法插值】。使用反距离加权法（IDW）将点插值成二维数组。")]),t._v(" "),a("p",[a("strong",[t._v("参数：")])]),t._v(" "),a("p",[t._v(" Points："),a("code",[t._v("list||tuple||array")]),t._v(" 。插值点 X（经度），Y（纬度）坐标。至少有 4 个坐标点。")]),t._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"title"},[t._v("示例")]),a("p",[t._v("Points = [(122.52,  52.97), (124.72,  52.35), (124.4 ,  51.67), (126.63,  51.73)]")])]),a("p",[t._v(" Values："),a("code",[t._v("array")]),t._v("。坐标点对应的数据值，与 Points 数量相同。")]),t._v(" "),a("p",[a("strong",[t._v("可选参数：")])]),t._v(" "),a("p",[t._v(" Boundary = "),a("code",[t._v("tuple")]),t._v("。插值结果的四至边界，分别为最小经度（左）、最小纬度（下）、最大经度（右）、最大纬度（上）。默认（None）从输入坐标点提取范围。")]),t._v(" "),a("p",[t._v(" Resolution = "),a("code",[t._v("float")]),t._v("。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。")]),t._v(" "),a("p",[t._v(" Power = "),a("code",[t._v("float")]),t._v("。距离指数（幂）。用来控制插值周围点的显著性，默认为 2。")]),t._v(" "),a("p",[t._v(" SearchRadius = "),a("code",[t._v("int")]),t._v("。搜索范围。指定要用于执行插值的最邻近输入采样点数量，默认为 12 个点。")]),t._v(" "),a("p",[t._v(" InProjection = "),a("code",[t._v("str")]),t._v("。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。")]),t._v(" "),a("p",[a("strong",[t._v("返回：")]),t._v(" 类型："),a("code",[t._v("namedtuple")]),t._v("。包含数据（Data）和仿射变换（Transform）。")]),t._v(" "),a("p",[a("strong",[t._v("参考文献：")])]),t._v(" "),a("p",[t._v(" [1] Philip, G. M., and D. F. Watson. A Precise Method for Determining Contoured Surfaces. Australian Petroleum Exploration Association Journal 22: 205–212. 1982.")]),t._v(" "),a("p",[t._v(" [2] Watson, D. F., and G. M. Philip. A Refinement of Inverse Distance Weighted Interpolation. Geoprocessing 2:315–327. 1985.")]),t._v(" "),a("hr"),t._v(" "),a("p",[a("strong",[t._v("示例 "),a("em",[t._v("（下载 "),a("a",{attrs:{href:"/smc/Interpolate.xlsx"}},[t._v("示例数据")]),t._v("）")]),t._v("：")])]),t._v(" "),a("div",{staticClass:"language-python line-numbers-mode"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" smc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" io\n\nELSXLayer "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" io"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ReadVector"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"Interpolate.xlsx"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nData "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" ELSXLayer"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ToDataFrame"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\nPoints "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("loc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'经度'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'纬度'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("values\nValues "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("loc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'值'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("values\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# 插值")]),t._v("\nIDWD "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" smc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Interpolate"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("IDW"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("Points"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" Values"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" Resolution "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("0.05")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])]),t._v(" "),a("div",{staticClass:"line-numbers-wrapper"},[a("span",{staticClass:"line-number"},[t._v("1")]),a("br"),a("span",{staticClass:"line-number"},[t._v("2")]),a("br"),a("span",{staticClass:"line-number"},[t._v("3")]),a("br"),a("span",{staticClass:"line-number"},[t._v("4")]),a("br"),a("span",{staticClass:"line-number"},[t._v("5")]),a("br"),a("span",{staticClass:"line-number"},[t._v("6")]),a("br"),a("span",{staticClass:"line-number"},[t._v("7")]),a("br"),a("span",{staticClass:"line-number"},[t._v("8")]),a("br"),a("span",{staticClass:"line-number"},[t._v("9")]),a("br"),a("span",{staticClass:"line-number"},[t._v("10")]),a("br")])]),a("p",[a("em",[t._v("与 ArcGIS IDW 插值结果（重分类后）对比：")])]),t._v(" "),a("p",[a("img",{attrs:{src:"/smc/IDW.webp",alt:"fdg"}})])])}),[],!1,null,null,null);s.default=e.exports}}]);