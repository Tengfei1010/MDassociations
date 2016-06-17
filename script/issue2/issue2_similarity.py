# !/usr/bin/evn python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import decimal
import operator
import traceback
from mdat.db.conn_mongo import conn_mongo


def c1(a, b):
    n = a
    k = b
    # 使用float则不能转化长整型的数，只能使用decimal
    # 使用reduce来求组合，简化了代码
    if k == 0:
        return 1
    return decimal.Decimal(reduce(operator.mul, range(n - k + 1, n + 1)) / reduce(operator.mul, range(1, k + 1)))


def similarity_element(n1, n2, c):
    """

    :param n1: Number of times of n1
    :param n2: Number of times of n2
    :param c:  n1 and n2 the common times in second column
    在用此公式计算时会出现问题，当n1=n2=c时，此时组合的下标出现了0，则此组合数为0，结果为1-0=1
    当n1 n2 c 很大时，随着迭代此处的增加(c1(c, i)*c1(n1+n2-2*c, c-i))/c1(n1+n2-c, c)
    会越来越小，最终趋于0，最后的结果就为1-1=0
    :return:
    """
    k = c
    try:
        rate = decimal.Decimal(0)
        for i in range(1, k):
            rate += (c1(c, i)*c1(n1+n2-2*c, c-i))/c1(n1+n2-c, c)

        return 1 - rate
    except Exception, e:
        traceback.print_exc()


def similarity_element_new(n1, n2, c, N):
    """

    :param n1:
    :param n2:
    :param c:
    :return:
    """

    min_times = n1
    if min_times > n2:
        min_times = n2
    rate = decimal.Decimal(0)
    for i in range(c, min_times+1):

        rate += (c1(n1, i)*c1(N-n1, n2-i))/c1(N, n2)
    return rate


def calculate_similar():
    """
    calculate rna1 and rna2 similarity and then insert into mongodb
    :return:
    """
    client = conn_mongo()
    db = client.md
    for item in db.rna_times.find():
        n1 = int(item["rna1-times"])
        n2 = int(item["rna2-times"])
        c = int(item["common-times"])
        # 将decimal再转化为float，否则不能在mongo中存储
        similarity = float(similarity_element(n1, n2, c))
        items = {
            "rna1": item["rna1"],
            "rna2": item["rna2"],
            "similar_sore": similarity
        }
        db.similar_score_new.insert(items)


def calculate_similar_new():
    """

    :return:
    """
    client = conn_mongo()
    db = client.md
    list2 = db.target_scan_split.distinct("item1")
    # get the 2th column distinct number
    target_sum = len(list2)
    # 使用 batch_size控制一下每次查询块的大小，防止太大导致长时间不与服务器端联系而报错
    for item in db.rna_times.find().batch_size(50):
        n1 = int(item["rna1-times"])
        n2 = int(item["rna2-times"])
        c = int(item["common-times"])
        # 将decimal再转化为float，否则不能在mongo中存储
        similarity = float(similarity_element_new(n1, n2, c, target_sum))
        items = {
            "rna1": item["rna1"],
            "rna2": item["rna2"],
            "similar_sore": similarity
        }
        db.similar_score_new2.insert(items)


if __name__ == "__main__":
    # print similarity_element(4, 5, 3)
    # calculate_similar()
    # print c1(6, 0)
    calculate_similar_new()


