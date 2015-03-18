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
        temp = db.kenos.find_one(
            {"draw": cont_draw["draw"]},
            {"comp": cont_draw["comp"]}
        )
        print("\ntemp = {}\n".format(temp))
        #  that return None if Exception
        return True if temp else False
    except Exception:
        raise Exception("'keno_draw' что-то не так")


def save_keno(draw_data):
    """
    Сохранить в базу
    """
    try:
        resp = db.kenos.save(draw_data)
        return db.kenos.find_one({"_id": resp})
    except Exception:
        raise Exception("'save_keno' что-то не так")

if __name__ == "__main__":
    pass
