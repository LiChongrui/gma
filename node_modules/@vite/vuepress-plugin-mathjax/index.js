const fs = require('fs');
const path = require('path');
const mk = require('@iktakahiro/markdown-it-katex');

module.exports = (options, ctx) => {
  const mathjaxStylePath = path.resolve(ctx.tempPath, 'plugins-mathjax.css')

  return {
    async ready() {
      options = Object.assign({
        mathjax: options.mathjax || {}
      }, options);
      fs.writeFileSync(mathjaxStylePath, "@import 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.css'\n");
    },
    extendMarkdown: md => {
      md.use(mk)
    },
    enhanceAppFiles: [
      {
        name: 'mathjaxClient',
        content: `
          import '${mathjaxStylePath}'
          export default ({Vue, options, router, siteData}) => {
            // Ignore mathjax element
            Vue.config.ignoredElements = [
              /^mjx-/
            ]
          }
        `
      }
    ]
  }
}
