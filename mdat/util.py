#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def split_mesh_tree_file(file_name):
    """
    读取16年的MeshTree的数据 保存到 Leancloud 数据库中
    :param file_name:
    :return:
    """
    if not os.path.exists(file_name):
        raise IOError('There is not MeshTree file.'
                      ' Please check your file path.')

    with open(file_name) as f:
        for line in f:
            if '.......' in line:
                items = line.strip(' \r\r\n').split('.' * 43)
