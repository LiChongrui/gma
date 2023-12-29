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
                    {text: '简易说明', link: '/UserGuide/Instructions/Overview'},
                    {text: '函数总览', link: '/UserGuide/Instructions/Function'}
                ],
            },
            { 
                text: '帮助与示例', 
                items: [
                    {text: '气候气象-climet', link: '/UserGuide/climet/'},
                    {text: '遥感指数-rsvi', link: '/UserGuide/rsvi/EVI'},
                    {text: '数学运算-math', link: '/UserGuide/math/'},
                    {text: '系统交互-osf', link: '/UserGuide/osf/DateSeries'},
                    {text: '空间杂项-smc', link: '/UserGuide/smc/'},
                    {text: '栅格处理-rasp', link: '/UserGuide/rasp/'},
                    {text: '矢量处理-vesp', link: '/UserGuide/vesp/'},
                    {text: '地图工具-map', link: '/UserGuide/map/plot/MapFrame/'},
                    {text: '地理驱动-gft', link: '/UserGuide/gft/GetRasterFormat'},
                    {text: '输入输出-io', link: '/UserGuide/io/'},
                    {text: '空间参考-crs', link: '/UserGuide/crs/'},
                ],
            },
         ]
    },

    {
        text: '更新日志',
        icon: "fas fa-arrow-up",
        link: '/Update/log/2.0/2.0.4'
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