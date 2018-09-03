#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
f = open("10rows.csv", "r")
itr = f.read()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

# for i in range(10):
#     channel.basic_publish(exchange='', routing_key='task_queue', body=itr,
#                           properties=pika.BasicProperties(delivery_mode=2, # make message persistent
#     ))
#     print(" [%d] Sent %r" % (i, message))
channel.basic_publish(exchange='', routing_key='task_queue', body=itr,
        properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
        ))
print(itr)


connection.close()

