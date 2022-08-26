import json
from kombu import Connection, Producer, Exchange, Queue

from src.app import flask_app as app


def publish_event(event_msg, queue, exchange, routing_key):
    with Connection(app.config['CELERY_BROKER_URL']) as conn:
        with conn.channel() as channel:
            event_queue = Queue(
                queue,
                Exchange(exchange, 'topic', durable=True),
                routing_key
            )
            producer = Producer(channel)
            try:
                print(f'before: publish event {event_queue.routing_key}')
                p = producer.publish(
                    json.dumps(event_msg),
                    retry=True,
                    exchange=event_queue.exchange,
                    routing_key=event_queue.routing_key,
                    declare=[event_queue],
                    content_type='application/json',
                    content_encoding='utf-8'
                )
                print(f'after: publish event {event_queue.routing_key}')
                if p.ignore_result or p.failed or p.on_error:
                    print('publish event failed. --- call fallback ----')
            except Exception as e:
                print(f'Exception occured: {str(e)}')
