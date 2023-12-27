import redis
from rq import Queue, Connection, Worker
import environ
from tasks.billing import bill_tokens
import time
import os

listen = ['high', 'default', 'low']

env = environ.Env()
environ.Env.read_env()


redis_url = env('REDIS_URL')

conn = redis.from_url(redis_url)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()