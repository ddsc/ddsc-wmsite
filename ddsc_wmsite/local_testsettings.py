DATABASES = {
    'default': {
        'NAME': 'DDSC_PLAY_TEMP',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'shaoqing',
        'PASSWORD': 'geoict',
        'HOST': '10.10.101.118', # empty string for localhost.
        'PORT': '5432', # empty string for default.
    }
}

IMPORTER_GEOSERVER = {
    'geoserver_url':
        'http://10.10.101.118:8080/geoserver',
    'geoserver_workspace':
        'ddsc',
}

