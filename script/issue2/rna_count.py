# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

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
    try:
        maps = Code("""function(){emit(this.mirna,{"count":1});}""")
        reduces = Code("""function(key, values){
                       var times = 0;
                       for(var i=0; i<values.length;i++){
                           times += values[i].count
                       }
                       var ret={mirna:key,count:times};
                       return ret;}
                       """)
        db.hybrid.map_reduce(maps, reduces, out="rnacount")
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    rna_count()
