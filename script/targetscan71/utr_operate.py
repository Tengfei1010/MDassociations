#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def utr_operate(in_path, out_path):
    """

    :return:
    """
    all_line = []
    with open(out_path, 'w') as f_out:
        with open(in_path, 'r') as f_in:
            for line in f_in:

                if '>' in line:
                    line = line.strip('\n\r')
                    temp = line.lstrip('>')
                    new_line = temp + '9606\n'
                    f_out.write(new_line)

                else:
                    f_out.write(line)


if __name__ == "__main__":
    utr_operate('/home/wtq/Downloads/targetscan/UTR_original.txt', '/home/wtq/Downloads/targetscan/new_utr.txt')

