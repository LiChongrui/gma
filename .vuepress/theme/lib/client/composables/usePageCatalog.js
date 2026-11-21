import { computed, inject } from 'vue';
import { usePageFrontmatter } from 'vuepress/client';
export const catalogSymbol = Symbol('catalog');
export const usePageCatalog = () => {
    const frontmatter = usePageFrontmatter();
    const catalog = inject(catalogSymbol);
    if (!catalog) {
        throw new Error('usePageCatalog() is called without provider.');
    }
    const isShowCatalog = computed(() => catalog.value.length > 0 && frontmatter.value.home !== true);
    return { catalog, isShowCatalog };
};
const stripSigArgs = (title) => {
    // 成员头一行化后标题为 name(args)；目录只显示方法名，锚点 slug 不受影响
    const i = title.indexOf('(');
    return i > 0 ? title.slice(0, i).trim() : title;
};
const headerToCatalogItem = (header) => ({
    text: stripSigArgs(header.title),
    link: `#${header.slug}`,
    level: header.level,
    children: headersToCatalog(header.children),
});
export const headersToCatalog = (headers) => headers.map((header) => headerToCatalogItem(header));
