export declare function useFriendshipLink(): {
    friendshipLinks: import("vue").ComputedRef<{
        logo: string;
        link: string;
        title: string;
    }[]>;
    handlClick: (link: string) => void;
};
