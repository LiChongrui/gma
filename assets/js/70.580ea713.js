(window.webpackJsonp=window.webpackJsonp||[]).push([[70],{609:function(t,s,a){"use strict";a.r(s);var n=a(9),e=Object(n.a)({},(function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h2",{attrs:{id:"gma-climet-index-cwdi-pre-etc-axis-none-weights-0-3-0-25-0-2-0-15-0-1-durationperweight-10"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#gma-climet-index-cwdi-pre-etc-axis-none-weights-0-3-0-25-0-2-0-15-0-1-durationperweight-10"}},[t._v("#")]),t._v(" gma.climet.Index."),a("strong",[t._v("CWDI")]),t._v("("),a("em",[t._v("PRE, ETc, Axis=None, Weights=[0.3, 0.25, 0.2, 0.15, 0.1], DurationPerWeight=10")]),t._v(") "),a("Badge",{attrs:{text:"2.0.11 +"}})],1),t._v(" "),a("hr"),t._v(" "),a("p",[a("strong",[t._v("功能：")]),t._v("【作物水分亏缺指数】。计算作物水分亏缺指数（Crop Water Deficit Index）。")]),t._v(" "),a("p",[a("strong",[t._v("参数：")])]),t._v(" "),a("p",[t._v(" PRE: "),a("code",[t._v("array")]),t._v("。降水量（mm）。")]),t._v(" "),a("p",[t._v(" ETc: "),a("code",[t._v("array")]),t._v("。作物需水量（mm）。")]),t._v(" "),a("p",[a("strong",[t._v("可选参数：")])]),t._v(" "),a("p",[t._v("  Axis = "),a("code",[t._v("int||None")]),t._v("。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。")]),t._v(" "),a("p",[t._v("  Weights = "),a("code",[t._v("list")]),t._v("。分组权重。默认为 [0.3, 0.25, 0.2, 0.15, 0.1]。")]),t._v(" "),a("p",[t._v("  DurationPerWeight = "),a("code",[t._v("int")]),t._v("。与权重对应，每个权重系数对应的时长。默认为 10。")]),t._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"title"},[t._v("每日 CWDI")]),a("p",[t._v("用以计算每日 CWDI 的数据为当日及之前 len(Weights) × DurationPerWeight 日数据。默认情况下为 50 天（组）。")])]),a("p",[a("strong",[t._v("返回：")]),a("code",[t._v("array")]),t._v("。单位为 %。")]),t._v(" "),a("p",[a("strong",[t._v("参考文献：")])]),t._v(" "),a("p",[t._v(" Li Chongrui, You Songcai, Wu Yongfeng, Wang Yihao. Improved crop water deficit index for monitoring drought disaster change process of spring maize in the Northeast China[J]. Transactions of the Chinese Society of Agricultural Engineering (Transactions of the CSAE),  2019, 35(21): 175-185. DOI: 10.11975/j.issn.1002-6819.2019.21.021")]),t._v(" "),a("hr"),t._v(" "),a("p",[a("strong",[t._v("示例 ："),a("em",[t._v("基于 Excel 表数据（下载 "),a("a",{attrs:{href:"/climet/PRE_ET0.xlsx"}},[t._v("示例数据")]),t._v("）")])])]),t._v(" "),a("div",{staticClass:"language-python line-numbers-mode"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" climet"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" io\n\nELSXLayer "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" io"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ReadVector"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'PRE_ET0.xlsx'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nData "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" ELSXLayer"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ToDataFrame"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\nPRE "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'PRE'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("values\nETc "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'ET0'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("values    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("##这里仅做演示，实际使用时请使用真实的ETc。")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# 计算 CWDI 指数")]),t._v("\nCWDI "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" climet"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Index"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("CWDI"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("PRE"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" ETc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])]),t._v(" "),a("div",{staticClass:"line-numbers-wrapper"},[a("span",{staticClass:"line-number"},[t._v("1")]),a("br"),a("span",{staticClass:"line-number"},[t._v("2")]),a("br"),a("span",{staticClass:"line-number"},[t._v("3")]),a("br"),a("span",{staticClass:"line-number"},[t._v("4")]),a("br"),a("span",{staticClass:"line-number"},[t._v("5")]),a("br"),a("span",{staticClass:"line-number"},[t._v("6")]),a("br"),a("span",{staticClass:"line-number"},[t._v("7")]),a("br"),a("span",{staticClass:"line-number"},[t._v("8")]),a("br"),a("span",{staticClass:"line-number"},[t._v("9")]),a("br"),a("span",{staticClass:"line-number"},[t._v("10")]),a("br")])]),a("blockquote",[a("p",[t._v("CWDI 计算结果")])]),t._v(" "),a("p",[a("img",{attrs:{src:"/climet/CWDI.svg",alt:""}})])])}),[],!1,null,null,null);s.default=e.exports}}]);