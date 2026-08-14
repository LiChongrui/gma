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
            title:'GmaGIS',
            collapsable: false,
            children: [
                'GmaGIS',
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

    '/UserGuide/gio/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'gio',
            collapsable: false,
            children: [
                'Dataset',
                'Feature',
                'FieldType',
                'FieldTypes',
                'GeoDatabase',
                'Geometry',
                'Layer',
                'VirtualRasterDataset',
                'VirtualVectorGeoDatabase',
                'open_file',
                'open_raster',
                'open_vector',
                'read_dataframe'
            ]
        },
    ],
    '/UserGuide/smc/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'extraction',
            collapsable: false,
            children: [
                'extraction/extract_values', 
                'extraction/zonal_statistics'
            ]
        },
        {
            title: 'interp',
            collapsable: false,
            children: [
                "interp/b_spline", 
                "interp/idw", 
                "interp/kriging", 
                "interp/natural_neighbor", 
                "interp/nearest", 
                "interp/rbf", 
                "interp/trend", 
            ]
        },
        {
            title: 'query',
            collapsable: false,
            children: [
                "query/calculate_area", 
                "query/calculate_distance", 
                "query/coord_transform"
            ]
        },
    ],

    '/UserGuide/climet/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'index',
            collapsable: false,
            children: [
                "index/CWDI", 
                "index/PAP", 
                "index/PCI", 
                "index/RMI", 
                "index/SPEI", 
                "index/SPI", 
                "index/SWAP", 
            ]
        },
        {
            title: 'astropy',
            collapsable: false,
            children: [
                "astronomy/day_light_hours", 
                "astronomy/declination", 
                "astronomy/earth_sun_relative_distance", 
                "astronomy/solar_radiation_flux_oa", 
                "astronomy/time_angle", 
            ]
        },
        {
            title: 'diagnosis',
            collapsable: false,
            children: [
                "diagnosis/Buishand", 
                "diagnosis/MannKendall", 
                "diagnosis/Pettitt", 
                "diagnosis/SNHT", 
            ]
        },
        {
            title: 'et0',
            collapsable: false,
            children: [
                "et0/Hargreaves", 
                "et0/PenmanMonteith", 
                "et0/Thornthwaite", 
            ]
        },
    ],

    '/UserGuide/etools/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'etools',
            collapsable: false,
            children: [
                "aspect", 
                "hillshade", 
                "list_dir", 
                "merge", 
                "mosaic", 
                "orthorectification", 
                "pansharpen", 
                "progress_fun", 
                "read", 
                "roughness", 
                "slope", 
                "tpi", 
                "translate", 
                "tri", 
            ]
        },
    ],
    '/UserGuide/math/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'correction',
            collapsable: false,
            children: [
                "correction/gamma", 
                "correction/log", 
                "correction/sigmoid", 
            ]
        },
        {
            title: 'evaluation',
            collapsable: false,
            children: [
                "evaluation/MAE", 
                "evaluation/NRMSE", 
                "evaluation/R2", 
                "evaluation/RMSE", 
                "evaluation/corrcoef",
            ]
        },
        {
            title: 'kernel',
            collapsable: false,
            children: [
                "kernel/aggregate",
            ]
        },
        {
            title: 'prepro',
            collapsable: false,
            children: [
                "prepro/fill_nodata", 
                "prepro/to_numeric_array", 
            ]
        },
        {
            title: 'smooth',
            collapsable: false,
            children: [
                "smooth/moving_average", 
                "smooth/savitzky_golay", 
            ]
        },
        {
            title: 'stretch',
            collapsable: false,
            children: [
                "stretch/hist_equalize", 
                "stretch/max_min", 
                "stretch/percentage", 
                "stretch/std", 
            ]
        },
    ],

    '/UserGuide/rsvi/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'rsvi',
            collapsable: false,
            children: [
                "EVI", 
                "NDBI", 
                "NDVI", 
                "NDWI", 
                "TVDI",
            ]
        },
    ],
    '/UserGuide/driver/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'driver',
            collapsable: false,
            children: [
                "DriveStatistics", 
                "RasterDriver", 
                "VectorDriver", 
            ]
        },
    ],
    '/UserGuide/crs/': [
        {
            title: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            title: 'crs',
            collapsable: false,
            children: [
                "CoordinateReferenceSystem", 
                "Datum", 
                "Ellipsoid", 
                "GeographicCoordinateSystem", 
                "ProjectedCoordinateSystem",
            ]
        },
        {
            title: 'crs.ProjMethods',
            collapsable: false,
            children: [
                "ProjMethods/Aitoff", 
                "ProjMethods/AlbersConicEqualArea", 
                "ProjMethods/AzimuthalEquidistant", 
                "ProjMethods/Bonne", 
                "ProjMethods/CassiniSoldner", 
                "ProjMethods/CompactMiller", 
                "ProjMethods/CylindricalEqualArea", 
                "ProjMethods/EckertI", 
                "ProjMethods/EckertII", 
                "ProjMethods/EckertIII", 
                "ProjMethods/EckertIV", 
                "ProjMethods/EckertV", 
                "ProjMethods/EckertVI", 
                "ProjMethods/EquidistantConic", 
                "ProjMethods/Equirectangular", 
                "ProjMethods/GallStereographic", 
                "ProjMethods/GoodeHomolosine", 
                "ProjMethods/LambertAzimuthalEqualArea", 
                "ProjMethods/LambertConformalConic2SP", 
                "ProjMethods/Loximuthal", 
                "ProjMethods/Mercator", 
                "ProjMethods/Mercator2SP", 
                "ProjMethods/Mollweide", 
                "ProjMethods/NaturalEarth", 
                "ProjMethods/NaturalEarthII", 
                "ProjMethods/Polyconic", 
                "ProjMethods/Robinson", 
                "ProjMethods/Sinusoidal", 
                "ProjMethods/Times", 
                "ProjMethods/TransverseMercator", 
                "ProjMethods/VanDerGrinten", 
                "ProjMethods/WinkelI", 
                "ProjMethods/WinkelII", 
                "ProjMethods/WinkelTripel", 
            ]
        },
    ],

}