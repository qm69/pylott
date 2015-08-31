#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import bson
# import json
from pymongo import MongoClient
""" для поиска по _id
    from bson.objectid import ObjectId
    from pymongo import Connection
    from bson import tz_util
    offset timezone in minutes east from UTC.
    tz_util.FixedOffset(180, "Europe/Kiev")
    print(tz_util.utc)
"""

client = MongoClient("localhost", 27017)
db = client["mean-dev"]


class LottDB(object):
    """docstring for Keno"""
    def __init__(self, game):
        """ troika > 3 x 10
            quatro > 4 x 10
            quinta > 5 x N
            sextra > 6 x N
            decima > 20 x 80
        """
        self.game = db[game]

    def save_one(self, draw_dict):
        """ firm: 'УНЛ'
            game: 'Трійка'
            draw: 4024
            suit: ['А', '4']
            date: datetime.datetime(2015, 8, 21, 23, 0)
            resalt: [5, 7, 3]
        """
        try:
            return self.game.save(draw_dict)
        except Exception:
            raise Exception("Keno.save_one() что-то не так")

    def save_many(self):
        pass

    def find_draw(self, firm, draw):
        """ Проверить наличие тиража в базе """
        try:
            # returns Document or None,
            return self.game.find_one({'firm': firm, 'draw': draw})
        except Exception:
            raise Exception("Keno.find_one() что-то не так")

    def find_many(self, firm, amount):
        """ Find n last draws """
        try:
            return (self.game
                    .find({'firm': firm})
                    .sort('draw', -1)
                    .limit(amount))
        except Exception:
            raise Exception("Troika.find() что-то не так")

    def last_draw(self, firm):
        """ Достать последний тираж """
        try:
            # Document or None
            resp = (self.game
                    .find({'firm': firm}, {'draw': 1})
                    .sort('draw', -1)
                    .limit(1))
            return resp[0]['draw'] if resp.count() > 0 else 0
        except Exception:
            raise Exception("Keno.last_draw() что-то не так")

    def last_date(self, firm):
        """ Достать последний тираж """
        try:
            # Document or None
            resp = (self.game
                    .find({'firm': firm}, {'date': 1})
                    .sort('date', -1)
                    .limit(1))
            return resp[0]['date'] if resp.count() > 0 else '17/12/23'
        except Exception:
            raise Exception("Keno.last_draw() что-то не так")

    def updt_one(self, firm, numb, tipe, data):
        # api.mongodb.org/python/2.6.3/api/pymongo/collection.html
        try:
            return self.game.find_and_modify(
                query={"draw": numb,
                       "firm": firm},
                update={"$set": {tipe: data}},
                upsert=False,
                sort=None,
                full_response=False)
        except Exception:
            raise Exception("'keno_updt' что-то не так")

    def updt_many(self):
        pass

if __name__ == '__main__':
    """
    troika = LottDB('troika')
    last_draw = troika.find_last('УНЛ')
    find = troika.find_many('УНЛ', 5)
    for f in find:
        print(f)
    """
    decima = LottDB('decima')
    last_draw = decima.find_last('УНЛ')
    find = decima.find_many('УНЛ', 5)
    for f in find:
        print(f)
