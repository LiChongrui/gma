import { defineAsyncComponent } from 'vue'

export default {
  enhance: ({ app }) => {    
      app.component("enhancement", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/enhancement.vue")))
    
      app.component("fix", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/fix.vue")))
    
      app.component("install", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/install.vue")))
    
      app.component("introduce", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/introduce.vue")))
    
      app.component("issues", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/issues.vue")))
    
      app.component("new", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/new.vue")))
    
      app.component("osgeo", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/osgeo.vue")))
    
      app.component("removal", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/removal.vue")))
    
      app.component("support", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/support.vue")))
    
      app.component("update", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/update.vue")))
    
      app.component("use-guide", defineAsyncComponent(() => import("D:/github/gma/.vuepress/components/use-guide.vue")))
  },
}
