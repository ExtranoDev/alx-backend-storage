#!/usr/bin/env python3
"""
uses the requests module to obtain the HTML content of a particular
URL and returns it
"""
import requests
import redis
from functools import wraps


r = redis.Redis()


def count_url_visit(method):
    """count number of times a url was visited"""
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        url_key = url
        data = r.get(url_key)
        if data:
            return data.decode("utf-8")
        count_access = "count:{}".format(url)
        html = method(url)
        r.incr(count_access)
        r.setex(url_key, 10, hmtl)
        return html
    return wrapper


@count_url_visit
def get_page(url: str) -> str:
    """ uses the requests to obtain content of a URL and returns it"""
    html_content = requests.get(url)
    return html_content.text
