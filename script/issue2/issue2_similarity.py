# !/usr/bin/evn python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import traceback
from mdat.db.conn_mongo import conn_mongo


def combin(a, b):
    m = a
    n = b
    if m < n:
        m, n = n, m

    fenmu = 1.0
    fenzi = 1.0
    for i in range(0, int(n)):
        fenzi = fenzi * m
        m = m-1
    for i in range(0, int(n)):
        fenmu = fenmu * (i + 1)

    return float(fenzi / fenmu)


def similarity_element(n1, n2, c):
    """

    :param n1: Number of times of n1
    :param n2: Number of times of n2
    :param c:  n1 and n2 the common times in second column
    :return:
    """
    k = c
    try:
        rate = 0
        for i in range(1, k):
            rate += ((combin(c, i)*combin(n1+n2-2*c, c-i))/combin(n1+n2-c, c))
        return 1 - rate
    except Exception, e:
        traceback.print_exc()


def calculate_similar():
    """
    calculate rna1 and rna2 similarity and then insert into mongodb
    :return:
    """
    client = conn_mongo()
    db = client.md
    for item in db.rna_times.find():
        n1 = item["rna1-times"]
        n2 = item["rna2-times"]
        c = item["common-times"]

        similarity = similarity_element(n1, n2, c)
        items = {
            "rna1": item["rna1"],
            "rna2": item["rna2"],
            "similar_sore": similarity
        }
        db.similar_score.insert(items)

if __name__ == "__main__":
    # print similarity_element(5.0, 6.0, 3)
    calculate_similar()
