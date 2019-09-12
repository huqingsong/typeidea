import os
import raven

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talk',
        'HOST': '192.168.80.129',
        'USER': 'root',
        'PASSWORD': '123',
        'PORT': 3306
    }
}

#这里使用的是django的性能分析工具
INSTALLED_APPS += [
    'debug_toolbar',
    # 'raven.contrib.django.raven_compat',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')