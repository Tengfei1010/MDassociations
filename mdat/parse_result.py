#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

from mdat.config import MONGODB_HOST, MONGODB_PORT


def parse_result():
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.md
    collection = db.mirana
    with open('../data/result.aln', 'r') as input:
        is_target = False
        for line in input:
            if is_target:
                results = line.split('\t')
                post = {
                    'item1': results[0][1:],
                    'item2': results[1],
                    'item3': results[2],
                }
                collection.insert_one(post)
                is_target = False

            if line.strip() == 'Scores for this hit:':
                is_target = True


if __name__ == '__main__':
    parse_result()
