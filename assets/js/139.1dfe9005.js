(window.webpackJsonp=window.webpackJsonp||[]).push([[139],{678:function(t,a,s){"use strict";s.r(a);var n=s(9),e=Object(n.a)({},(function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h2",{attrs:{id:"gma-math-kernel-gaussfilter-data-kernelsize-3-nodata-none-axis-none-edgeexpmode-edge-sigma-1-nsrange-1"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#gma-math-kernel-gaussfilter-data-kernelsize-3-nodata-none-axis-none-edgeexpmode-edge-sigma-1-nsrange-1"}},[t._v("#")]),t._v(" gma.math.Kernel."),s("strong",[t._v("GaussFilter")]),t._v("("),s("em",[t._v("Data, KernelSize = 3, NoData = None, Axis = None, EdgeEXPMode = 'Edge', Sigma = 1, NSRange = 1")]),t._v(")"),s("Badge",{attrs:{text:"1.0.11 +"}})],1),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("功能：")]),t._v(" 【高斯滤波】。利用高斯核对数组进行滤波处理。")]),t._v(" "),s("p",[s("strong",[t._v("参数：")])]),t._v(" "),s("p",[t._v(" Data: 所有数据类型。需要计算的数据。")]),t._v(" "),s("p",[s("strong",[t._v("可选参数：")])]),t._v(" "),s("p",[t._v(" KernelSize = "),s("code",[t._v("int")]),t._v("。滤波核大小。默认为 3 。")]),t._v(" "),s("p",[t._v(" NoData = "),s("code",[t._v("float")]),t._v("。输入数组中的无效值。此值不会参与滤波计算，默认自动设置（None）。")]),t._v(" "),s("p",[t._v(" Axis = "),s("code",[t._v("int||list")]),t._v("。计算轴。默认自动扩展到所有轴（None）。")]),t._v(" "),s("p",[t._v(" EdgeEXPMode = "),s("code",[t._v("str||float")]),t._v("。边缘数据扩展方法。默认使用边缘值扩展（'Edge'）。")]),t._v(" "),s("div",{staticClass:"custom-block tip"},[s("p",{staticClass:"title"},[t._v("其他边缘值处理方法")]),s("p",[t._v("str: Edge，Linear_Ramp，Maximum，Mean，Median，Minimum，Reflect，Symmetric，Wrap，Empty。")]),t._v(" "),s("p",[t._v("float: 若配置为常数，则用此常数扩展。")])]),s("p",[t._v(" Sigma = "),s("code",[t._v("float")]),t._v("。生成高斯滤波核的标准差。默认为 1。")]),t._v(" "),s("p",[t._v(" NSRange = "),s("code",[t._v("float")]),t._v("。生成高斯滤波核的范围。默认为高斯分布 ± 1 个标准差内。")]),t._v(" "),s("p",[s("strong",[t._v("返回：")]),s("code",[t._v("array")]),t._v("。")]),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("示例：")])]),t._v(" "),s("div",{staticClass:"language-python line-numbers-mode"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" math\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" numpy "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("as")]),t._v(" np\n\nnp"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("random"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("seed"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("1992")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nData "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" np"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("random"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("uniform"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("0")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("100")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("200")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("200")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\nGF3 "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" math"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Kernel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("GaussFilter"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("Data"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" KernelSize "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("3")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nGF9 "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" math"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Kernel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("GaussFilter"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("Data"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" KernelSize "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("9")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])]),t._v(" "),s("div",{staticClass:"line-numbers-wrapper"},[s("span",{staticClass:"line-number"},[t._v("1")]),s("br"),s("span",{staticClass:"line-number"},[t._v("2")]),s("br"),s("span",{staticClass:"line-number"},[t._v("3")]),s("br"),s("span",{staticClass:"line-number"},[t._v("4")]),s("br"),s("span",{staticClass:"line-number"},[t._v("5")]),s("br"),s("span",{staticClass:"line-number"},[t._v("6")]),s("br"),s("span",{staticClass:"line-number"},[t._v("7")]),s("br"),s("span",{staticClass:"line-number"},[t._v("8")]),s("br")])]),s("p",[s("img",{attrs:{src:"/math/GaussFilter.svg",alt:""}})])])}),[],!1,null,null,null);a.default=e.exports}}]);