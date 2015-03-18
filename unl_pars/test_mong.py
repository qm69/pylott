#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import pymongo
from pymongo import MongoClient

#  from pymongo import Connection
#  import bson

client = MongoClient("localhost", 27017)

db = client["pylott-dev"]
mong_keno = db["keno"]


def keno_draw(cont_draw):
    """
    Проверить наличие тиража в базе
    """
    try:
        temp = db.kenos.aggregate(
            {'draw': 5089}
        )
        # that return None if Exception
        return temp if temp else False
    except Exception:
        raise Exception("'keno_draw' что-то не так")
qwer = {
    'draw': 5090,
    'comp': 'unl',
    'date': 'qwdeqweqwe'
}
"""
{'_id': ObjectId('5509cb2eedce301277c7b9b6'), 'date': '17.03.2015',
'draw': 5089, 'comp': 'unl', 'game': 'keno',
'rslt': [53, 4, 61, 18, 74, 30, 49, 57, 13,], 'tron': ['5089', '2015-03-17']}
"""
rest = keno_draw(qwer)
print(rest)
