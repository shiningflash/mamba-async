import os


DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)


# Celery Config
# CELERY_BROKER_URL = 'amqp://admin:mypassword@localhost:5672/myvhost/'
# CELERY_BROKER_URL = 'amqp://localhost:15672/'
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# CELERY_RESULT_BACKEND = 'amqp://admin:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'rpc://'
# CELERY_RESULT_BACKEND = 'amqp://localhost:15672/'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
