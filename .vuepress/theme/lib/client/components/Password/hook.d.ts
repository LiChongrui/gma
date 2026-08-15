import type { ComputedRef, Ref } from 'vue';
export declare function useSiteInfo(): {
    siteBrandLogo: ComputedRef<string | null | undefined>;
    siteBrandTitle: ComputedRef<string>;
    sitePassword: ComputedRef<string[]>;
};
export declare function useHandlePassword(sitePassword: ComputedRef<string[]>, emit: any): {
    lockIcon: Ref<any>;
    password: Ref<string>;
    passwordRef: Ref<any>;
    lockText: Ref<string>;
    focus: () => void;
};
