#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'kevin'

import numpy

from mdat.util import calculate_dv_similarity


if __name__ == '__main__':
    diseases = []
    with open('../data/disease_names.txt') as f:
        for line in f.readlines():
            diseases.append(line.strip('\n\r'))

    similarity = []
    for disease_1 in diseases:
        cu = []
        for disease_2 in diseases:
            cu.append(calculate_dv_similarity(disease_1, disease_2))
        similarity.append(cu)
    a = numpy.asarray(similarity)
    numpy.savetxt("disease_similarity_result.csv", a, delimiter=",")


