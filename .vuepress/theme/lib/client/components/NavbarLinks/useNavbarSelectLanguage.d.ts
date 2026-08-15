import { ComputedRef } from 'vue';
import type { MenuLink, MenuGroup } from '../../../types';
/**
 * Get navbar config of select language dropdown
 */
export declare const useNavbarSelectLanguage: () => ComputedRef<MenuGroup<MenuLink> | null>;
