(window.webpackJsonp=window.webpackJsonp||[]).push([[101],{640:function(t,a,s){"use strict";s.r(a);var n=s(9),e=Object(n.a)({},(function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h2",{attrs:{id:"io-readarrayasdataset-array-projection-none-transform-none-datatype-none-nodata-none"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#io-readarrayasdataset-array-projection-none-transform-none-datatype-none-nodata-none"}},[t._v("#")]),t._v(" io."),s("strong",[t._v("ReadArrayAsDataSet")]),t._v("("),s("em",[t._v("Array, Projection = None, Transform = None, DataType = None, NoData = None")]),t._v(")")]),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("功能：")]),t._v(" 【读取 NumPy 数组 为 DataSet】。")]),t._v(" "),s("p",[s("strong",[t._v("参数：")])]),t._v(" "),s("p",[t._v(" Array："),s("code",[t._v("array")]),t._v("。输入数组。")]),t._v(" "),s("p",[s("strong",[t._v("可选参数：")])]),t._v(" "),s("p",[t._v(" Projection  = "),s("code",[t._v("str||EPSG||WKT||Proj4||SpatRef||...")]),t._v(" 。输出栅格坐标系。默认不指定坐标系（None）。")]),t._v(" "),s("p",[t._v(" Transform  = "),s("code",[t._v("tuple")]),t._v("。输出栅格的仿射变换。默认不指定仿射变换（None）。")]),t._v(" "),s("p",[t._v(" Format   = "),s("code",[t._v("str")]),t._v("。输出栅格文件格式。默认为 GTiff。其他格式详见 ToOtherFormat 函数。")]),t._v(" "),s("p",[t._v(" DataType  = "),s("code",[t._v("int||str")]),t._v("。输出栅格数据类型的代码或字符串标记。默认根据写出数组的数据类型确定（None），其他类型详见 ChangeDataType 函数。")]),t._v(" "),s("p",[t._v(" NoData = "),s("code",[t._v("float")]),t._v("。输出栅格的无效值。默认不设置无效值（None）。")]),t._v(" "),s("p",[s("strong",[t._v("返回：")]),s("code",[t._v("DataSet")]),t._v("。")]),t._v(" "),s("p",[s("em",[s("strong",[t._v(" 类内属性/方法详见："),s("RouterLink",{attrs:{to:"/UserGuide/io/DataSet.html"}},[t._v("DataSet")]),t._v("。")],1)])]),t._v(" "),s("hr"),t._v(" "),s("p",[s("strong",[t._v("示例：")])]),t._v(" "),s("div",{staticClass:"language-python line-numbers-mode"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" gma "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" io\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" numpy "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("as")]),t._v(" np\n\nnp"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("random"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("seed"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("1992")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nData "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" np"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("random"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("uniform"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("0")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("100")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" size "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("50")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("100")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\nDataSet "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" io"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("ReadArrayAsDataSet"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("Data"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" Projection "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("3857")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("print")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("DataSet"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])]),t._v(" "),s("div",{staticClass:"line-numbers-wrapper"},[s("span",{staticClass:"line-number"},[t._v("1")]),s("br"),s("span",{staticClass:"line-number"},[t._v("2")]),s("br"),s("span",{staticClass:"line-number"},[t._v("3")]),s("br"),s("span",{staticClass:"line-number"},[t._v("4")]),s("br"),s("span",{staticClass:"line-number"},[t._v("5")]),s("br"),s("span",{staticClass:"line-number"},[t._v("6")]),s("br"),s("span",{staticClass:"line-number"},[t._v("7")]),s("br"),s("span",{staticClass:"line-number"},[t._v("8")]),s("br")])]),s("blockquote",[s("p",[t._v(">>> <gma.algos.dataio.rads.DataSet at 0x......>")])]),t._v(" "),s("p",[s("img",{attrs:{src:"/io/ReadArrayAsDataSet.png",alt:""}})])])}),[],!1,null,null,null);a.default=e.exports}}]);