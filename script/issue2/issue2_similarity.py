# !/usr/bin/evn python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def combin(m, n):

    if m < n:
        print "input wrong, m must bigger then n"
    else:
        fenmu = 1.0
        fenzi = 1.0
        for i in range(0, n):
            fenzi = fenzi * m
            m = m-1
        for i in range(0, n):
            fenmu = fenmu * (i + 1)

        return fenzi / fenmu


def similarity_element(n1, n2, c):
    """

    :param n1: Number of times of n1
    :param n2: Number of times of n2
    :param c:  n1 and n2 the common times in second column
    :return:
    """
    rate = 0
    for i in range(1, c):
        rate += ((combin(c, i)*combin(n1+n2-2*c, c-i))/combin(n1+n2-c, c))
    return 1 - rate


if __name__ == "__main__":
    print similarity_element(5, 6, 3)


