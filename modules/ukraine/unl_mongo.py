#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import bson, json
import pymongo

# from pymongo import MongoClient

# from datetime import datetime
# from bson.objectid import ObjectId <- для поиска по _id
# from pymongo import Connection

client = pymongo.MongoClient("localhost", 27017)
lott_base = client["lott-test"]
"""
from bson import tz_util
offset timezone in minutes east from UTC.
tz_util.FixedOffset(180, "Europe/Kiev")
print(tz_util.utc)
"""


class Triples(object):
    """docstring for Triples"""
    def __init__(self):
        self.triples = lott_base['triples']

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
            return self.triples.save(meta_data)
        except Exception:
            raise Exception("Triples.save() что-то не так")

    def last_draw(self, firm):
        """ Returns Int of last Draw """
        try:
            resp = (self.triples
                    .find({'firm': firm}, {'draw': 1})
                    .sort('draw', -1)
                    .limit(1))
            # возвращает ноль если пусто и теребит все сюда
            return 4000 if resp.count() == 0 else resp[0]['draw']
        except Exception:
            raise Exception("Triples.last_draw() что-то не так")

    def find(self, firm, amount):
        """ Find n last draws """
        try:
            return (self.triples
                    .find({'firm': firm})
                    .sort('draw', -1)
                    .limit(amount))
        except Exception:
            raise Exception("Triples.find() что-то не так")


class Decemas(object):
    """docstring for Decemas"""
    def __init__(self):
        self.triples = lott_base['triples']

    def save(self, meta_data):
        """
            firm: 'УНЛ'
            game: 'Кено'
            draw: 4024
            suit: ['А', 4]
            date: datetime.datetime( ... )
            resalt: [5, 7, 3]
        """
        try:
            return self.triples.save(meta_data)
        except Exception:
            raise Exception("Triples.save() что-то не так")

    def last_draw(self, firm):
        """ Returns Int of last Draw """
        try:
            resp = (self.triples
                    .find({'firm': firm}, {'draw': 1})
                    .sort('draw', -1)
                    .limit(1))
            # возвращает ноль если пусто и теребит все сюда
            return 4000 if resp.count() == 0 else resp[0]['draw']
        except Exception:
            raise Exception("Triples.last_draw() что-то не так")

    def find(self, firm, amount):
        """ Find n last draws """
        try:
            return (self.triples
                    .find({'firm': firm})
                    .sort('draw', -1)
                    .limit(amount))
        except Exception:
            raise Exception("Triples.find() что-то не так")

""" Quater """
""" Quinta """
""" Sexta """

if __name__ == '__main__':

    trpl = Triples()
    last_draw = trpl.last_draw('УНЛ')
    find = trpl.find('УНЛ', 5)
    for f in find:
        print(f)
