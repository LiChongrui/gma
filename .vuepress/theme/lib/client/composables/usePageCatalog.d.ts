import type { PageHeader } from 'vuepress/client';
import type { ComputedRef, InjectionKey } from 'vue';
export interface ResolvedPageCatalog {
    [prop: string]: any;
}
export type CatalogRef = ComputedRef<ResolvedPageCatalog[]>;
export declare const catalogSymbol: InjectionKey<CatalogRef>;
export declare const usePageCatalog: () => {
    catalog: CatalogRef;
    isShowCatalog: ComputedRef<boolean>;
};
export declare const headersToCatalog: (headers: PageHeader[]) => ResolvedPageCatalog[];
