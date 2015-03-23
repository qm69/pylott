#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import pymongo
# import bson
from pymongo import MongoClient
from bson.objectid import ObjectId
# from pymongo import Connection


client = MongoClient("localhost", 27017)

db = client["pylott-dev"]
mong_keno = db["keno"]


def keno_draw():
    """
    Проверить наличие тиража в базе
    """
    try:
        # return db.kenos.find_one({'draw': 5089, 'comp': 'unl'})
        return db.kenos.find_one(
            {'_id': ObjectId('5509cb2eedce301277c7b9b6')}
        )
    except Exception:
        raise Exception("'keno_draw' что-то не так")

"""
{'_id': ObjectId('5509cb2eedce301277c7b9b6'), 'date': '17.03.2015',
'draw': 5089, 'comp': 'unl', 'game': 'keno',
'rslt': [53, 4, 61, 18, 74, 30, 49, 57, 13,], 'tron': ['5089', '2015-03-17']}

for doc in keno_draw(qwer):
    print(doc)
"""
print(keno_draw())
