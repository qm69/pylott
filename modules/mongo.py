#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import pymongo
# import bson
import json
from pymongo import MongoClient
# from bson.objectid import ObjectId
# from pymongo import Connection

client = MongoClient("localhost", 27017)

db = client["pylott-dev"]
mong_keno = db["keno"]


def keno_fone(draw, comp):
    """
    Проверить наличие тиража в базе
    """
    try:
        # Document or None
        return db.kenos.find_one(
            # '_id': ObjectId('5509cb2eedce301277c7b9b6'),
            {'draw': draw, 'comp': comp}
        )
    except Exception:
        raise Exception("'keno_draw' что-то не так")


def keno_save(draw_dict):
    """
    Сохранить в базу
    """
    try:
        return db.kenos.save(draw_dict)
    except Exception:
        raise Exception("'save_keno' что-то не так")


def keno_updt(numb, comp, type, data):
    """
    http://api.mongodb.org/python/2.6.3/
    api/pymongo/collection.html
    """
    print(json.dumps(data))
    try:
        return db.kenos.find_and_modify(
            query={"draw": numb, "comp": comp},
            update={"$set": {type: data}},
            upsert=False,
            sort=None,
            full_response=False
        )
    except Exception:
        raise Exception("'keno_updt' что-то не так")

if __name__ == "__main__":
    pass
