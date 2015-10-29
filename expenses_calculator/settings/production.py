from expenses_calculator.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    u'172.31.224.148',
    'localhost',
    '*'
]

DATABASES = {
    'default': {},
    'users_master': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'boracay',
        'NAME': 'boracay_production',
        'PASSWORD': 'Xhdtlstk!2Wjdfl',
        'HOST': 'page-user.mydb.iwilab.com',
        'PORT': '3306'
    },
    'users_slave': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'boracay',
        'NAME': 'boracay_production',
        'PASSWORD': 'Xhdtlstk!2Wjdfl',
        'HOST': 'page-user-slv.mydb.iwilab.com',
        'PORT': '3306'
    }
}

ATS_IMG_SERVER_URL = 'ats server url on PRODUCTION'
