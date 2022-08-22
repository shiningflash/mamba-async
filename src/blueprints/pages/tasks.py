from src.app import celery_app
from src.publish import publish_event

celery = celery_app


@celery.task(bind=True)
def my_task(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    event_msg = {
        'payload': kwargs.get('payload')
    }
    publish_event(
        event_msg=event_msg,
        queue='mamba-async_tasks_stock entry_halosis update',
        exchange='mamba-async',
        routing_key='mamba-async.tasks.halosis.update'
    )
