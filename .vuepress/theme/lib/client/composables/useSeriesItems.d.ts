import type { ComputedRef } from 'vue';
import type { ResolvedSeriesItem } from '../../types';
export type SeriesItemsRef = ComputedRef<ResolvedSeriesItem[]>;
export declare const useSeriesItems: () => SeriesItemsRef;
