
  import { defineAsyncComponent } from 'vue'
import { defineClientConfig } from 'vuepress/client'

import { applyClientSetup } from 'D:/github/gma/.vuepress/theme/lib/client/clientSetup.js'
import { applyClientEnhance } from 'D:/github/gma/.vuepress/theme/lib/client/clientEnhance.js'

import * as layouts from 'D:/github/gma/.vuepress/theme/lib/client/layouts/index.js'

  const layoutsFromDir = {}
export default defineClientConfig({
  enhance(...args) {
    applyClientEnhance(...args)
  },
  setup() {
    applyClientSetup()
  },
  // @ts-ignore
  layouts: { ...layouts, ...layoutsFromDir },
})
