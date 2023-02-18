#!/usr/bin/env python3
"""
script provides some stats about Nginx logs stored in MongoDB
"""


if __name__ == '__main__':
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_dict = {i: 0 for i in methods}
    count = 0
    status_count = 0
    ip = ''

    for log in db.nginx.find():
        count += 1
        method_type = log.get('method')

        if method_type in methods:
            method_dict[method_type] += 1
            if method_type == "GET":
                if log.get('path') == '/status':
                    status_count += 1
    print("{} logs".format(count))
    print("Methods:")
    for key, val in method_dict.items():
        print('\tmethod {}: {}'.format(key, val))
    print('{} status check'.format(status_count))

    pipeline = [
            {"$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
                }},
            {"$sort": {"count": -1}}, {"$limit": 10}
            ]
    counted_ips = db.nginx.aggregate(pipeline)
    print("IPs:")
    for ip in counted_ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))
