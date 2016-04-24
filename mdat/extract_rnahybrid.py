#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import traceback
from pymongo import MongoClient
from mdat.config import MONGODB_HOST, MONGODB_PORT


def extract_rnahybrid():
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.md
    collection = db.hybrid
    try:
        with open('../data/rnahybrid.aln', 'r') as input:
            for line in input:
                if not len(line) == 1:
                    item = {}
                    # 去掉字符串中的\n
                    line = line.strip("\n")
                    words = line.split(" ")
                    # print 'word', words[0]
                    if words[0] == 'target:':
                        target = words[1]
                    if words[0] == 'miRNA' and words[1] == ':':
                        item[words[2]] = target
                        if collection.find(item).count() == 0:
                            collection.insert_one(item)

    except Exception, e:
        traceback.print_exc()


if __name__ == '__main__':
    extract_rnahybrid()
