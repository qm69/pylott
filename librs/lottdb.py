#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import bson
# import json
""" для поиска по _id
    from bson.objectid import ObjectId
    from pymongo import Connection
    from bson import tz_util
    offset timezone in minutes east from UTC.
    tz_util.FixedOffset(180, "Europe/Kiev")
    print(tz_util.utc)
"""
from pymongo import MongoClient

""" https://mongolab.com
    Account name: qm69    Username: qm69
    Email: qm69@ua.fm     Password: saturn69
    DBUser: qm69          DBpass: balalajka7
"""
MONGODB_URI = "mongodb://qm69:balalajka7@ds047474.mongolab.com:47474/lottbase"
client = MongoClient(MONGODB_URI)
db = client.get_default_database()


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
                        .sort('date', -1)
                        .limit(amount))
        except Exception:
            raise Exception("LottDB.find() что-то не так")

    def find_last(self, firm, field, suit=None):
        """ Smth about this function

        Agruments:
            firm  >> str:
            field >> str: 'draw' or 'date'
            suit  >> bool:

        Returns:
            Smth
        """
        if field not in ['draw', 'date']:
            raise Exception("Такого поля нету")
        try:
            resp = self.game.find_one({'firm': firm}, sort=[('date', -1)])
            if resp:
                if field == 'date':
                    if suit:
                        # find_last('Florida', field='draw', suit=True)
                        return [resp['date'].date(), resp['suit'][0]]
                    else:
                        # find_last('Florida', field='date')
                        return resp['date'].date()
                else:
                    if suit:
                        # find_last('Florida', field='draw', suit=True)
                        return [resp['draw'], resp['suit'][0]]
                    else:
                        # find_last('Florida', field='date')
                        return resp['draw']
            else:
                return None

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
    triple = LottDB('decima')
    draw_dict = {
        'firm': 'УНЛ',
        'game': 'Кено',
        'draw': 5300,
        'suit': ['А', '4'],
        'resalt': [5, 7, 3]
    }
    triple.save_one(draw_dict)
