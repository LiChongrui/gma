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
                'Overview',
                'Function'
            ]
        }
    ],

    '/UserGuide/climet/': [
        {
            title: '气候气象',
            collapsable: false,
            children: [
                'SPEI',
                'SPI',
                'PAP',
                {
                    title: 'Diagnosis',
                    collapsable: false,
                    children: [
                        'Diagnosis/MKMutationTest',
                        'Diagnosis/Buishand',
                        'Diagnosis/Pettitt',
                        'Diagnosis/SNHT',
                    ]
                },
                {
                    title: 'ET0',
                    collapsable: false,
                    children: [
                        'ET0/Hargreaves',
                        'ET0/PenmanMonteith',
                        'ET0/Thornthwaite',

                    ]
                },
                {
                    title: 'Other',
                    collapsable: false,
                    children: [
                        'Other/DaylightHours',
                        'Other/Declination',
                        'Other/HourAngle',
                        'Other/RDBSunAndEarth',
                        'Other/SolarRadiationFluxOA'
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
                'EVI',
                'NDBI',
                'NDWI',
                'NDVI',
                'TVDI',
            ],
        }
    ],
       
    '/UserGuide/math/': [
        {
            title: '数学运算',
            collapsable: false,
            children: [
                'FillNoData',
                'ToNumericArray',
                {
                    title: 'Smooth',
                    collapsable: false,
                    children: [
                        'Smooth/',
                        'Smooth/MovingAverage',
                        'Smooth/SavitzkyGolay',
                    ]
                },
                {
                    title: 'Evaluation',
                    collapsable: false,
                    children: [
                        'Evaluation/',
                        'Evaluation/CORR',
                        'Evaluation/D',
                        'Evaluation/MaxAE',
                        'Evaluation/Methods',
                        'Evaluation/NRMSE',
                        'Evaluation/R2',
                        'Evaluation/RMSE',
                        'Evaluation/Select',
                    ]
                },
                {
                    title: 'Kernel',
                    collapsable: false,
                    children: [
                        'Kernel/Aggregate',
                        'Kernel/GaussFilter',
                        'Kernel/GeneralFilter',
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
                'DateSeries',
                'GetPath',
                'MultiThreading',
                'UnZip',
                'Zip',
                {
                    title: 'Rename',
                    collapsable: false,
                    children: [
                        'Rename/',
                        'Rename/Intercept',
                        'Rename/Modify',
                        'Rename/Replace',
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
                'CALArea',
                'CALDistance',
                'TRANCoordinate',
                {
                    title: 'Interpolate',
                    collapsable: false,
                    children: [
                        'Interpolate/BSpline',
                        'Interpolate/IDW',
                        'Interpolate/Kriging',
                        'Interpolate/NaturalNeighbor',
                        'Interpolate/Trend',
                    ]
                }
            ]
        }
    ],
    '/UserGuide/rasp/': [
        {
            title: '栅格处理',
            collapsable: false,
            children: [
                'AddColorTable',
                'BandDecomposition',
                'BandSynthesis',
                'ChangeDataType',
                'Clip',
                'Deformation',
                'GenerateOVR',
                'Mosaic',
                'MultiSDSToTif',
                'OrthophotoCorrection',
                'Reproject',
                'Resample',
                'SplitImage',
                'ToOtherFormat',
                'ToVector',
                'WriteRaster',
                {
                    title: 'Fusion',
                    collapsable: false,
                    children: [
                        'Fusion/Pansharpen',
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
                        'DEM/Aspect',
                        'DEM/HillShade',
                        'DEM/Roughness',
                        'DEM/Slope',
                        'DEM/TPI',
                    ]
                },
                {
                    title: 'Kernel',
                    collapsable: false,
                    children: [
                        'Kernel/Aggregate',
                        'Kernel/GeneralFilter',   
                        'Kernel/GaussFilter',   
                    ]
                }, 
                {
                    title: 'Extraction',
                    collapsable: false,
                    children: [
                        'Extraction/Isopleth',
                        'Extraction/Reclassify',
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
                'ChangeGeometryType',
                'Check',
                'Clip',
                'Erase',
                'FixGeometry',
                'Intersection',
                'Reproject',
                'Simplify',
                'Split',
                'SymDifference',
                'ToOtherFormat',
                'ToRaster',
                'Union',
                'Update',
            ]
        }
    ],
    '/UserGuide/config/': [
        {
            title: '高级配置',
            collapsable: false,
            children: [
                'GetRACreationOption',
                'GetRasterFormat',
                'GetVectorFormat',
                'GetVELayerCreationOption',
                'RasterFormatInfo',
                'VectorFormatInfo',
            ]
        }
    ],
    '/UserGuide/other/': [
        {
            title: '其他函数',
            collapsable: false,
            children: [
                'Open',
                'SubDataSet',
                'DataSet',
                'DataSource',
                'Layer',
                'Feature',
            ]
        },
    ],
    '/Update/log/': [
        {
            title:'更新日志',
            collapsable: false,
            children: [
                {
                    title: '1.1 (2023)',
                    collapsable: false,
                    children: [
                        '1.1/1.1.1',
                        '1.1/1.1.0',
                    ]
                }, 
                {
                    title: '1.0 (2022)',
                    collapsable: false,
                    children: [
                        '1.0/1.0.13',
                        '1.0/1.0.12',
                        '1.0/1.0.11',
                        '1.0/1.0.10',
                        '1.0/1.0.9',
                        '1.0/1.0.8',
                        '1.0/1.0.7',
                        '1.0/1.0.6',
                        '1.0/1.0.5',
                        '1.0/1.0.4',
                        '1.0/1.0.3',
                        '1.0/1.0.2',
                        '1.0/1.0.1',
                        '1.0/1.0.0',
                    ]
                }, 
            ]
        }
    ],

}