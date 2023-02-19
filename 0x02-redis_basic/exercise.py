#!/usr/bin/env python3
"""
Create a Cache class
Create a store method
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count the number of time a function is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method that takes a data argument and returns a key as string
        creates key using the uuid libary
        arg: data: to be inserted with created key
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Callable = None):
        """
        method that take a key string argument
        and an optional Callable argument named fn

        fn will be used to convert the data back to the desired format
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        converts the data to string
        """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        converts data to integer
        """
        data = self._redis.get(key)
        return int.from_bytes(data)
