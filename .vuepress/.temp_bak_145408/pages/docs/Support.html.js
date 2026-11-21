import comp from "D:/github/gma/.vuepress/.temp/pages/docs/Support.html.vue"
const data = JSON.parse("{\"path\":\"/docs/Support.html\",\"title\":\"Support\",\"lang\":\"en-US\",\"frontmatter\":{\"sidebar\":false,\"title\":\"Support\"},\"headers\":[{\"level\":2,\"title\":\"Feedback\",\"slug\":\"feedback\",\"link\":\"#feedback\",\"children\":[]},{\"level\":2,\"title\":\"Sponsor\",\"slug\":\"sponsor\",\"link\":\"#sponsor\",\"children\":[]}],\"git\":{\"createdTime\":1644777270000,\"updatedTime\":1786772306000,\"contributors\":[{\"name\":\"LiChongrui\",\"email\":\"858998723@qq.com\",\"commits\":8},{\"name\":\"lichongrui\",\"email\":\"858998723@qq.com\",\"commits\":1}]},\"filePathRelative\":\"docs/Support.md\"}")
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
