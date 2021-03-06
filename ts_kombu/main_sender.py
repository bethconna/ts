#-*- coding: utf-8 -*-
from sender import Producer
from config import config_use

if __name__ == '__main__':
    producer = Producer(config_use.get_connection())

    producer.send_as_task(exchange_name='AExchange', args=('about a ',), kwargs={"a": "a"},
                          routing_key='a')
    producer.send_as_task(exchange_name='BExchange', args=('about b ',), kwargs={"b": "b"},
                          routing_key='b')
