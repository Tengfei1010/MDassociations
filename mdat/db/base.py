#!/usr/bin/python
# -*- coding: utf-8 -*-


class DB(object):
    def __init__(self):
        pass

    def save_to_db(self, data):
        raise NotImplementedError

    def query_one(self, find):
        raise NotImplementedError

    def query_all(self, find):
        raise NotImplementedError

    def delete_one(self, find):
        raise NotImplementedError

    def delete_all(self, find):
        raise NotImplementedError

    def update_one(self, find):
        raise NotImplementedError

    def update_all(self, find):
        raise NotImplementedError
