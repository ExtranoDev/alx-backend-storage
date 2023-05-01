#!/usr/bin/env python3
"""
uses the requests module to obtain the HTML content of a particular
URL and returns it
"""
import requests
import redis
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ uses the requests to obtain content of a URL and returns it"""
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text

if __name__ == "__main__":
	get_page('http://slowwly.robertomurray.co.uk')
