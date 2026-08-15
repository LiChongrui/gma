import { PageDataRef, PageFrontmatterRef } from 'vuepress/client';
import type { RecoThemePageData, RecoThemeNormalPageFrontmatter } from '../../types';
export declare const usePageData: () => PageDataRef<RecoThemePageData>;
export declare const usePageFrontmatter: () => PageFrontmatterRef<RecoThemeNormalPageFrontmatter>;
