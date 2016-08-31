# !usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wtq'

import sys
import csv


def generate_rna_disease_matrix():
    """
    generate relationship between rna and disease
    :return:
    """
    disease_names = []
    with open(sys.path[0] + '/data/disease.names.txt', 'r') as f:
        for line in f:
            disease_names.append(line.rstrip())

    relationship = []
    with open(sys.path[0] + '/data/rna-name.txt', 'r') as f:
        for line in f:
            temp = [0]*134
            rna_name = line.rstrip()
            index = 0
            for disease in disease_names:

                with open(sys.path[0] + '/data/diseases-miRNA.associations.simple2.xlsx', 'r') as csv_file:
                    for csv_line in csv_file:
                        relas = csv_line.strip().split(',')
                        if rna_name == relas[0] and disease == relas[1]:
                            temp[index] = 1
                            break
                index += 1

            relationship.append(temp)

    return relationship

if __name__ == "__main__":
    generate_rna_disease_matrix()
