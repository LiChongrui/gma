import comp from "D:/github/gma/.vuepress/.temp/pages/docs/Introduce.html.vue"
const data = JSON.parse("{\"path\":\"/docs/Introduce.html\",\"title\":\"Introduce\",\"lang\":\"en-US\",\"frontmatter\":{\"title\":\"Introduce\",\"date\":\"2023-08-20T00:00:00.000Z\",\"subSidebar\":false},\"headers\":[{\"level\":2,\"title\":\"Included Features\",\"slug\":\"included-features\",\"link\":\"#included-features\",\"children\":[]},{\"level\":2,\"title\":\"Original Intent\",\"slug\":\"original-intent\",\"link\":\"#original-intent\",\"children\":[]}],\"git\":{\"createdTime\":1644595903000,\"updatedTime\":1786813176000,\"contributors\":[{\"name\":\"LiChongrui\",\"email\":\"858998723@qq.com\",\"commits\":10},{\"name\":\"lichongrui\",\"email\":\"858998723@qq.com\",\"commits\":2}]},\"filePathRelative\":\"docs/Introduce.md\"}")
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
