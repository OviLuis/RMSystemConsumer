from os import environ

from consumer import Consumer
from connection import Connection


if __name__ == "__main__":
    hostname = environ.get("REDIS_HOSTNAME", "localhost")
    port = environ.get("REDIS_PORT", 6379)
    print(hostname)
    print(port)
    connection = Connection(hostname, port)
    r = connection.connect_to_redis()

    consumer = Consumer(r)
    consumer.get_data()
