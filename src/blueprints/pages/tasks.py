import uuid

from src.app import celery_app
from src.publisher import publish_event

celery = celery_app


@celery.task(bind=True)
def my_task(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    event_msg = {
        'event_id': uuid.uuid4().hex,
        'payload': kwargs.get('payload')
    }
    queue_name = kwargs.get('queue')
    exhange_name = kwargs.get('exchange')
    routing_key = kwargs.get('routing_key')
    publish_event(
        event_msg=event_msg,
        queue=queue_name,
        exchange=exhange_name,
        routing_key=routing_key
    )
