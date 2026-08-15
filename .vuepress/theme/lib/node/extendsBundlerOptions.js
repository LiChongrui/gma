import { addViteConfig, addViteOptimizeDepsExclude, addViteOptimizeDepsInclude, addViteSsrNoExternal, } from "@vuepress/helper";
/**
 * @private
 */
export const extendsBundlerOptions = (bundlerOptions, app) => {
    addViteConfig(bundlerOptions, app, {
        build: {
            chunkSizeWarningLimit: 1024,
        },
    });
    addViteOptimizeDepsInclude(bundlerOptions, app, "@vueuse/core", true);
    addViteOptimizeDepsExclude(bundlerOptions, app, "@theme-reco");
    addViteSsrNoExternal(bundlerOptions, app, [
        "@vuepress/helper",
        "@vuepress/plugin-reading-time",
    ]);
};
