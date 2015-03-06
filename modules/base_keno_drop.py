#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class DropCount(object):
    """ This is my first class written @ Python 3.4

    Arguments:

        draws @ list: len == 30 >> list >> int; like:
        [...
            [64,48,79,70,40,69,20,59,66,61,80,53,78,57,28,13,76,72,26,65],
        ...]

        tirag @ int: number of draw
    """
    def __init__(self, draws, tirag):
        """
        Explanation of initialization
        """
        self.draws = draws
        self.draw = draws[0]
        self.chart = {
            'hots': [tirag, 0, 0],
            'evens': [tirag, 0, 0],
            'halves': [tirag, 0, 0],
            'twentys': [tirag, 0, 0, 0, 0],
            'repeats': [tirag, 0],
            'actives': [tirag, 0, 0],
            'rising': [tirag, 0, 0],
            'tenth': [tirag, 0, 0, 0, 0, 0, 0, 0, 0]
        }

    def get_balls(self):
        """
        Returns:
            ball @ list: len == 20 >> dict:
            {
                ball: 46, @ int
                place: 12, @ int
                hot: 'cold',
                even: 'even',
                half: 'last',
                twenty: 'third',
                repeat: 'twice',
                active: 'passive',
                rise: 'neit'
            }
        """
        # THEN data about the period of ball
        # TAKE from the db.keno.balls
        period = [
            0,
            3.87, 3.94, 3.92, 4.01, 4.02, 3.90, 4.05, 4.14, 3.94, 3.74,
            4.10, 4.13, 4.21, 4.19, 4.24, 4.15, 4.14, 3.94, 4.09, 4.12,
            3.96, 3.96, 4.01, 3.90, 3.91, 3.98, 3.95, 3.97, 3.82, 4.01,
            4.01, 4.10, 4.07, 3.97, 3.92, 3.99, 4.03, 4.14, 4.04, 3.92,
            4.01, 3.94, 3.95, 3.99, 4.23, 3.99, 3.99, 4.07, 4.14, 4.06,
            4.02, 3.87, 3.92, 4.12, 4.04, 4.04, 3.94, 3.91, 3.91, 3.93,
            3.86, 3.82, 3.77, 3.96, 3.92, 3.86, 3.92, 3.84, 3.87, 3.93,
            4.25, 3.94, 4.04, 4.04, 4.13, 4.07, 4.17, 3.94, 4.28, 4.10
        ]

        balls = []

        for position, ball in enumerate(self.draw):

            ball_data = dict(
                ball=ball,
                place=position + 1,
                hot='',
                even='',
                half='',
                twenty='',
                repeat='',
                active='',
                rise=''
            )

            # 1 Hot or Cold
            # 'hot', 'cold' or 'neit'
            if (period[ball] <= 3.91):
                ball_data['hot'] = 'hot'
                self.chart['hots'][1] += 1
            elif (period[ball] >= 4.09):
                ball_data['hot'] = 'cold'
                self.chart['hots'][2] += 1
            else:
                ball_data['hot'] = 'neit'

            # 2 Even or odd
            # 'even' or 'odd'
            if (ball % 2 == 0):
                ball_data['even'] = 'even'
                self.chart['evens'][1] += 1
            else:
                ball_data['even'] = 'odd'
                self.chart['evens'][2] += 1

            # 3 More or Less
            # 'last' or 'first'
            if (ball % 2 == 0):
                ball_data['half'] = 'last'
                self.chart['halves'][1] += 1
            else:
                ball_data['half'] = 'first'
                self.chart['halves'][2] += 1

            # 4 by twenty
            # 'first', 'second', 'third' or 'fourth'
            if (ball > 0 and ball <= 20):
                ball_data['twenty'] = 'first'
                self.chart['twentys'][1] += 1
            elif (ball > 20 and ball <= 40):
                ball_data['twenty'] = 'second'
                self.chart['twentys'][2] += 1
            elif (ball > 40 and ball <= 60):
                ball_data['twenty'] = 'third'
                self.chart['twentys'][3] += 1
            else:
                ball_data['twenty'] = 'fourth'
                self.chart['twentys'][4] += 1

            # 5 Number of zrepeated dropping of the ball
            # 'once', 'twice', 'threce',
            # 'fource', 'fifce' or 'sixce'
            in_row = self.__serializer(ball, 'repetitation', 7)
            obj_in_row = {
                0: 'once', 1: 'twice', 2: 'threce',
                3: 'fource', 4: 'fifce', 5: 'sixce'
            }

            ball_data['repeat'] = obj_in_row[in_row]
            if (ball_data['repeat'] != 'once'):
                self.chart['repeats'][1] += 1

            # 6 Active or passive
            # active  -> [1,1....]
            # passive -> [0,0,0,0,0,0]
            # neitral -> other
            # 'active', 'passive' or 'neit'
            in_serie = self.__serializer(ball, 'active', 8)
            if (in_serie[0] == 1 and in_serie[1] == 1):
                ball_data['active'] = 'active'
                self.chart['actives'][1] += 1
            elif (sum(in_serie) == 0):
                ball_data['active'] = 'passive'
                self.chart['actives'][2] += 1
            else:
                ball_data['active'] = 'neit'

            # 7 Rise or fall
            # 4.15 * 6 ~ 25 draws
            # 'rise', 'fall', 'neit'
            n = round(period[ball] * 6)
            res_map = self.__serializer(ball, 'rise', n)

            if (res_map >= 9):
                ball_data['rise'] = 'rise'
                self.chart['rising'][1] += 1
            if (res_map <= 3):
                ball_data['rise'] = 'fall'
                self.chart['rising'][2] += 1
            else:
                ball_data['rise'] = 'neit'

            # 8 Chart -> Tenth for parts.py
            tenth = int(math.floor((ball - 1) / 10)) + 1
            self.chart['tenth'][tenth] += 1

            # End: append ball data to the balls list
            balls.append(ball_data)

        return balls

    def get_charts(self):
        """
        Returns:
            self.chart @ dict:
            {
                hots: [5043, 4, 3],
                evens: [5043, 13, 7],
                halves: [5043, 9, 11],
                twentys: [5043, 4, 5, 6, 5],
                repeats: [5043, 3],
                actives: [5043, 2, 4],
                rising: [5043, 1, 2],
                tenth: [5043, 2, 3, 4, 1, 3, 2, 1, 4]
            }
        """
        return self.chart

    def get_odds(self):
        """
        Returns:
            @ dict:
            {
                totals: [648, 215, 432],
                first: [38, 'odd', 'lower'],
                last: [43, 'even', 'higher'],
                lowest: [1, 'even', 'true'],
                bigest: [78, 'odd', 'false']
            }
        """
        draw = self.draw
        # add css classes for summ lower or bigger for coloring
        s1 = sum(list(filter(lambda x: x < 41, draw)))
        s2 = sum(list(filter(lambda x: x > 40, draw)))
        s3 = sum(draw)

        first = draw[0]
        first_even = 'even' if (first % 2 == 0) else 'odd'
        first_half = 'lower' if (first < 41) else 'higher'

        last = draw[19]
        last_even = 'even' if (last % 2 == 0) else 'odd'
        last_half = 'lower' if (last < 41) else 'higher'

        draw_sort = sorted(draw)

        lowest = draw_sort[0]
        lowest_even = 'even' if (lowest % 2 == 0) else 'odd'
        lowest_numb = 'true' if (lowest < 3) else 'false'

        bigest = draw_sort[19]
        bigest_even = 'even' if (bigest % 2 == 0) else 'odd'
        bigest_numb = 'true' if (bigest > 78) else 'false'

        return {
            'totals': [s1, s2, s3],
            'first': [first, first_even, first_half],
            'last': [last, last_even, last_half],
            'lowest': [lowest, lowest_even, lowest_numb],
            'bigest': [bigest, bigest_even, bigest_numb]
        }

    # private_methos
    def __serializer(self, ball, tip, n):
        """
        internal function for counting
        5: povtor
        6: active/passive
        7: rise/fall
        """
        series = []
        for draw in self.draws[1:n]:
            if ball in draw:
                series.append(1)
            else:
                series.append(0)
        if tip == 'repetitation':
            return sum(series)
        elif tip == 'active':
            return series
        elif tip == 'rise':
            return sum(series)
