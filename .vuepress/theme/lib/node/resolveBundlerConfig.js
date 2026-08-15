import tailwindcss from 'tailwindcss';
import { path } from 'vuepress/utils';
import postcssEach from 'postcss-each';
import autoprefixer from 'autoprefixer';
import postcssImport from 'postcss-import';
import tailwindcssNesting from 'tailwindcss/nesting/index.js';
import { tailwindcssConfig } from '@vuepress-reco/tailwindcss-config';
// The bundlers for vuepress
import { viteBundler } from '@vuepress/bundler-vite';
import { webpackBundler } from '@vuepress/bundler-webpack';
export function injectiBuilderOptionsOfRecoTheme(app, themeConfig) {
    _customizeTailwindcssOptions(themeConfig);
    if (app.options.bundler.name === '@vuepress/bundler-vite') {
        const viteBundlerOptions = _getViteBundlerOptions(themeConfig);
        app.options.bundler = viteBundler(viteBundlerOptions);
    }
    else {
        const viteBundlerOptions = _getWebpackBundlerOptions(themeConfig);
        app.options.bundler = webpackBundler(viteBundlerOptions);
    }
}
const postcssPlugins = {
    plugins: [
        postcssImport,
        tailwindcssNesting,
        tailwindcss(tailwindcssConfig),
        autoprefixer({}),
        postcssEach,
    ],
};
let viteBundlerOptions = null;
const _getViteBundlerOptions = (themeConfig) => {
    if (viteBundlerOptions)
        return viteBundlerOptions;
    const userConfig = themeConfig?.viteBundlerOptions || {};
    const defaultConfig = {
        viteOptions: { css: { postcss: { ...postcssPlugins } } },
    };
    viteBundlerOptions = _mergeConfig(userConfig, defaultConfig);
    return viteBundlerOptions;
};
let webpackBundlerOptions = null;
const _getWebpackBundlerOptions = (themeConfig) => {
    if (webpackBundlerOptions)
        return webpackBundlerOptions;
    const userConfig = themeConfig?.webpackBundlerOptions || {};
    const defaultConfig = {
        chainWebpack: (config) => {
            config.resolve.extensions.merge(['.js', '.vue']).end();
        },
        postcss: {
            postcssOptions: { ...postcssPlugins },
        },
    };
    webpackBundlerOptions = _mergeConfig(userConfig, defaultConfig);
    return webpackBundlerOptions;
};
function _customizeTailwindcssOptions(themeConfig) {
    if (themeConfig?.primaryColor) {
        tailwindcssConfig.theme.extend.colors.reco.primary = themeConfig.primaryColor;
    }
    tailwindcssConfig.content.push(path.join(themeConfig?.docsDir || '/', './.vuepress/components/*.(vue|html|js)'));
}
function _mergeConfig(userConfig, defaultConfig) {
    const mergedConfig = { ...defaultConfig };
    for (const key in userConfig) {
        if (typeof userConfig[key] === 'object' &&
            typeof mergedConfig[key] === 'object') {
            mergedConfig[key] = _mergeConfig(userConfig[key], mergedConfig[key]);
        }
        else {
            mergedConfig[key] = userConfig[key];
        }
    }
    return mergedConfig;
}
