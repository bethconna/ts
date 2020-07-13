# -*- coding: utf-8 -*-
import os
import threading

from config import config_use
from consumer import ConsumerRoutes

KR = ConsumerRoutes(config_use.get_connection(), 2)

# if __name__ == '__main__':
    # @KR.route(exchange_name="AExchange", routing_key="a")
    # def print_info(body, message):
    #     print('body : "{0}"'.format(body))
    #     message.ack()

    # @KR.route(exchange_name="BExchange", queue_name="BQueue", routing_key="b")
    # def print_info(body, message):
    #     print('body : "{0}"'.format(body))
    #     message.ack()


if __name__ == '__main__':
    print('start1')
    @KR.route(exchange_name="AExchange", queue_name="AQueue", routing_key="a")
    def print_info(body, message):
        print("A线程", threading.currentThread().ident)
        print('A进程', os.getpid(), os.getppid())
        message.ack()
    print('end1')


    print('start2')
    @KR.route(exchange_name="BExchange", queue_name="BQueue", routing_key="b")
    def print_info(body, message):
        print("B线程", threading.currentThread().ident)
        print('B进程', os.getpid(), os.getppid())
        message.ack()
    print('end2')
