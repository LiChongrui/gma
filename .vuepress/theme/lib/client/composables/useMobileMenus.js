import { ref } from 'vue';
const isOpenMobileMenus = ref(false);
export const useMobileMenus = () => {
    const toggleMobileMenus = (to) => {
        isOpenMobileMenus.value = typeof to === 'boolean' ? to : !isOpenMobileMenus.value;
        document.body.style.overflowY = isOpenMobileMenus.value ? 'hidden' : 'auto';
    };
    return { isOpenMobileMenus, toggleMobileMenus };
};
