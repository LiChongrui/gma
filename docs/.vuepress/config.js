
module.exports = {
    locales: {
        '/': {
            lang: 'zh-CN'
        }
    },
    //,'/en/': { lang: 'en-US', },  },
    port: '9000', // 本地端口
    markdown:{
        lineNumbers: true
    },
    base: '/',
    head: [
        ['link', { rel: 'icon', href: '/images/Logo-gma.svg' }]
    ],
    title: '地理与气象分析库',
    theme: require.resolve('../../theme-reco'),
    themeConfig: {
        //导航栏logo
        logo: '/images/Logo-gma.svg',
        author: '洛',
        //type: 'blog',
        authorAvatar: '/images/Luo.jpg',

        displayAllHeaders: true,
        subSidebar: 'auto',
        sidebarDepth: 4,

        locales: {
            '/': {

                modePicker: true,
                nav: require('./config/navbar.js'),
                // 侧边栏
                sidebar: require('./config/sidebar.js'),

                //lastUpdated: '最近更新', 
                smoothScroll: true,

                startYear: 2021,
                showAccessNumber: true,
                //codeTheme: 'tomorrow',//'solarizedlight', 'funky','okaidia', 'tomorrow'
            },
        },
    },
    plugins: [
         [
             'vuepress-plugin-mermaidjs',{
                 //gantt: { barHeight: 40, fontSize:30, titleTopMargin:25, barGap:4, topPadding:75, sidePadding:75}
             }        
         ],
         'vuepress-plugin-boxx',
         'vuepress-plugin-mathjax'
    ]

}  