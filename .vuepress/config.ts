import { defineUserConfig } from "vuepress";
import recoTheme from "vuepress-theme-reco";
import { viteBundler } from '@vuepress/bundler-vite'
//import { webpackBundler } from '@vuepress/bundler-webpack'

export default defineUserConfig({
  title: "GMA for Python",
  description: "Geographic and Meteorological Analysis",
  bundler: viteBundler(),
  // bundler: webpackBundler(),
  theme: recoTheme({
    logo: "/logo.svg",
    author: "Luo_Suppe",
    authorAvatar: "/Luo.jpg",

    // docsRepo: "https://github.com/vuepress-reco/vuepress-theme-reco-next",
    // docsBranch: "main",
    // docsDir: "example",
    // lastUpdatedText: "",
    // series 为原 sidebar
    series: require('./config/sidebar.js'),
    navbar: require('./config/navbar.js'),
    bulletin: require('./config/bulletin.js'),
  }),
});
