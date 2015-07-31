#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DropCount(object):
    """
    This is my first class written @ Python 3.4
    """
    def __init__(self, draws, tirag):
        """
        Arguments:

            draws @ list: len == 30 >> list >> int; like:
            ['5018', '2015-01-05', 'B', '2', [64, 48, .. , 26, 65],

            tirag @ int: number of draw

        get_charts @ dict: {
            temp: [5043, 4, 3],          # hot or cold
            even: [5043, 13, 7],         # odd or even
            half: [5043, 9, 11],         # by halfs
            twenty: [5043, 4, 5, 6, 5],  # by twentytys
            repeat: [5043, 3],           # repeats
            active: [5043, 2, 4],        # active and passive
            hot: [5043, 1, 2],           # on hot and fall
        }
        """
        self.draws = [d[4] for d in draws]
        self.draw = draws[0][4]
        self.chart = {
            'temp': [tirag, 0, 0],
            'even': [tirag, 0, 0],
            'half': [tirag, 0, 0],
            'twentyty': [tirag, 0, 0, 0, 0],
            'repeat': [tirag, 0],
            'active': [tirag, 0, 0],
            'vector': [tirag, 0, 0]
        }

    def get_balls(self):
        # TODO: take data about the period in DB
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
        """
        get_balls @ list > @ dict: len == 20 {
            ball: 46, @ int     # ball
            seat: 12, @ int     # seate
            temp: 'cold',       # temperature
            even: 'even',       # odd or even
            half: 'last',       # by halfs
            twenty: 'third',    # by twentytyves
            repeat: 'twice',    # repeat or not
            active: 'passive',  # active
            vector: 'inert'      # hot or fall
        } """
        balls = []

        for position, ball in enumerate(self.draw):

            ball_data = dict(
                ball=ball,
                seat=position + 1,
                temp='',
                even='',
                half='',
                twenty='',
                repeat='',
                active='',
                vector='')

            # 1. Hot or Cold
            # 'hot', 'cold' or 'inert'
            if (period[ball] <= 3.91):
                ball_data['temp'] = 'hot'
                self.chart['temp'][1] += 1
            elif (period[ball] >= 4.09):
                ball_data['temp'] = 'cold'
                self.chart['temp'][2] += 1
            else:
                ball_data['temp'] = 'inert'

            # 2. Even or odd
            # 'even' or 'odd'
            if (ball % 2 == 0):
                ball_data['even'] = 'even'
                self.chart['even'][1] += 1
            else:
                ball_data['even'] = 'odd'
                self.chart['even'][2] += 1

            # 3. More or Less
            # 'last' or 'first'
            if (ball % 2 == 0):
                ball_data['half'] = 'last'
                self.chart['half'][1] += 1
            else:
                ball_data['half'] = 'first'
                self.chart['half'][2] += 1

            # 4. by twentyty
            # 'first', 'second', 'third' or 'fourth'
            if (ball > 0 and ball <= 20):
                ball_data['twenty'] = 'first'
                self.chart['twentyty'][1] += 1
            elif (ball > 20 and ball <= 40):
                ball_data['twenty'] = 'second'
                self.chart['twentyty'][2] += 1
            elif (ball > 40 and ball <= 60):
                ball_data['twenty'] = 'third'
                self.chart['twentyty'][3] += 1
            else:
                ball_data['twenty'] = 'fourth'
                self.chart['twentyty'][4] += 1

            # 5. Number of zrepeated dropping of the ball
            # 'once', 'twice', 'threce', 'fource', 'fifce', 'sixce'
            in_row = self.__serializer(ball, 'repetitation', 7)
            obj_in_row = {0: 'once', 1: 'twice', 2: 'threce',
                          3: 'fource', 4: 'fifce', 5: 'sixce',
                          6: 'sevence'}

            ball_data['repeat'] = obj_in_row[in_row]
            if (ball_data['repeat'] != 'once'):
                self.chart['repeat'][1] += 1

            # 6. Active or passive
            # active  -> [1, 1....]
            # passive -> [0, 0, 0, 0, 0, 0]
            # inert -> other
            # 'active', 'passive' or 'inert'
            in_serie = self.__serializer(ball, 'active', 8)
            if (in_serie[0] == 1 and in_serie[1] == 1):
                ball_data['active'] = 'active'
                self.chart['active'][1] += 1
            elif (sum(in_serie) == 0):
                ball_data['active'] = 'passive'
                self.chart['active'][2] += 1
            else:
                ball_data['active'] = 'inert'

            # 7. vector: hot or fall
            # 4.15 * 6 ~ 25 draws
            # 'hot', 'fall', 'inert'
            n = round(period[ball] * 6)
            res_map = self.__serializer(ball, 'hot', n)

            if (res_map >= 9):
                ball_data['vector'] = 'rise'
                self.chart['vector'][1] += 1
            if (res_map <= 3):
                ball_data['vector'] = 'fall'
                self.chart['vector'][2] += 1
            else:
                ball_data['vector'] = 'inert'

            """
            # 8. Chart -> Tenth for parts.py
            tenth = int(math.floor((ball - 1) / 10)) + 1
            self.chart['tens'][tenth] += 1
            """
            # End: append ball data to the balls list
            balls.append(ball_data)

        return balls

    def get_charts(self):

        return self.chart

    def get_odds(self):
        """
        Returns @ dict: {
            totals: [648, 215, 432],       # totals
            first: [38, 'odd', 'lower'],   # first
            last: [43, 'even', 'higher'],  # last
            least: [1, 'even', 'true'],    # lowest
            most: [78, 'odd', 'false']     # bigest
        } """
        draw = self.draw

        # add css classes for summ lower or bigger for coloring
        s1 = sum(list(filter(lambda x: x < 41, draw)))
        s2 = sum(list(filter(lambda x: x > 40, draw)))
        s3 = sum(draw)

        first = draw[0]
        first_even = 'even' if (first % 2 == 0) else 'odd'
        first_half = 'under' if (first < 41) else 'over'

        last = draw[19]
        last_even = 'even' if (last % 2 == 0) else 'odd'
        last_half = 'under' if (last < 41) else 'over'

        draw_sort = sorted(draw)

        lowest = draw_sort[0]
        lowest_even = 'even' if (lowest % 2 == 0) else 'odd'
        lowest_numb = 'under' if (lowest < 3) else 'over'

        bigest = draw_sort[19]
        bigest_even = 'even' if (bigest % 2 == 0) else 'odd'
        bigest_numb = 'under' if (bigest > 78) else 'over'

        return dict(totals=[s1, s2, s3],
                    first=[first, first_even, first_half],
                    last=[last, last_even, last_half],
                    least=[lowest, lowest_even, lowest_numb],
                    most=[bigest, bigest_even, bigest_numb])

    # private_methos
    def __serializer(self, ball, tip, n):
        """
        internal function for counting
        5: povtor
        6: active/passive
        7: hot/fall
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
        elif tip == 'hot':
            return sum(series)
