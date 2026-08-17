import { defineUserConfig } from "vuepress";
import recoTheme from "./theme"; // 自定义主题
import { viteBundler } from '@vuepress/bundler-vite'
//import { webpackBundler } from '@vuepress/bundler-webpack'

export default defineUserConfig({
  bundler: viteBundler(),
  locales: {
    '/': {
      lang: 'en-US', 
      title: "GMA for Python",
      description: "Geographic and Meteorological Analysis",
    },
  },
  // bundler: webpackBundler(),
  
  theme: recoTheme({
    locales: {
      '/': {
        selectLanguageName: 'English',
        logo: "/logo.svg",
        author: "Luo_Suppe",
        authorAvatar: "/Luo.jpg",
        
        // docsBranch: "main",
        // docsDir: "example",
        // lastUpdatedText: "",
        // series 为原 sidebar
        
        series: require('./config/sidebar.js'),
        navbar: require('./config/navbar.js'),
        bulletin: require('./config/bulletin.js'),
      },
    },
  }),
});
