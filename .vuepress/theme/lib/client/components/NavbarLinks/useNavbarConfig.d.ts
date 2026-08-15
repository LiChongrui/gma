import type { MenuLink, MenuGroup, MenuLinkGroup } from '../../../types';
import { ComputedRef } from 'vue';
export declare const useNavbarConfig: () => ComputedRef<Array<MenuLink | MenuGroup<MenuLinkGroup>>>;
