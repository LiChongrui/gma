module.exports = {


    '/Explore/': [
        {
            title:'组织说明',
            collapsable: false,
            children: [
                '',
                'Structure',
                'Default',
                'Constants',
                'Naming',
            ]
        },
        {
            title:'应用探索',
            collapsable: false,
            children: [
                'RasterOperation',
                'VectorOperation',
            ]
        },
    ],

    '/UserGuide/Instructions/': [
        {
            title:'使用说明',
            collapsable: false,
            children: [
                '/UserGuide/Instructions/Overview',
                '/UserGuide/Instructions/Function'
            ]
        }
    ],

    '/UserGuide/climet/': [
        {
            title: '气候气象',
            collapsable: false,
            children: [
                '/UserGuide/climet/SPEI',
                '/UserGuide/climet/SPI',
                '/UserGuide/climet/PAP',
                '/UserGuide/climet/MKMutationTest',
                {
                    title: 'ET0',
                    collapsable: false,
                    children: [
                        '/UserGuide/climet/ET0/Hargreaves',
                        '/UserGuide/climet/ET0/PenmanMonteith',
                        '/UserGuide/climet/ET0/Thornthwaite',

                    ]
                },
                {
                    title: 'Other',
                    collapsable: false,
                    children: [
                        '/UserGuide/climet/Other/DaylightHours',
                        '/UserGuide/climet/Other/Declination',
                        '/UserGuide/climet/Other/HourAngle',
                        '/UserGuide/climet/Other/RDBSunAndEarth',
                        '/UserGuide/climet/Other/SolarRadiationFluxOA'
                    ]
                },
            ],
        }
    ],

    '/UserGuide/rsvi/': [
        {
            title: '遥感指数',
            collapsable: false,
            children: [
                '/UserGuide/rsvi/EVI',
                '/UserGuide/rsvi/NDBI',
                '/UserGuide/rsvi/NDWI',
                '/UserGuide/rsvi/NDVI',
                '/UserGuide/rsvi/TVDI',
            ],
        }
    ],
       
    '/UserGuide/math/': [
        {
            title: '数学运算',
            collapsable: false,
            children: [
                '/UserGuide/math/FillNoData',
                '/UserGuide/math/ToNumericArray',
                {
                    title: 'Smooth',
                    collapsable: false,
                    children: [
                        '/UserGuide/math/Smooth/',
                        '/UserGuide/math/Smooth/MovingAverage',
                        '/UserGuide/math/Smooth/SavitzkyGolay',
                    ]
                },
                {
                    title: 'Evaluation',
                    collapsable: false,
                    children: [
                        '/UserGuide/math/Evaluation/',
                        '/UserGuide/math/Evaluation/CORR',
                        '/UserGuide/math/Evaluation/D',
                        '/UserGuide/math/Evaluation/MaxAE',
                        '/UserGuide/math/Evaluation/Methods',
                        '/UserGuide/math/Evaluation/NRMSE',
                        '/UserGuide/math/Evaluation/R2',
                        '/UserGuide/math/Evaluation/RMSE',
                        '/UserGuide/math/Evaluation/Select',
                    ]
                },
                {
                    title: 'Kernel',
                    collapsable: false,
                    children: [
                        '/UserGuide/math/Kernel/Aggregate',
                        '/UserGuide/math/Kernel/GaussFilter',
                        '/UserGuide/math/Kernel/GeneralFilter',
                    ]
                }
            ]
        }
    ],

    '/UserGuide/osf/': [
        {
            title: '系统交互',
            collapsable: false,
            children: [
                '/UserGuide/osf/DateSeries',
                '/UserGuide/osf/GetPath',
                '/UserGuide/osf/MultiThreading',
                '/UserGuide/osf/UnZip',
                '/UserGuide/osf/Zip',
                {
                    title: 'Rename',
                    collapsable: false,
                    children: [
                        '/UserGuide/osf/Rename/',
                        '/UserGuide/osf/Rename/Intercept',
                        '/UserGuide/osf/Rename/Modify',
                        '/UserGuide/osf/Rename/Replace',
                    ]
                }
            ]
        }
    ],
    '/UserGuide/smc/': [
        {
            title: '空间杂项',
            collapsable: false,
            children: [
                '/UserGuide/smc/CALDistance',
                '/UserGuide/smc/TRANCoordinate',
            ]
        }
    ],
    '/UserGuide/rasp/': [
        {
            title: '栅格处理',
            collapsable: false,
            children: [
                '/UserGuide/rasp/AddColorTable',
                '/UserGuide/rasp/BandDecomposition',
                '/UserGuide/rasp/BandSynthesis',
                '/UserGuide/rasp/ChangeDataType',
                '/UserGuide/rasp/Clip',
                '/UserGuide/rasp/Deformation',
                '/UserGuide/rasp/GenerateOVR',
                '/UserGuide/rasp/Mosaic',
                '/UserGuide/rasp/MultiSDSToTif',
                '/UserGuide/rasp/OrthophotoCorrection',
                '/UserGuide/rasp/Reproject',
                '/UserGuide/rasp/Resample',
                '/UserGuide/rasp/SplitImage',
                '/UserGuide/rasp/ToOtherFormat',
                '/UserGuide/rasp/ToVector',
                '/UserGuide/rasp/WriteRaster',
                {
                    title: 'Fusion',
                    collapsable: false,
                    children: [
                        '/UserGuide/rasp/Fusion/Pansharpen',
                    ]
                }
            ]
        }
    ],
    '/UserGuide/raa/': [
        {
            title: '栅格分析',
            collapsable: false,
            children: [
                {
                    title: 'DEM',
                    collapsable: false,
                    children: [
                        '/UserGuide/raa/DEM/Aspect',
                        '/UserGuide/raa/DEM/HillShade',
                        '/UserGuide/raa/DEM/Roughness',
                        '/UserGuide/raa/DEM/Slope',
                        '/UserGuide/raa/DEM/TPI',
                    ]
                },
                {
                    title: 'Kernel',
                    collapsable: false,
                    children: [
                        '/UserGuide/raa/Kernel/Aggregate',
                        '/UserGuide/raa/Kernel/GeneralFilter',   
                        '/UserGuide/raa/Kernel/GaussFilter',   
                    ]
                }, 
                {
                    title: 'Extraction',
                    collapsable: false,
                    children: [
                        '/UserGuide/raa/Extraction/Isopleth',
                    ]
                }, 
            ]
        }
    ],
    '/UserGuide/vesp/': [
        {
            title: '矢量处理',
            collapsable: false,
            children: [
                '/UserGuide/vesp/Check',
                '/UserGuide/vesp/Clip',
                '/UserGuide/vesp/Erase',
                '/UserGuide/vesp/FixGeometry',
                '/UserGuide/vesp/Intersection',
                '/UserGuide/vesp/Reproject',
                '/UserGuide/vesp/Simplify',
                '/UserGuide/vesp/Split',
                '/UserGuide/vesp/SymDifference',
                '/UserGuide/vesp/ToOtherFormat',
                '/UserGuide/vesp/ToRaster',
                '/UserGuide/vesp/Union',
                '/UserGuide/vesp/Update',
            ]
        }
    ],
    '/UserGuide/config/': [
        {
            title: '高级配置',
            collapsable: false,
            children: [
                '/UserGuide/config/GetRACreationOption',
                '/UserGuide/config/GetRasterFormat',
                '/UserGuide/config/GetVectorFormat',
                '/UserGuide/config/GetVELayerCreationOption',
                '/UserGuide/config/RasterFormatInfo',
                '/UserGuide/config/VectorFormatInfo',
            ]
        }
    ],
    '/UserGuide/other/': [
        {
            title: '其他函数',
            collapsable: false,
            children: [
                '/UserGuide/other/Open',
                '/UserGuide/other/RasterOpen',
                '/UserGuide/other/VectorOpen',
                '/UserGuide/other/Layer',
            ]
        },
    ],
    '/Update/log/': [
        {
            title:'更新日志',
            collapsable: false,
            children: [
                '1.0.12',
                '1.0.11',
                '1.0.10',
                '1.0.9',
                '1.0.8',
                '1.0.7',
                '1.0.6',
                '1.0.5',
                '1.0.4',
                '1.0.3',
                '1.0.2',
                '1.0.1',
                '1.0.0',
            ]
        }
    ],

}