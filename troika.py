#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 'blue', 'green', 'yellow', 'magenta', 'red' # 'grey', 'white'
from termcolor import colored
from lottlibs.mongo_db import Troika
# from lottlibs.tabler import counter, one, odd, more, amount, summ

troika = Troika()
resp = troika.find_draws('УНЛ', 12)
rslt = [r['rslt'] for r in resp]

drawBalls = []
metaData = []
ballLine = []  # выпавшие шары
oneTwoTri = []
smallLarge = []  # наименьш и наибольш
neighbors = []  # + 1й > 2 & 1й > 3го; 1й, 2й & 3й
multiple = []  # кратный 2, 3, 4
oddEven = []  # чет и нечет
allWinAmnt = []  # к-во и сумма

