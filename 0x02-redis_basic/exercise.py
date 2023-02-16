#!/usr/bin/env python3
"""
Create a Cache class
Create a store method
"""
import redis
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        __init__ method, store an instance of the Redis client
        arg: redis: instace of Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Method that takes a data argument and returns a string
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key
