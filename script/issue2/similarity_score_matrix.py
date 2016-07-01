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
                 for i in db.similar_score_new2.find({"$or": [{"rna1": r1, "rna2": r2}, {"rna1": r2, "rna2": r1}]}):
                     similar.append(i['similar_sore'])

            files.write(str(similar))
            files.write("\n")
    except Exception:
        traceback.print_exc()


def get_rna_name(file_path):
    """
    generate the rna name which related to rna-similar-score
    :param file_path:
    :return:
    """
    rna = db.target_scan_split.distinct("item2")
    rna.sort()
    files = file(file_path, 'w')

    for i in rna:
        files.write(i)
        files.write('\n')

if __name__ == "__main__":
    # generate_matrix("/home/wtq/rna-similar-score.txt")
    get_rna_name("/home/wtq/rna-name.txt")
