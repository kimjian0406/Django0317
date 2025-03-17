INSTALLED_APPS = [
    # 기존 앱들...
    'django_summernote',
    'django_cleanup',
    # 기타 앱들...
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# django-summernote 설정
SUMMERNOTE_CONFIG = {
    'iframe': {
        'width': '100%',
        'height': '500px',
    },
}

INSTALLED_APPS = [
    ...
    'django_cleanup.apps.CleanupConfig',  # django-cleanup 추가
]
INSTALLED_APPS = [
    # 다른 앱들
    'django_summernote',
]
SUMMERNOTE_CONFIG = {
    'js': ('summernote/summernote.js',),
    'css': ('summernote/summernote.css',),
}

