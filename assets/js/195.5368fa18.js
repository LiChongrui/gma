(window.webpackJsonp=window.webpackJsonp||[]).push([[195],{734:function(t,a,s){"use strict";s.r(a);var n=s(9),e=Object(n.a)({},(function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h2",{attrs:{id:"gma-smc-extraction-extractvalues-points-gmadataset"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#gma-smc-extraction-extractvalues-points-gmadataset"}},[t._v("#")]),t._v(" gma.smc.Extraction."),s("strong",[t._v("ExtractValues")]),t._v("("),s("em",[t._v("Points, GMADataSet")]),t._v(")")]),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("功能：")]),t._v(" 【计算面积】。计算输入多点组成多边形的面积。")]),t._v(" "),s("p",[s("strong",[t._v("参数：")])]),t._v(" "),s("p",[t._v(" Points："),s("code",[t._v("list||tuple||array")]),t._v(" 。需要提取数据点的 X（经度），Y（纬度）坐标。")]),t._v(" "),s("div",{staticClass:"custom-block tip"},[s("p",{staticClass:"title"},[t._v("示例")]),s("p",[t._v("Points = [(130.1, 45.2), (131.5, 40.2), (131.5, 45.2)]")])]),s("p",[t._v(" GMADataSet："),s("code",[t._v("DataSet")]),t._v(" 。用于提取数据的 gma 栅格数据集 DataSet。")]),t._v(" "),s("div",{staticClass:"custom-block warning"},[s("p",{staticClass:"title"},[t._v("注意")]),s("p",[t._v("请保证坐标点和栅格数据集的坐标系相同。")])]),s("p",[s("strong",[t._v("返回：")]),s("code",[t._v("DataFrame")]),t._v("。")]),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("示例：")])]),t._v(" "),s("div",{staticClass:"language-python line-numbers-mode"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("map")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" inres\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" smc\n\nDEMDS "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" inres"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("WorldDataSet"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("DEM\nPoints "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("112")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("30")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("120")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("45")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n\nEVData "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" smc"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Extraction"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ExtractValues"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("Points"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" DEMDS"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])]),t._v(" "),s("div",{staticClass:"line-numbers-wrapper"},[s("span",{staticClass:"line-number"},[t._v("1")]),s("br"),s("span",{staticClass:"line-number"},[t._v("2")]),s("br"),s("span",{staticClass:"line-number"},[t._v("3")]),s("br"),s("span",{staticClass:"line-number"},[t._v("4")]),s("br"),s("span",{staticClass:"line-number"},[t._v("5")]),s("br"),s("span",{staticClass:"line-number"},[t._v("6")]),s("br"),s("span",{staticClass:"line-number"},[t._v("7")]),s("br")])]),s("blockquote",[s("p",[t._v(">>>")])]),t._v(" "),s("table",[s("thead",[s("tr",[s("th",{staticStyle:{"text-align":"right"}}),t._v(" "),s("th",{staticStyle:{"text-align":"right"}},[t._v("X")]),t._v(" "),s("th",{staticStyle:{"text-align":"right"}},[t._v("Y")]),t._v(" "),s("th",{staticStyle:{"text-align":"right"}},[t._v("Band_0")])])]),t._v(" "),s("tbody",[s("tr",[s("td",{staticStyle:{"text-align":"right"}},[t._v("0")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("112")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("30")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("44")])]),t._v(" "),s("tr",[s("td",{staticStyle:{"text-align":"right"}},[t._v("1")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("120")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("45")]),t._v(" "),s("td",{staticStyle:{"text-align":"right"}},[t._v("742")])])])])])}),[],!1,null,null,null);a.default=e.exports}}]);