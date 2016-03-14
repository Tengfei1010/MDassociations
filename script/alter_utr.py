#!/usr/bin/python
# -*- coding: utf-8 -*-

import fileinput
import sys


if __name__ == '__main__':
    for line in fileinput.input('../data/UTR_original.txt', inplace=True):
        if '>' in line:
            new_line = line[1:-2] + '\t' + '9606' + '\t'
            sys.stdout.write(new_line)
        else:
            sys.stdout.write(line)
