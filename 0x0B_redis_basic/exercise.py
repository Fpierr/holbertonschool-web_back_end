#!/usr/bin/env python3
""" Redis Module """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator that tracks how many times a function is invoked """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator that logs function inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        input_key = key + ":inputs"
        output_key = key + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(fn: Callable):
    """ Displays the function call history, including input-output pairs """
    redis_instance = redis.Redis()
    function_name = fn.__qualname__
    call_count = redis_instance.get(function_name)
    try:
        call_count = call_count.decode('utf-8')
    except Exception:
        call_count = 0
    time_str = "time:" if call_count == 1 else "times:"
    print(f'{function_name} was called {call_count} {time_str}')
    inputs = redis_instance.lrange(function_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(function_name + ":outputs", 0, -1)
    for input_value, output_value in zip(inputs, outputs):
        try:
            input_value = input_value.decode('utf-8')
        except Exception:
            input_value = ""
        try:
            output_value = output_value.decode('utf-8')
        except Exception:
            output_value = ""
        print(f'{function_name}(*{input_value}) -> {output_value}')


class Cache():
    """ A simple cache class for interacting with Redis """

    def __init__(self):
        """ Initialize the Redis client and clear the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store a piece of data in Redis, associated with a unique key """
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Retrieve data from Redis and optionally apply a function to the result """
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key: str) -> int:
        """ Retrieve data as an integer """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value

    def get_str(self, key):
        """ Retrieve data as a string """
        value = self._redis.get(key)
        return value.decode("utf-8")
