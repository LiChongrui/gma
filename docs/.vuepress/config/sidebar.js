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
                '',
                {
                    title: 'Index',
                    collapsable: false,
                    children: [
                        'Index/SPEI',
                        'Index/SPI',
                        'Index/PAP',
                        'Index/RMI',
                    ]
                },
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
                    title: 'Astronomy',
                    collapsable: false,
                    children: [
                        'Astronomy/DaylightHours',
                        'Astronomy/Declination',
                        'Astronomy/HourAngle',
                        'Astronomy/RDBSunAndEarth',
                        'Astronomy/SolarRadiationFluxOA'
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
                 '',
                {
                    title: 'PrePro',
                    collapsable: false,
                    children: [
                        'PrePro/FillNoData',
                        'PrePro/ToNumericArray',
                    ]
                },
                {
                    title: 'Smooth',
                    collapsable: false,
                    children: [
                        'Smooth/MovingAverage',
                        'Smooth/SavitzkyGolay',
                    ]
                },
                {
                    title: 'Evaluation',
                    collapsable: false,
                    children: [
                        'Evaluation/CORR',
                        'Evaluation/D',
                        'Evaluation/MaxAE',
                        'Evaluation/NRMSE',
                        'Evaluation/R2',
                        'Evaluation/RMSE',
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
                },
                {
                    title: 'Stretch',
                    collapsable: false,
                    children: [
                        'Stretch/Percentage',
                        'Stretch/STD',
                        'Stretch/MaxMin',
                        'Stretch/HistEqualize',
                    ]
                },
                {
                    title: 'Correction',
                    collapsable: false,
                    children: [
                        'Correction/Sigmoid',
                        'Correction/Log',
                        'Correction/Gamma',
                    ]
                },
            ]
        }
    ],

    '/UserGuide/osf/': [
        {
            title: '系统交互',
            collapsable: false,
            children: [
                'DateSeries',
                'FindPath',
                'MultiThreading',
                'UnZip',
                'Zip'
            ]
        }
    ],

    '/UserGuide/smc/': [
        {
            title: '空间杂项',
            collapsable: false,
            children: [
                {
                    title: 'Extraction',
                    collapsable: false,
                    children: [
                        'Extraction/ExtractValues'
                    ]
                },
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
                },
                {
                    title: 'Query',
                    collapsable: false,
                    children: [
                        'Query/CALArea',
                        'Query/CALDistance',
                        'Query/TRANCoordinate'
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
                {
                    title: 'Basic',
                    collapsable: false,
                    children: [
                        'Basic/AddColorTable',
                        'Basic/BandSynthesis',
                        'Basic/ChangeDataType',
                        'Basic/Clip',
                        'Basic/Deformation',
                        'Basic/GenerateOVR',
                        'Basic/Mosaic',
                        'Basic/OrthophotoCorrection',
                        'Basic/Reproject',
                        'Basic/Resample',
                        'Basic/ToOtherFormat',
                    ]
                },
                {
                    title: 'Decompose',
                    collapsable: false,
                    children: [
                        'Decompose/BandDecomposition',
                        'Decompose/SplitImage'
                    ]
                },
                {
                    title: 'Extraction',
                    collapsable: false,
                    children: [
                        'Extraction/Isopleth',
                        'Extraction/Reclassify',
                        'Extraction/ToVector'
                    ]
                },
                {
                    title: 'Fusion',
                    collapsable: false,
                    children: [
                        'Fusion/Pansharpen',
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
                    title: 'Multidim',
                    collapsable: false,
                    children: [
                        'Multidim/ToNORRaster',
                    ]
                },
                {
                    title: 'Surface',
                    collapsable: false,
                    children: [
                        'Surface/Aspect',
                        'Surface/HillShade',
                        'Surface/Roughness',
                        'Surface/Slope',
                        'Surface/TPI',
                        'Surface/TRI',
                    ]
                }
            ]
        }
    ],
    '/UserGuide/vesp/': [
        {
            title: '矢量处理',
            collapsable: false,
            children: [
                {
                    title: 'Basic',
                    collapsable: false,
                    children: [
                        'Basic/ChangeGeometryType',
                        'Basic/Check',
                        'Basic/FixGeometry',
                        'Basic/Reproject',
                        'Basic/Simplify',
                        'Basic/ToOtherFormat',
                    ]
                },
                {
                    title: 'Extraction',
                    collapsable: false,
                    children: [
                        'Extraction/Split',
                        'Extraction/ToRaster',
                    ]
                },
                {
                    title: 'Geometry',
                    collapsable: false,
                    children: [
                        'Geometry/Clip',
                        'Geometry/Erase',
                        'Geometry/Intersection',
                        'Geometry/SymDifference',
                        'Geometry/Union',
                        'Geometry/Update',
                    ]
                },
            ]
        }
    ],

    '/UserGuide/map/': [
        {
            title: '地图工具',
            collapsable: false,
            children: [
                '',
                {
                    title: 'MapFrame',
                    collapsable: false,
                    children: [
                        'plot/MapFrame/',
                        'plot/MapFrame/AddLayer',
                        'plot/MapFrame/AddFeature',
                        'plot/MapFrame/AddCompass',
                        'plot/MapFrame/AddGridLines',
                        'plot/MapFrame/AddLegend',
                        'plot/MapFrame/AddScaleBar',
                        'plot/MapFrame/AddDataSetClassify',
                        'plot/MapFrame/AddDataSetDiscrete',
                        'plot/MapFrame/SetBackground',
                        'plot/MapFrame/SetFrame',
                    ]
                }, 
                {
                    title: 'plot',
                    collapsable: false,
                    children: [
                        'plot/GetSystemFonts',
                        'plot/GetPreDefinedCMaps',
                    ]
                }, 
                {
                    title: 'inres',
                    collapsable: false,
                    children: [
                        'inres/WorldDataSet',
                        'inres/WorldLayer',
                    ]
                }, 
            ],
        }
    ],

    '/UserGuide/gft/': [
        {
            title: '地理驱动',
            collapsable: false,
            children: [
                'GetRasterFormat',
                'GetVectorFormat',
                'RasterSummary',
                'VectorSummary',
            ]
        }
    ],

    '/UserGuide/io/': [
        {
            title: '输入输出',
            collapsable: false,
            children: [
                '',
                'CreateFeature',
                'CreateGeoDataBase',
                'CreateLayer',
                'Open',
                'ReadArrayAsDataSet',
                'ReadDataFrameAsLayer',
                'ReadRaster',
                'ReadVector',
                'SaveArrayAsRaster',
                'GeoDataBase',
                'DataSet',
                'Layer',
                'Feature',
            ]
        },
    ],

    '/UserGuide/crs/': [
        {
            title: '空间参考',
            collapsable: false,
            children: [
                '',
                'Ellips',
                'Ellipsoid',
                'Datum',
                'ProjMethod',
                'AngularUnits',
                'LinearUnits',
                'PriMems',
                'GeogCS',
                'ProjCS',
                'SpatRef'
            ]
        },
    ],

    '/Update/log/': [
        {
            title:'更新日志',
            collapsable: false,
            children: [
                 {
                    title: 'gma 2',
                    collapsable: false,
                    children: [
                        '2.0/2.0.4',
                        '2.0/2.0.3',
                        '2.0/2.0.2',
                        '2.0/2.0.1',
                        '2.0/2.0.0',
                    ]
                }, 
                {
                    title: 'gma 1',
                    collapsable: false,
                    children: [
                        '1.1/1.1.6',
                        '1.1/1.1.5',
                        '1.1/1.1.4',
                        '1.1/1.1.3',
                        '1.1/1.1.2',
                        '1.1/1.1.1',
                        '1.1/1.1.0',
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