"""
Django settings for v2ex project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h8mx&zhj$wm=-(w^#=9!2&aufed18#45rx3+c+1g*2yruqf@!0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'operation.apps.OperationConfig',
    'topic.apps.TopicConfig',
    'notes.apps.NotesConfig',
    'django_celery_results',
]

AUTH_USER_MODEL = "user.UserProfile"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'middle.custom_middle.CountOnlineMiddlewareMixin',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'v2ex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'v2ex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 数据库取本地时间


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 缓存相关
CACHES = {
    # 默认配置，cache 单独使用
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 新增配置让session 使用，
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 设置忽略连接异常
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# session 相关配置
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_AGE = 60 * 20
# 用户刷新页面，重新设置缓存时间
SESSION_SAVE_EVERY_REQUEST = True

# 分页器配置
PRE_PAGE_COUNT = 15
PAGER_NUMS = 7

# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# TODO
# 提交之前删除此信息
# 发送邮件的邮箱
EMAIL_HOST_USER = '1160628027@qq.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'grywawxdwsnhbaee'
# 收件人看到的发件人
EMAIL_FROM = '1160628027@qq.com'

# 主域
BASE_DOMAIN = 'http://127.0.0.1:8000'

# 头像存放目录（当然也可以使用OSS等云存储，这里存储到本地）
AVATAR_FILE_PATH = os.path.join(BASE_DIR, 'static', 'img')


# CELERY 配置
# BROKER 地址
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/2'
# RESULT 返回到数据库中（可选返回cache中）
CELERY_RESULT_BACKEND = 'django-db'
# 接受的格式json
CELERY_ACCEPT_CONTENT = ['json']
# 序列化为json
CELERY_TASK_SERIALIZER = 'json'

# CELERY_BEAT_SCHEDULE = {
#     # 周期性任务
#     'task-one': {
#         'task': 'app.tasks.print_hello',
#         'schedule': 5.0, # 每5秒执行一次
#         # 'args': ()
#     },
#     # 定时任务
#     'task-two': {
#         'task': 'app.tasks.print_hello',
#         'schedule': crontab(minute=0, hour='*/3,10-19'),
#         # 'args': ()
#     }
# }