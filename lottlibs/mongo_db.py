#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import bson
# import json
from pymongo import MongoClient
# для поиска по _id
# from bson.objectid import ObjectId
# from pymongo import Connection
""" from bson import tz_util
    offset timezone in minutes east from UTC.
    tz_util.FixedOffset(180, "Europe/Kiev")
    print(tz_util.utc)
"""

client = MongoClient("localhost", 27017)
db = client["mean-dev"]


class Troika(object):
    """docstring for Troika"""
    def __init__(self):
        self.troika = db['troika']

    def save(self, meta_data):
        """
            firm: 'УНЛ'
            game: 'Трійка'
            draw: 4024
            suit: ['А', 4]
            date: datetime.datetime( ... )
            resalt: [5, 7, 3]
        """
        try:
            return self.troika.save(meta_data)
        except Exception:
            raise Exception("Troika.save() что-то не так")

    def last_draw(self, firm):
        """ Returns Int of last Draw """
        try:
            resp = (self.troika
                    .find({'firm': firm}, {'draw': 1})
                    .sort('draw', -1)
                    .limit(1))
            # возвращает ноль если пусто и теребит все сюда
            return 4000 if resp.count() == 0 else resp[0]['draw']
        except Exception:
            raise Exception("Troika.last_draw() что-то не так")

    def find_draws(self, firm, amount):
        """ Find n last draws """
        try:
            return (self.troika
                    .find({'firm': firm})
                    .sort('draw', -1)
                    .limit(amount))
        except Exception:
            raise Exception("Troika.find() что-то не так")


class Keno(object):
    """docstring for Keno"""
    def __init__(self, arg):
        # super(Keno, self).__init__()
        self.keno = db['keno']

    def find(self, comp, draw):
        """ Проверить наличие тиража в базе """
        try:
            # Document or None # '_id': ObjectId('55 ... c6'),
            return self.keno.find_one({'draw': draw,
                                       'comp': comp})
        except Exception:
            raise Exception("'keno_draw' что-то не так")

    def keno_last(self, comp):
        """ Достать последний тираж """
        try:
            # Document or None
            return self.keno.find_one({
                '$query': {'comp': comp},
                '$orderby': {"draw": -1}
            })
        except Exception:
            raise Exception("'keno_last' что-то не так")

    def keno_save(self, draw_dict):
        """ Сохранить в базу """
        try:
            return self.keno.save(draw_dict)
        except Exception:
            raise Exception("'save_keno' что-то не так")

    def keno_updt(self, numb, comp, type, data):
        """ http://api.mongodb.org/python/2.6.3/
            api/pymongo/collection.html     """
        # print(json.dumps(data))
        try:
            return self.keno.find_and_modify(
                query={"draw": numb, "comp": comp},
                update={"$set": {type: data}},
                upsert=False,
                sort=None,
                full_response=False)
        except Exception:
            raise Exception("'keno_updt' что-то не так")

""" Quatro """
""" Quinta """
""" Sexta """

if __name__ == '__main__':

    trpl = Troika()
    last_draw = trpl.last_draw('УНЛ')
    find = trpl.find('УНЛ', 5)
    for f in find:
        print(f)
