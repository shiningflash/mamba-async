import json


def process_sales_order(data=None):
    print('process', 'processing sales order')
    print('data', data)

    # assuming the sales order is failed
    process_failed_sales_order(data=data)

    print('processing done')


def process_failed_sales_order(data=None):
    from src.blueprints.pages.tasks import my_task
    try:
        source_app_name = json.loads(data).get('payload').get('order_data').get('source_app_name')
        print(source_app_name)
    except Exception as _:
        source_app_name = 'unanimous'
    queue_name = f'sales_order.failed.events.captured.erpnext.{source_app_name}'
    task = my_task.delay(
            payload=data,
            queue=queue_name,
            exchange='sales_order.failed.events.exchange',
            routing_key='sales_order.failed.events.captured.erpnext'
        )
    print(task.id, task.status, task.result)
