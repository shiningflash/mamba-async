from celery import bootsteps
from kombu import Consumer, Exchange, Queue, binding
from src.blueprints.consumer.process.sales_order import process_sales_order


class SalesOrderConsumer(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        print('get_consumers enter')
        exchange = Exchange(
            name='sales_order.events.exchange',
            type='topic',
            durable=True
        )
        return [
            Consumer(
                channel,
                queues=[
                    Queue(
                        name='sales_order.events.captured.erpnext.create',
                        bindings=[
                            binding(
                                exchange,
                                routing_key='sales_order.events.captured.erpnext'
                            ),
                        ],
                    )
                ],
                callbacks=[self.handle_message],
                accept=['json']
            )]

    @staticmethod
    def handle_message(body, message):
        print('enter callbacks')
        try:
            print('enter', 'sales order consumer')
            print(body)
            message.ack()
            print('done')
            process_sales_order(data=body)
        except Exception as e:
            print('exception occurs: ', str(e))
            return
