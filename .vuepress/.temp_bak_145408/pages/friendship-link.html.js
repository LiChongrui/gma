import comp from "D:/github/gma/.vuepress/.temp/pages/friendship-link.html.vue"
const data = JSON.parse("{\"path\":\"/friendship-link.html\",\"title\":\"\",\"lang\":\"en-US\",\"frontmatter\":{\"layout\":\"FriendshipLink\"},\"headers\":[],\"git\":{},\"filePathRelative\":null}")
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
