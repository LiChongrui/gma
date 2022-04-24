module.exports = [  
    //{ text: '首页', link: '/', icon: "fas fa-house-user" },

    { 
        text: '简介', 
        icon: "fab fa-stumbleupon-circle",
        link:'/Introduce.md',
    },

    { 
        text: '快速安装', 
        icon: "fab fa-instalod",
        link:"/Install.md"
    },

    {
        text: '功能探索',
        icon: "fas fa-toolbox",
        link: '/Explore/'
    },

    {
        text: '使用指南',
        icon: "fa-brands fa-yelp",
        link: '/UserGuide/'
    },

    {
        text: '更新记录',
        icon: "fas fa-arrow-up",
        link: '/Update/'
    },

    {
        text: '支持',
        icon: "fa-solid fa-paper-plane",
        items: [
            { text: '研学分享', link: "https://luosgeo.com" },
            { text: '反馈与赞助', link: "/Support" },
         ]
    },

]