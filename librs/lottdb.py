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
db = client["pylott-dev"]


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

    """ save """
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
            raise Exception("LottDB.save_one() что-то не так")

    def save_many(self):
        print('LottDB.save_many() is dump function')

    def find_one(self, firm, date):
        """ find by date """
        try:
            # returns Document or None,
            return self.game.find_one({'firm': firm, 'date': date})
        except Exception:
            raise Exception("LottDB.find_one() что-то не так")

    def find_many(self, firm, amount):
        """ Find n last draws """
        try:
            return (self.game
                    .find({'firm': firm})
                    .sort('draw', -1)
                    .limit(amount))
        except Exception:
            raise Exception("LottDB.find() что-то не так")

    def find_last(self, firm, dt=None, draw=None):
        """ return Date() or Int() or None"""
        try:
            if dt:
                resp = (self.game.find({'firm': firm}, {'date': 1})
                                 .sort('date', -1)
                                 .limit(1))
                if resp.count() > 0:
                    # а если нет ???
                    return [resp[0]['date'], resp[0]['suit'][0]]
                else:
                    return None
            else:
                resp = (self.game.find({'firm': firm}, {'draw': 1})
                                 .sort('draw', -1)
                                 .limit(1))
                return resp[0]['draw'] if resp.count() > 0 else None

        except Exception:
            raise Exception("LottDB.find_last() что-то не так")

    """ updt """
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
            raise Exception("LottDB.updt_one() что-то не так")

    def updt_many(self):
        print('LottDB.updt_many() is dump function')

if __name__ == '__main__':
    triple = LottDB('triple')
    last_draw = triple.find_last('Florida', dt=True)
    print(last_draw)
    [print(f) for f in triple.find_many('Florida', 5)]
