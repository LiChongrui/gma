import { computed } from 'vue';
import { useRoute, usePageFrontmatter } from 'vuepress/client';
import { isPlainObject, isString, resolveLocalePath } from 'vuepress/shared';
import { useExtendPageData } from '@vuepress-reco/vuepress-plugin-page/composables';
import { useSortSeries, useThemeLocaleData } from '@composables/index.js';
import { getNavLink } from './getNavLink.js';
export const useSeriesItems = () => {
    const route = useRoute();
    const { series } = useExtendPageData();
    const themeLocal = useThemeLocaleData();
    const frontmatter = usePageFrontmatter();
    const seriesItems = computed(() => resolveSeriesItems(frontmatter.value, themeLocal.value, route, series));
    if (!seriesItems) {
        throw new Error('useSeriesItems() is called without provider.');
    }
    return seriesItems;
};
const resolveSeriesItems = (frontmatter, themeLocal, route, autoSeries) => {
    const { sortSeries } = useSortSeries();
    // get series config from frontmatter > themeConfig
    let seriesConfig = themeLocal.series ?? {};
    Object.keys(autoSeries).forEach(key => {
        autoSeries[key] = sortSeries(autoSeries[key]);
    });
    seriesConfig = {
        ...seriesConfig,
        ...autoSeries,
    };
    // 解决
    // resolve series items according to the config
    if (frontmatter.home) {
        return [];
    }
    if (isPlainObject(seriesConfig)) {
        return resolveMultiSeriesItems(seriesConfig, route);
    }
    return [];
};
/**
 * Resolve series items if the config is an array
 */
const resolveArraySeriesItems = (seriesPath, seriesConfig) => {
    return seriesConfig.map((item) => {
        if (isString(item)) {
            const link = item.includes(seriesPath) ? item : `${seriesPath}${item}`;
            return getNavLink(link);
        }
        const resolvedItem = { ...item };
        // @ts-ignore
        if (item.children) {
            // @ts-ignore
            resolvedItem.children = resolveArraySeriesItems(seriesPath, item.children);
        }
        // @ts-ignore
        return resolvedItem;
    });
};
/**
 * Resolve series items if the config is a key -> value (path-prefix -> array) object
 */
const resolveMultiSeriesItems = (seriesConfig, route) => {
    const seriesPath = resolveLocalePath(seriesConfig, decodeURIComponent(route.path));
    const matchedSeriesConfig = seriesConfig[seriesPath] ?? [];
    return resolveArraySeriesItems(seriesPath, matchedSeriesConfig);
};
