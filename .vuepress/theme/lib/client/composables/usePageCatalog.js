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
const headerToCatalogItem = (header) => ({
    text: header.title,
    link: `#${header.slug}`,
    level: header.level,
    children: headersToCatalog(header.children),
});
export const headersToCatalog = (headers) => headers.map((header) => headerToCatalogItem(header));
