from src.app import celery_app
from src.publisher import publish_event

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
        queue='sales_order.events.captured.erpnext.create',
        exchange='sales_order.events.exchange',
        routing_key='sales_order.events.captured.erpnext'
    )
