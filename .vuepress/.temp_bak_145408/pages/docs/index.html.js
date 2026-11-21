import comp from "D:/github/gma/.vuepress/.temp/pages/docs/index.html.vue"
const data = JSON.parse("{\"path\":\"/docs/\",\"title\":\"\",\"lang\":\"en-US\",\"frontmatter\":{\"home\":true,\"modules\":[\"BannerBrand\",\"Features\",\"MdContent\",\"Footer\"],\"bannerBrand\":{\"bgImage\":\"/bg.svg\",\"title\":\"GMA for Python\",\"description\":\"Geographic and Meteorological Analysis, gma\",\"tagline\":\"A Python package for rapid processing, analysis, and cartographic visualization of geospatial and meteorological data.\",\"buttons\":[{\"text\":\"Explore Latest → gma 3.0.3\",\"link\":\"/docs/Introduce.html#included-features\"},{\"text\":\"Learn GMA\",\"link\":\"/docs/Introduce\",\"type\":\"plain\"}]},\"features\":[{\"title\":\"User-Friendly First\",\"details\":\"Built on Python, with a clear guide for quick start.\"},{\"title\":\"Open and Shared\",\"details\":\"Over 100 functions are available for open use.\"},{\"title\":\"Efficient Updates\",\"details\":\"Continuously optimized for peak performance.\"}],\"footer\":{\"startYear\":2022}},\"headers\":[{\"level\":2,\"title\":\"Quick Start\",\"slug\":\"quick-start\",\"link\":\"#quick-start\",\"children\":[{\"level\":3,\"title\":\"Install（bash）\",\"slug\":\"install-bash\",\"link\":\"#install-bash\",\"children\":[]},{\"level\":3,\"title\":\"Import（IDE）\",\"slug\":\"import-ide\",\"link\":\"#import-ide\",\"children\":[]},{\"level\":3,\"title\":\"Plotting (Example)\",\"slug\":\"plotting-example\",\"link\":\"#plotting-example\",\"children\":[]}]}],\"git\":{\"createdTime\":1644595903000,\"updatedTime\":1786769004000,\"contributors\":[{\"name\":\"LiChongrui\",\"email\":\"858998723@qq.com\",\"commits\":12},{\"name\":\"lichongrui\",\"email\":\"858998723@qq.com\",\"commits\":2}]},\"filePathRelative\":\"docs/README.md\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
