(window.webpackJsonp=window.webpackJsonp||[]).push([[84],{623:function(s,t,a){"use strict";a.r(t);var n=a(9),e=Object(n.a)({},(function(){var s=this,t=s.$createElement,a=s._self._c||t;return a("ContentSlotsDistributor",{attrs:{"slot-key":s.$parent.slotKey}},[a("h2",{attrs:{id:"gma-crs-projcs-name-gma-pcs-linearunit-meter-projmethod-albersconicequalarea-gcs-wgs84-aeraofuse-none"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#gma-crs-projcs-name-gma-pcs-linearunit-meter-projmethod-albersconicequalarea-gcs-wgs84-aeraofuse-none"}},[s._v("#")]),s._v(" gma.crs."),a("strong",[s._v("ProjCS")]),s._v("("),a("em",[s._v("Name='GMA PCS', LinearUnit='Meter', ProjMethod = 'AlbersConicEqualArea', GCS='WGS84', AeraOfUse=None")]),s._v(")")]),s._v(" "),a("hr"),s._v(" "),a("p",[a("strong",[s._v("功能：")]),s._v(" 创建一个自定义投影坐标系。")]),s._v(" "),a("p",[a("strong",[s._v("可选参数：")])]),s._v(" "),a("p",[s._v("  Name = "),a("code",[s._v("str")]),s._v("。坐标系名称。")]),s._v(" "),a("p",[s._v("  LinearUnit = "),a("code",[s._v("str||float")]),s._v("。线性单位。若为 str，则必须是内置线性单位的名称。")]),s._v(" "),a("p",[s._v("  ProjMethod = "),a("code",[s._v("str||class")]),s._v("。投影方法。若为 str，则必须是内置投影方法中的类名称。若为 class，则必须为 crs.ProjMethod 下自定义的投影方法。")]),s._v(" "),a("p",[s._v("  GCS = "),a("code",[s._v("str||int||class")]),s._v("。地理坐标系。可为 EPSG，WKT，Proj4，空间参考类或其他任何可识别坐标系。")]),s._v(" "),a("p",[s._v("  AeraOfUse = "),a("code",[s._v("None||list")]),s._v("。坐标系的使用范围（左、下、右、上），经纬度单位。若为 None，则视为世界范围 [-180, -90, 180, 90]。")]),s._v(" "),a("p",[a("strong",[s._v("返回：")]),s._v(" "),a("code",[s._v("SpatRef")]),s._v("。")]),s._v(" "),a("p",[a("strong",[s._v("示例：")])]),s._v(" "),a("div",{staticClass:"language-python line-numbers-mode"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("from")]),s._v(" gma "),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("import")]),s._v(" crs\n\nPCS "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" crs"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(".")]),s._v("ProjCS"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),s._v("Name "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'GMA PCS'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(",")]),s._v(" LinearUnit "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'Meter'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(",")]),s._v(" ProjMethod "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'AlbersConicEqualArea'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(",")]),s._v(" \n                 GCS "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[s._v("'WGS84'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(",")]),s._v(" AeraOfUse "),a("span",{pre:!0,attrs:{class:"token operator"}},[s._v("=")]),s._v(" "),a("span",{pre:!0,attrs:{class:"token boolean"}},[s._v("None")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[s._v("print")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v("(")]),s._v("GCS"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[s._v(")")]),s._v("\n")])]),s._v(" "),a("div",{staticClass:"line-numbers-wrapper"},[a("span",{staticClass:"line-number"},[s._v("1")]),a("br"),a("span",{staticClass:"line-number"},[s._v("2")]),a("br"),a("span",{staticClass:"line-number"},[s._v("3")]),a("br"),a("span",{staticClass:"line-number"},[s._v("4")]),a("br"),a("span",{staticClass:"line-number"},[s._v("5")]),a("br")])]),a("blockquote",[a("p",[s._v('>>> PROJCS["GMA PCS",\nGEOGCS["WGS 84",\nDATUM["WGS_1984",\nSPHEROID["WGS 84",6378137,298.257223563,\nAUTHORITY["EPSG","7030"]],\nAUTHORITY["EPSG","6326"]],\nPRIMEM["Greenwich",0,\nAUTHORITY["EPSG","8901"]],\nUNIT["degree",0.0174532925199433,\nAUTHORITY["EPSG","9122"]],\nAUTHORITY["EPSG","4326"]],\nPROJECTION["Albers_Conic_Equal_Area"],\nPARAMETER["longitude_of_center",0],\nPARAMETER["latitude_of_center",0],\nPARAMETER["false_easting",0],\nPARAMETER["false_northing",0],\nPARAMETER["standard_parallel_1",25],\nPARAMETER["standard_parallel_2",47],\nUNIT["Meter",1],\nAXIS["Easting",EAST],\nAXIS["Northing",NORTH]]')])])])}),[],!1,null,null,null);t.default=e.exports}}]);