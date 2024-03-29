"""
Django settings for Talk project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

VERSION = '${version}'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'cdxb8_5hxehcq)8$!q$3u7z&f6_8hsv#kp11^$kvf9co4%^pnm'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'blog',
    'config',
    'comment',
    'captcha',

    'dal',              # 自动补全代码的轻量级插件 django-autocomplete-light
    'dal_select2',
    'ckeditor',         # 富文本编辑器
    'ckeditor_uploader',# 富文本编辑器上传图片模块
    'crispy_forms',
    'rest_framework',
    'xadmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    #自定义的设置用户uuid的中间件
    'blog.middleware.user_id.UseIDMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Talk.urls'

THEME = 'bootstrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Talk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'themes', THEME, "static"),
]

XADMIN_TITLE = 'Typeidea管理后台'
XADMIN_FOOTER_TITLE = 'powered by the5fire.com'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
        'tabSpaces': 4,
        'extraPlugins': 'codesnippet',
    },
}


CKEDITOR_UPLOAD_PATH = "article_images"

#设置redis为缓存，注意redis必须设置密码否则项目运行时会提示不安全
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://192.168.80.130:6379/2',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "123456",
        },
    },
}

#存储图片所使用的
DEFAULT_FILE_STORAGE = 'Talk.storage.WatermarkStorage'

#rest_framework相关设置
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10,
}


# logging日志配置
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
           'format': '%(levelname)s %(asctime)s %(module)s:'
                     '%(funcName)s:%(lineno)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] '
                      '[%(pathname)s:%(funcName)s:%(lineno)d] [%(levelname)s-%(message)s]',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format':'[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers':{
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'blog.log'),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024, #1M
            'backupCount': 5,
         },
        'static_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'statistics.log'),
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf8',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'static': {
            'handlers': ['static_handler'],
            'level': 'DEBUG'
        },
    },
}
