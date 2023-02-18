#!/usr/bin/env python3
"""
Function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts data into document
    Args:
        mongo_collection: document collectio
        kwargs(dict): data
    """
    if mongo_collection is not None:
        result = mongo_collection.insert_one({**kwargs})
        return result.inserted_id
    return ""
