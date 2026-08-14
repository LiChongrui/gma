module.exports = [  
    //{ text: '首页', link: '/', icon: "fas fa-house-user" },

    { 
        text: 'Introduce', 
        icon: "fab fa-stumbleupon-circle",
        link:'/Introduce.md',
    },

    { 
        text: 'Install', 
        icon: "fab fa-instalod",
        link:"/Install.md"
    },

    // {
    //     text: '功能探索',
    //     icon: "fas fa-toolbox",
    //     link: '/Explore/'
    // },

    {
        text: 'User Guide',
        icon: "fa-brands fa-yelp",
        items: [
            {text: 'climet', link: '/UserGuide/climet/'},
            {text: 'rsvi', link: '/UserGuide/rsvi/'},
            {text: 'math', link: '/UserGuide/math/'},
            {text: 'crs', link: '/UserGuide/crs/'},
            {text: 'driver', link: '/UserGuide/driver/'},
            {text: 'gio', link: '/UserGuide/gio/'},
            {text: 'smc', link: '/UserGuide/smc/'},
            {text: 'etools', link: '/UserGuide/etools/'},
            {text: 'const', link: '/UserGuide/const/'},
         ]
    },

    {
        text: 'Release Notes',
        icon: "fas fa-arrow-up",
        link: '/Update/'
    },
    {
        text: 'Support',
        icon: "fa-solid fa-paper-plane",
        link: '/Support/'
    },

]