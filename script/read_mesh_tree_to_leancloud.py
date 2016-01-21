#!/usr/bin/python
# -*- coding: utf-8 -*-
import leancloud
from leancloud import Object


from mdat.config import APP_ID, APP_KEY


def read_mesh_tree():
    leancloud.init(APP_ID, APP_KEY)
    MESH = Object.extend('MESH')
    with open('../data/2016MeshTree.txt') as f:
        for line in f:
            if '.......' in line:
                items = line.strip(' \r\r\n').split('.'*43)
                mesh = MESH()
                mesh.set('tag', items[0])
                mesh.set('title', items[1])
                mesh.save()


if __name__ == '__main__':
    read_mesh_tree()
