module.exports = {


    '/Explore/': [
        {
            title:'功能探索',
            collapsable: false,
            children: [
                '',
                'Structure',
                'Default',
                'Constants',
                'Naming',
            ]
        }
    ],

    '/UserGuide/': [
        {
            title:'使用说明',
            collapsable: false,
            children: [
                '',
                'Function'
            ]
        },
        {
            title: '指数运算',
            collapsable: false,
            children: [
                'index/EVI',
                'index/NDBI',
                'index/NDWI',
                'index/NDVI',
                'index/PM_ET0',
                'index/TVDI',
            ],
        },
        {
            title: '数学运算',
            collapsable: false,
            children: [
                'math/FillNoData',
                'math/ToNumericArray',
                {
                    title: 'Smooth',
                    collapsable: false,
                    children: [
                        'math/Smooth/',
                        'math/Smooth/MovingAverage',
                        'math/Smooth/SavitzkyGolay',
                    ]
                },
                {
                    title: 'Evaluation',
                    collapsable: false,
                    children: [
                        'math/Evaluation/',
                        'math/Evaluation/CORR',
                        'math/Evaluation/D',
                        'math/Evaluation/MaxAE',
                        'math/Evaluation/Methods',
                        'math/Evaluation/NRMSE',
                        'math/Evaluation/R2',
                        'math/Evaluation/RMSE',
                        'math/Evaluation/Select',
                    ]
                }
            ]
        },
        {
            title: '系统交互',
            collapsable: false,
            children: [
                'osf/DateSeries',
                'osf/GetPath',
                'osf/MultiThreading',
                'osf/UnZip',
                'osf/Zip',
                {
                    title: 'Rename',
                    collapsable: false,
                    children: [
                        'osf/Rename/',
                        'osf/Rename/Intercept',
                        'osf/Rename/Modify',
                        'osf/Rename/Replace',
                    ]
                }
            ]
        },
        {
            title: '空间杂项',
            collapsable: false,
            children: [
                'smc/CALDistance',
                'smc/TRANCoordinate',
            ]
        },
        {
            title: '栅格处理',
            collapsable: false,
            children: [
                'rasp/AddColorTable',
                'rasp/BandDecomposition',
                'rasp/BandSynthesis',
                'rasp/ChangeDataType',
                'rasp/Clip',
                'rasp/Deformation',
                'rasp/GenerateOVR',
                'rasp/Mosaic',
                'rasp/MultiSDSToTif',
                'rasp/OrthophotoCorrection',
                'rasp/Reproject',
                'rasp/Resample',
                'rasp/SplitImage',
                'rasp/ToOtherFormat',
                'rasp/ToVector',
                'rasp/WriteRaster',
                {
                    title: 'Fusion',
                    collapsable: false,
                    children: [
                        'rasp/Fusion/Pansharpen',
                    ]
                }
            ]
        },
        {
            title: '栅格分析',
            collapsable: false,
            children: [
                {
                    title: 'DEM',
                    collapsable: false,
                    children: [
                        'raa/DEM/Aspect',
                        'raa/DEM/HillShade',
                        'raa/DEM/Roughness',
                        'raa/DEM/Slope',
                        'raa/DEM/TPI',
                        'raa/DEM/TRI',
                    ]
                }
            ]
        },
        {
            title: '矢量处理',
            collapsable: false,
            children: [
                'vesp/Check',
                'vesp/Clip',
                'vesp/Erase',
                'vesp/FixGeometry',
                'vesp/Intersection',
                'vesp/Reproject',
                'vesp/Simplify',
                'vesp/Split',
                'vesp/SymDifference',
                'vesp/ToOtherFormat',
                'vesp/ToRaster',
                'vesp/Union',
                'vesp/Update',
            ]
        },
        {
            title: '高级配置',
            collapsable: false,
            children: [
                'config/GetRACreationOption',
                'config/GetRasterFormat',
                'config/GetVectorFormat',
                'config/GetVELayerCreationOption',
                'config/RasterFormatInfo',
                'config/VectorFormatInfo',
            ]
        },
        {
            title: '其他函数',
            collapsable: false,
            children: [
                'other/Open',
                'other/RasterOpen',
                'other/VectorOpen',
                'other/Layer',
            ]
        },
    ],
    '/Update/': [
        {
            title:'更新记录',
            collapsable: false,
            children: [
                '',
                'Update',
                'Plan',
            ]
        }
    ],

}