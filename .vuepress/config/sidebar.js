module.exports = {

    '/docs/UserGuide/gio/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'gio',
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
    '/docs/UserGuide/smc/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'extraction',
            collapsable: false,
            children: [
                'extraction/extract_values', 
                'extraction/zonal_statistics'
            ]
        },
        {
            text: 'interp',
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
            text: 'query',
            collapsable: false,
            children: [
                "query/calculate_area", 
                "query/calculate_distance", 
                "query/coord_transform"
            ]
        },
    ],

    '/docs/UserGuide/climet/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'index',
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
            text: 'astropy',
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
            text: 'diagnosis',
            collapsable: false,
            children: [
                "diagnosis/Buishand", 
                "diagnosis/MannKendall", 
                "diagnosis/Pettitt", 
                "diagnosis/SNHT", 
            ]
        },
        {
            text: 'et0',
            collapsable: false,
            children: [
                "et0/Hargreaves", 
                "et0/PenmanMonteith", 
                "et0/Thornthwaite", 
            ]
        },
    ],

    '/docs/UserGuide/etools/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'etools',
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
    '/docs/UserGuide/math/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'correction',
            collapsable: false,
            children: [
                "correction/gamma", 
                "correction/log", 
                "correction/sigmoid", 
            ]
        },
        {
            text: 'evaluation',
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
            text: 'kernel',
            collapsable: false,
            children: [
                "kernel/aggregate",
            ]
        },
        {
            text: 'prepro',
            collapsable: false,
            children: [
                "prepro/fill_nodata", 
                "prepro/to_numeric_array", 
            ]
        },
        {
            text: 'smooth',
            collapsable: false,
            children: [
                "smooth/moving_average", 
                "smooth/savitzky_golay", 
            ]
        },
        {
            text: 'stretch',
            collapsable: false,
            children: [
                "stretch/hist_equalize", 
                "stretch/max_min", 
                "stretch/percentage", 
                "stretch/std", 
            ]
        },
    ],

    '/docs/UserGuide/rsvi/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'rsvi',
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
    '/docs/UserGuide/driver/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'driver',
            collapsable: false,
            children: [
                "DriveStatistics", 
                "RasterDriver", 
                "VectorDriver", 
            ]
        },
    ],
    '/docs/UserGuide/crs/': [
        {
            text: 'Start',
            collapsable: false,
            children: [
                ''
            ]
        },
        {
            text: 'crs',
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
            text: 'crs.ProjMethods',
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