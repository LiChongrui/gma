import { ref, computed } from 'vue';
import { useSeriesItems } from './index.js';
const isOpenSeries = ref(false);
export const useSeriesData = () => {
    const seriesItems = useSeriesItems();
    const isShowSeries = computed(() => seriesItems.value.length > 0 && isOpenSeries);
    const toggleSeries = (to) => {
        isOpenSeries.value = typeof to === 'boolean' ? to : !isOpenSeries.value;
        document.body.style.overflowY = isOpenSeries.value ? 'hidden' : 'auto';
    };
    return { isOpenSeries, isShowSeries, toggleSeries };
};
