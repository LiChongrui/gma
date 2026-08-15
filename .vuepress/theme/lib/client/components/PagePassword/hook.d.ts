export declare function usePageInfo(): {
    pagePassword: import("vue").ComputedRef<string[]>;
};
export declare function useHandlePassword(pagePassword: any, emit: any): {
    password: import("vue").Ref<string, string>;
    passwordRef: import("vue").Ref<null, null>;
    lockIcon: import("vue").Ref<string, string>;
    lockText: import("vue").Ref<string, string>;
    focus: () => void;
};
