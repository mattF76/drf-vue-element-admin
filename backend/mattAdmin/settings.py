"""
Django settings for mattAdmin project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ad=0-va!_tmz!c&8j&3ofw^)@d_71*w4)7cuowqmb%!2@o!t2c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user.apps.UserConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'mattAdmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mattAdmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # mysql驱动
        'NAME': 'matt_admin',  # 数据库名称
        'USER': 'root',  # 登录帐号
        'PASSWORD': 'root',  # 登录密码
        'HOST': 'db',  # 主机地址（容器部署）
        # 'HOST': '127.0.0.1',  # 主机地址
        'PORT': '3306',  # 端口
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# 运行python manage.py collectstatic命令，会从STATICFILES_DIRS目录下收集的静态文件
# 放到 STATIC_ROOT目录下，该目录下文件可以通过STATIC_URL进行访问
STATIC_ROOT = os.path.join(BASE_DIR, "collect_static/")
STATIC_URL = 'static/'
STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static/"),
]


#其中STATIC_ROOT和STATICFILES_DIRS默认为None，
#即未设置，我是自己配置成这样子的


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# drf使用jwt进行认证
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# jwt token配置
JWT = {
    # token失效时间，单位分钟
    'EXPIRE_MINUTES': 60 * 4
}

# 免登访问的接口(正则表达式风格)
NO_LOGIN_API = [
    r"^/api/user/login",
    r"^/api/user/logout",
    r"^/api/user/info",
    r"^/admin/.*$"
]

# 超管用户角色。拥有该角色，可以访问所有接口
SUPER_ADMIN_ROLE = "admin"

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:9080', 'http://localhost:9080']