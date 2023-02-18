#!/usr/bin/env python3
"""
Function lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Returns all data in a collection or an empty list if collection is none
    Args:
        mongo_collection: mongo colleciton
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
