import type { ComputedRef } from "vue";
import type { SocialLink } from "../../../types/page.js";
export declare function useSocialLinks(): {
    socialLinks: ComputedRef<Array<SocialLink>>;
    jumpSocialLink: (link?: string) => void;
};
