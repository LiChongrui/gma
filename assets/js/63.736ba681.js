(window.webpackJsonp=window.webpackJsonp||[]).push([[63],{602:function(s,t,a){"use strict";a.r(t);var n=a(9),e=Object(n.a)({},(function(){var s=this,t=s.$createElement,a=s._self._c||t;return a("ContentSlotsDistributor",{attrs:{"slot-key":s.$parent.slotKey}},[a("h2",{attrs:{id:"gma-climet-diagnosis-buishand-data-axis-none-method-q"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#gma-climet-diagnosis-buishand-data-axis-none-method-q"}},[s._v("#")]),s._v(" gma.climet.Diagnosis."),a("strong",[s._v("Buishand")]),s._v("("),a("em",[s._v("Data, Axis = None, Method = 'Q'")]),s._v(")"),a("Badge",{attrs:{text:"1.1.1 +"}})],1),s._v(" "),a("hr"),s._v(" "),a("p",[a("strong",[s._v("功能：")]),s._v("【Buishand 突变点检验】。基于 Buishand 法对时间序列数据进行突变点检验。")]),s._v(" "),a("p",[a("strong",[s._v("参数：")])]),s._v(" "),a("p",[s._v(" Data："),a("code",[s._v("list||array")]),s._v(" 。需要检验的数据。")]),s._v(" "),a("p",[a("strong",[s._v("可选参数：")])]),s._v(" "),a("p",[s._v(" Axis = "),a("code",[s._v("int")]),s._v("  。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。")]),s._v(" "),a("p",[s._v(" Method = "),a("code",[s._v("Q")]),s._v("  。Buishand 方法。默认为 'Q'。")]),s._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"title"},[s._v("其他方法")]),a("p",[s._v("'Range'，'LL Ration'，'U'。")])]),a("p",[a("strong",[s._v("返回：")]),s._v(" "),a("code",[s._v("namedtuple")]),s._v("。")]),s._v(" "),a("p",[s._v("  最大统计量：R（Range）或 Q（Q）或 V（LL Ration）或 U（U）。")]),s._v(" "),a("p",[s._v("  LOC：突变位置。")]),s._v(" "),a("hr"),s._v(" "),a("p",[a("strong",[s._v("示例：")])]),s._v(" "),a("div",{staticClass:"language-python line-numbers-mode"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("from")]),s._v(" gma "),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("import")]),s._v(" climet\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[s._v("# 这里建立一个随机序列来模拟代码数据处理过程")]),s._v("\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("import")]),s._v(" numpy "),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("as")]),s._v(" np\nnp"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("random"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("seed"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("0")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\nData "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" np"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("random"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("uniform"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),s._v("size "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[s._v("72")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\n\nBD "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" climet"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("Diagnosis"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("Buishand"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),s._v("Data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(",")]),s._v(" Method"),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'Q'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\n\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("print")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),s._v("BD"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\n")])]),s._v(" "),a("div",{staticClass:"line-numbers-wrapper"},[a("span",{staticClass:"line-number"},[s._v("1")]),a("br"),a("span",{staticClass:"line-number"},[s._v("2")]),a("br"),a("span",{staticClass:"line-number"},[s._v("3")]),a("br"),a("span",{staticClass:"line-number"},[s._v("4")]),a("br"),a("span",{staticClass:"line-number"},[s._v("5")]),a("br"),a("span",{staticClass:"line-number"},[s._v("6")]),a("br"),a("span",{staticClass:"line-number"},[s._v("7")]),a("br"),a("span",{staticClass:"line-number"},[s._v("8")]),a("br"),a("span",{staticClass:"line-number"},[s._v("9")]),a("br")])]),a("blockquote",[a("p",[s._v(">>> BuishandQ(Q=1.2571112721486875, LOC=40)")])])])}),[],!1,null,null,null);t.default=e.exports}}]);