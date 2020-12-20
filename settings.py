# Heroku设置
if os.getcwd() == '/app':    # 函数getcwd() ，它获取当前的工作目录 （当前运行的文件所在的目录）,在Heroku部署中，这个目录总是/app
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }
    # 让request.is_secure()承认X-Forwarded-Proto头
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # 支持所有的主机头（host header）
    ALLOWED_HOSTS = ['*']
    # 静态资产配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
