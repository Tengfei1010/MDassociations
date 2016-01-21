#!/usr/bin/python
# -*- coding: utf-8 -*-
import leancloud

from mdat.db.base import DB
from mdat.config import APP_ID
from mdat.config import APP_KEY


class LeancloudDB(DB):
    def __init__(self):
        super(LeancloudDB, self).__init__()
        self.app_id = APP_ID
        self.app_key = APP_KEY

        # leancloud init
        leancloud.init(self.app_id, self.app_key)

    def delete_all(self, find):
        pass

    def save_to_db(self, data):
        pass

    def query_one(self, find):
        pass

    def update_all(self, find):
        pass

    def query_all(self, find):
        pass

    def update_one(self, find):
        pass

    def delete_one(self, find):
        pass
