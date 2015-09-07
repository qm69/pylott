#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from dateutil.parser import parse
from datetime import date, timedelta


""" Response {
    'Message': None,
    'Exception': None,
    'DrawType': 'Pick3Draw',
    'VideoUrls': 'https://nlotstoragemedia01.b ... 01-22T193A303A26Z'},
    'Succeeded': True
    'Data': {
        'Draw': {
            'Rank5Winners': 5,
            'Rank1Gains': 500.0,
            'Rank3Winners': 16,
            'Rank4Winners': 13,
            'Rank6Winners': 1294,
            'NextDraw': '2015-09-05T18:59:59',
            'Rank4Gains': 50.0,
            'Number1': 6,
            'Stats': None,
            'Rank2Winners': 0,
            'Number2': 3,
            'Id': 4953,
            'Number3': 0,
            'Results': [6, 3, 0],
            'GainDistribution': [
                {'Title': 'In volgorde', 'Gains': 500.0, 'Winners': 2},
                {'Title': 'In willekeurige volgorde met dubbels', 'Gains': 160.0, 'Winners': 0},
                {'Title': 'In willekeurige volgorde zonder dubbels', 'Gains': 80.0, 'Winners': 16},
                {'Title': 'Eerste 2', 'Gains': 50.0, 'Winners': 13},
                {'Title': 'Laatste 2', 'Gains': 50.0, 'Winners': 5},
                {'Title': 'Laatste cijfer', 'Gains': 1.0, 'Winners': 1294}
            ],
            'Rank6Gains': 1.0,
            'Rank1Winners': 2,
            'TotalMoney': 18928.0,
            'DrawDate': '2015-09-04T19:59:59',
            'Rank2Gains': 160.0,
            'Rank3Gains': 80.0,
            'Rank5Gains': 50.0
}   }   }
"""

game_name = dict(pick_3=['Pick3', 'Pick 3'], keno=['Keno', 'Keno'])


def get_resalts(game, dd):
    link = ('http://www.nationale-loterij.be/drawapi/draw/getdraw?' +
            'drawdate=' + dd + '&' +
            'brand=' + game_name[game][0] + '&' +
            'language=nl-BE')

    resp = requests.get(link).json()
    if resp['Data'] is None:
        return None
    data = dict(firm='Belgium', game=game_name[game][1])
    data['date'] = parse(resp['Data']['Draw']['DrawDate']) - timedelta(hours=2)

    rslt = resp['Data']['Draw']['Results']
    data['rslt'] = rslt
    data['srtd'] = sorted(rslt, key=lambda i: i)

    return data

if __name__ == '__main__':
    print(get_resalts('pick_3', '2015-08-12'))
