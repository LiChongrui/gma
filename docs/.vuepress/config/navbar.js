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
        //link: '/UserGuide/'
         items: [
            { 
                text: '使用说明', 
                items: [
                    {text: '统计总览', link: '/UserGuide/Instructions/Overview'},
                    {text: '函数列表', link: '/UserGuide/Instructions/Function'}
                ],
            },
            { 
                text: '帮助与示例', 
                items: [
                    {text: '指数运算', link: '/UserGuide/index/EVI'},
                    {text: '数学运算', link: '/UserGuide/math/FillNoData'},
                    {text: '系统交互', link: '/UserGuide/osf/DateSeries'},
                    {text: '空间杂项', link: '/UserGuide/smc/CALDistance'},
                    {text: '栅格处理', link: '/UserGuide/rasp/AddColorTable'},
                    {text: '栅格分析', link: '/UserGuide/raa/DEM/Aspect'},
                    {text: '矢量处理', link: '/UserGuide/vesp/Check'},
                    {text: '高级配置', link: '/UserGuide/config/GetRACreationOption'},
                    {text: '其他函数', link: '/UserGuide/other/Open'},
                ],
            },
         ]
    },

    {
        text: '更新记录',
        icon: "fas fa-arrow-up",
        items: [
            { text: '更新日志', link: '/Update/log/1.0.9'},
            { text: '更新预览', link: "/Update/Plan" },
         ]
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