# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

from pymongo import MongoClient
from mdat.config import MONGODB_HOST, MONGODB_PORT

def conn_mongo(dbname, mongo_host=MONGODB_HOST, mongo_port=MONGODB_PORT):
    """
    :param dbname:
    :param mongo_host:
    :param mongo_port:
    :return: the connectioned db
    """
    client = MongoClient(mongo_host, mongo_port)
    return client.dbname
