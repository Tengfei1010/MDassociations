# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import traceback
from mdat.db.conn_mongo import conn_mongo

client = conn_mongo()
db = client.md


def generate_matrix(file_path):
    """
    generate the similar_score matrix then write it into csv
    :return:
    """
    files = file(file_path, "w+")
    rna1 = db.target_scan_split.distinct("item2")
    rna1.sort()
    rna2 = rna1
    try:
        for r1 in rna1:
            similar = []
            for r2 in rna2:
                 for i in db.similar_score_new.find({"$or": [{"rna1": r1, "rna2": r2}, {"rna1": r2, "rna2": r1}]}):
                     similar.append(i['similar_sore'])

            files.write(str(similar))
            files.write("\n")
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    generate_matrix("/home/wtq/rna-similar-score.txt")

