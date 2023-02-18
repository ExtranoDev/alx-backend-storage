#!/usr/bin/env python3
"""
function returns list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    searchs for data using topic in a collection
    """
    return mongo_collection.find({'topics': topic})
