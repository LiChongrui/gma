---
title: 组织方式
date: 2021-10-29
---

## 构建思路

&emsp;&emsp; gma 整体按照 **库-模块-类/函数-（方法/属性/子类）** 的思路构建，详细思路如下所示：

<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 776.87 297.86" width="100%" height="100%">
	<defs>
		<style>.cls-1{fill:#9cf;}.cls-2{isolation:isolate;}.cls-10,.cls-2{font-size:14.39px;font-family:MicrosoftYaHei, Microsoft YaHei;}.cls-3{fill:#dbeef3;}.cls-4{fill:#fcebdd;}.cls-5{fill:#f2dcda;}.cls-6,.cls-8,.cls-9{fill:none;}.cls-6{stroke:#000;stroke-linecap:round;stroke-linejoin:round;stroke-width:0.75px;}.cls-7{fill:#ebf1df;}.cls-8,.cls-9{stroke:#d3d3d3;stroke-miterlimit:10;}.cls-9{stroke-dasharray:12.16 12.16;}.cls-10{fill:gray;}</style>
	</defs>
	<g id="shape1-1">
		<rect class="cls-1" x="419.35" y="10.72" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(442.37 29.19) scale(1.09 1)">库</text>
	</g>
	<g id="shape2-4">
		<rect class="cls-3" x="310.33" y="79.63" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(321.59 98.11) scale(1.09 1)">模块1</text>
	</g>
	<g id="shape3-7">
		<rect class="cls-3" x="419.35" y="79.63" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(430.61 98.11) scale(1.09 1)">模块2</text>
	</g>
	<g id="shape4-10">
		<rect class="cls-3" x="528.37" y="79.63" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(539.63 98.11) scale(1.09 1)">模块3</text>
	</g>
	<g id="shape5-13">
		<rect class="cls-4" x="256.07" y="141" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(275.17 159.47) scale(1.09 1)">类1</text>
	</g>
	<g id="shape7-16">
		<rect class="cls-4" x="357.64" y="141.32" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(368.9 159.8) scale(1.09 1)">函数1</text>
	</g>
	<g id="shape9-19">
		<rect class="cls-5" x="154.5" y="206.14" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(165.76 224.61) scale(1.09 1)">方法1</text>
	</g>
	<g id="shape10-22">
		<rect class="cls-5" x="256.07" y="206.14" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(267.33 224.61) scale(1.09 1)">属性1</text>
	</g>
	<g id="shape11-25">
		<rect class="cls-5" x="357.64" y="206.14" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(368.9 224.61) scale(1.09 1)">子类1</text>
	</g>
	<g id="shape12-28">
		<path class="cls-6" d="M450.21,39V79.63"/>
	</g>
	<g id="shape13-31">
		<path class="cls-6" d="M450.21,39V56.6h-109v23"/>
	</g>
	<g id="shape14-34">
		<path class="cls-6" d="M450.21,39V56.5h109V79.63"/>
	</g>
	<g id="shape15-37">
		<path class="cls-6" d="M341.19,108v17H286.93v16"/>
	</g>
	<g id="shape16-40">
		<path class="cls-6" d="M341.19,108v16.75H388.5v16.61"/>
	</g>
	<g id="shape17-43">
		<path class="cls-6" d="M286.92,169.32v36.82"/>
	</g>
	<g id="shape18-46">
		<path class="cls-6" d="M286.92,169.32v18H185.35v18.81"/>
	</g>
	<g id="shape19-49">
		<path class="cls-6" d="M286.92,169.32v17.91H388.5v18.91"/>
	</g>
	<g id="shape22-52">
		<rect class="cls-4" x="481.06" y="141" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(496.24 159.47) scale(1.09 1)">……</text>
	</g>
	<g id="shape23-55">
		<rect class="cls-7" x="256.07" y="253.78" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(271.25 272.26) scale(1.09 1)">……</text>
	</g>
	<g id="shape24-58">
		<rect class="cls-5" x="481.06" y="206.14" width="61.71" height="28.32"/>
		<text class="cls-2" transform="translate(496.24 224.61) scale(1.09 1)">……</text>
	</g>
	<line class="cls-8" x1="29.69" y1="50.04" x2="35.69" y2="50.04"/>
	<line class="cls-9" x1="47.85" y1="50.04" x2="722.93" y2="50.04"/>
	<line class="cls-8" x1="729.01" y1="50.04" x2="735.01" y2="50.04"/>
	<line class="cls-8" x1="29.69" y1="118.09" x2="35.69" y2="118.09"/>
	<line class="cls-9" x1="47.85" y1="118.09" x2="722.93" y2="118.09"/>
	<line class="cls-8" x1="729.01" y1="118.09" x2="735.01" y2="118.09"/>
	<line class="cls-8" x1="29.69" y1="177.25" x2="35.69" y2="177.25"/>
	<line class="cls-9" x1="47.85" y1="177.25" x2="722.93" y2="177.25"/>
	<line class="cls-8" x1="729.01" y1="177.25" x2="735.01" y2="177.25"/>
	<line class="cls-8" x1="29.69" y1="245" x2="35.69" y2="245"/>
	<line class="cls-9" x1="47.85" y1="245" x2="722.93" y2="245"/>
	<line class="cls-8" x1="729.01" y1="245" x2="735.01" y2="245"/>
	<text class="cls-10" transform="translate(65.75 28.88) scale(1.09 1)">顶层</text>
	<text class="cls-10" transform="translate(65.75 97.79) scale(1.09 1)">功能组</text>
	<text class="cls-10" transform="translate(65.75 159.16) scale(1.09 1)">功能</text>
	<text class="cls-10" transform="translate(65.75 224.3) scale(1.09 1)">子功能</text>
</svg>

## 文件组织

&emsp; &emsp; 库内所有文件的组织形式和功能如下：

::: theorem 

- **algorithm** *&emsp;&emsp; &emsp;&emsp; == **基础算法（内部调用）***
	* calindex *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 指数运算，index 调用的遥感、气象指数运算相关算法*
	* dataio *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 数据读写操作*
	* dem *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== DEM 分析，raa 调用的 DEM 算法*
	* formatio *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 栅格 / 矢量驱动格式控制*
	* interact *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 系统交互，osf 调用的算法*
	* mathematics *&emsp;&emsp; &emsp;&emsp; ==== 数学运算，math 调用的栅格处理算法* 
	* miscellaneous *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 杂项计算，smc 调用的算法*
	* raster *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 基础栅格处理算法， rasp 调用的栅格处理算法* 
	* vector *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 基础矢量处理算法，vesp 调用的矢量处理算法*
- **configure** *&emsp;&emsp; &emsp;&emsp; ==  **配置数据***
- **extend** *&emsp;&emsp; &emsp;&emsp; ==  **扩展功能***
- **relation** *&emsp;&emsp; &emsp;&emsp; ==  **关联参数和函数***
	* [**constants**](Default.html#常量单位)  *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 常量名称、值或与国际单位的代换值*
	* driver *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 驱动格式支持信息*
	* initialize *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 初始化输入参数，错误检查*
	* [**key**](Default.html#默认参数) *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 栅格 / 矢量 处理的其他参数，例如**压缩**，**超大 TIFF 支持**等*
- [**config**](/UserGuide/Function.html#高级配置) *&emsp;&emsp; &emsp;&emsp; == **高级配置**参数*
- [**index**](/UserGuide/Function.html#指数运算) *&emsp;&emsp; &emsp;&emsp; == **指数运算**函数包*
- [**math**](/UserGuide/Function.html#数学运算) *&emsp;&emsp; &emsp;&emsp; == **数学运算**函数包*
- [**osf**](/UserGuide/Function.html#系统交互) *&emsp;&emsp;&emsp; &emsp;&emsp; == **系统交互**操作*
- [**smc**](/UserGuide/Function.html#空间杂项) *&emsp;&emsp;&emsp; &emsp;&emsp; == **空间杂项**计算*
- [**rasp**](/UserGuide/Function.html#栅格处理) *&emsp;&emsp; &emsp;&emsp; == **栅格处理**函数包*
- [**raa**](/UserGuide/Function.html#栅格分析) *&emsp;&emsp; &emsp;&emsp; == **栅格分析**函数包*
- [**vesp**](/UserGuide/Function.html#矢量处理) *&emsp;&emsp; &emsp;&emsp; == **矢量处理**函数包*

:::

