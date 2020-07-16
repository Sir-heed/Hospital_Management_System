"""Database Configuration sample"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hms',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'USER': 'db_user',
#         'PASSWORD': 'db_pass',
#         'HOST': 'db_host',
#         'PORT': 'db_port'
#     }
# }