# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import time
import traceback
from pymongo import MongoClient
from mdat.config import MONGODB_HOST, MONGODB_PORT
from mdat.db.conn_mongo import conn_mongo
from bson.code import Code

client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = client.md


def rna_count():
    """
    using mapreduce to count the mirna's time
    :return:
    """
    start = time.clock()
    try:
        maps = Code("""function(){emit(this.item2,{"count":1});}""")
        reduces = Code("""function(key, values){
                       var times = 0;
                       for(var i=0; i<values.length;i++){
                           times += values[i].count
                       }
                       var ret={mirna:key,count:times};
                       return ret;}
                       """)
        db.target_scan.map_reduce(maps, reduces, out="rnacount")
    except Exception:
        traceback.print_exc()
    end = time.clock()
    print "cup's time  ", end - start


def target_count():
    """
    分别计算target_scan表中的两个rna在target上重复的数目
    :return:
    """
    start_time = time.time()
    cpu_start = time.clock()
    rna = []
    rrna = []
    rna_dict = {}
    # save the different rna to list
    for item in db.rnacount.find():
        rna.append(item['value']['mirna'])
        rrna.append(item['value']['mirna'])
        rna_dict[item['value']['mirna']] = item['value']['count']

    # rna与rrna分别为正序列逆序列存储着rna的list
    rrna.reverse()

    for i in range(0, len(rna)):
        for j in range(0, len(rna)):

            if rna[i] == rrna[j]:
                break
            common = 0
            for f1 in db.target_scan2.find({"item2": rna[i]}):
                if db.target_scan2.find({"item2": rrna[j], "item1": f1["item1"]}).count():
                    common += 1

            items = {
                "rna1": rna[i],
                "rna1-times": rna_dict[rna[i]],
                "rna2": rrna[j],
                "rna2-times": rna_dict[rrna[j]],
                "common-times": common
            }
            db.is2_similar.insert_one(items)

    end_time = time.time()
    cpu_end = time.clock()
    print 'sum time', end_time-start_time
    print 'cup time', cpu_end-cpu_start

if __name__ == '__main__':
    # rna_count()
    target_count()

