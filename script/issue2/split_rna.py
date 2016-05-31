# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import traceback
from mdat.db.conn_mongo import conn_mongo


def split_rna():
    """
    split rna if it contains "/"
    :return:
    """
    try:
        client = conn_mongo()
        db = client.md
        # db.target_scan_split.ensureIndex({"item1": 1, "item2": 1})
        for item in db.target_scan2.find():
            rna = item["item2"]
            head = ""

            if not rna.__contains__("/"):
                items = {
                    "item2": "hsa-"+rna,
                    "item1": item["item1"]
                }
                if db.target_scan_split.find(items).count() == 0:
                    db.target_scan_split.insert(items)

            else:
                for i in rna.split("/"):
                    if i.__contains__("miR"):
                        head = "hsa-miR-"
                        items = {
                            "item2": "hsa-"+i,
                            "item1": item["item1"]
                        }
                        if db.target_scan_split.find(items).count() == 0:
                            db.target_scan_split.insert(items)

                    elif i.__contains__("let"):
                        head = "hsa-let-"
                        items = {
                            "item2": "hsa-"+i,
                            "item1": item["item1"]
                        }
                        if db.target_scan_split.find(items).count() == 0:
                            db.target_scan_split.insert(items)

                    else:
                        items = {
                            "item2": head + i,
                            "item1": item["item1"]
                        }
                        if db.target_scan_split.find(items).count() == 0:
                            db.target_scan_split.insert(items)
    except Exception, e:
        traceback.print_exc(e)


if __name__ == "__main__":
    split_rna()

