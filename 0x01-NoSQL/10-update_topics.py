#!/usr/bin/env python3
"""
Function changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name: str, topics):
    """
    updates the topic of the school documents
    Args:
        mongo_collection: mongo collection object
        name(str): school name to update
        topics(list of str): list of topics
    """
    condition = {'name': name}
    update_top = {'$set': {'topics': topics}}
    mongo_collection.update_many(condition, update_top)
