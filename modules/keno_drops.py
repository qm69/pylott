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
            [...
                ['5018', '2015-01-05', 'B', '2', [64, 48, .. , 26, 65],
            ...]

            tirag @ int: number of draw
        ==============================================
        get_charts @ dict: {
            hots: [5043, 4, 3],       # hot or cold
            even: [5043, 13, 7],      # odd or even
            half: [5043, 9, 11],      # by halfs
            twel: [5043, 4, 5, 6, 5], # by twelves
            rept: [5043, 3],          # repeats
            actv: [5043, 2, 4],       # active and passive
            rise: [5043, 1, 2],       # on rise and fall
        }
        """
        self.draws = [d[4] for d in draws]
        self.draw = draws[0][4]
        self.chart = {
            'hots': [tirag, 0, 0],
            'even': [tirag, 0, 0],
            'half': [tirag, 0, 0],
            'twel': [tirag, 0, 0, 0, 0],
            'rept': [tirag, 0],
            'actv': [tirag, 0, 0],
            'rise': [tirag, 0, 0]
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
            ball: 46, @ int  # ball
            plac: 12, @ int  # place
            temp: 'cold',    # temperature
            even: 'even',    # odd or even
            half: 'last',    # by halfs
            twen: 'third',   # by twelves
            rept: 'twice',   # repeat or not
            actv: 'passive', # active
            rise: 'neit'     # rise or fall
        }
        """
        balls = []

        for position, ball in enumerate(self.draw):

            ball_data = dict(
                ball=ball,
                plac=position + 1,
                temp='',
                even='',
                half='',
                twen='',
                rept='',
                actv='',
                rise=''
            )

            # 1. Hot or Cold
            # 'hot', 'cold' or 'neit'
            if (period[ball] <= 3.91):
                ball_data['temp'] = 'hot'
                self.chart['hots'][1] += 1
            elif (period[ball] >= 4.09):
                ball_data['temp'] = 'cold'
                self.chart['hots'][2] += 1
            else:
                ball_data['temp'] = 'neit'

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

            # 4. by twenty
            # 'first', 'second', 'third' or 'fourth'
            if (ball > 0 and ball <= 20):
                ball_data['twen'] = 'first'
                self.chart['twel'][1] += 1
            elif (ball > 20 and ball <= 40):
                ball_data['twen'] = 'second'
                self.chart['twel'][2] += 1
            elif (ball > 40 and ball <= 60):
                ball_data['twen'] = 'third'
                self.chart['twel'][3] += 1
            else:
                ball_data['twen'] = 'fourth'
                self.chart['twel'][4] += 1

            # 5. Number of zrepeated dropping of the ball
            # 'once', 'twice', 'threce',
            # 'fource', 'fifce' or 'sixce'
            in_row = self.__serializer(ball, 'repetitation', 7)
            obj_in_row = {
                0: 'once', 1: 'twice', 2: 'threce',
                3: 'fource', 4: 'fifce', 5: 'sixce',
                6: 'sevence'
            }

            ball_data['rept'] = obj_in_row[in_row]
            if (ball_data['rept'] != 'once'):
                self.chart['rept'][1] += 1

            # 6. Active or passive
            # active  -> [1,1....]
            # passive -> [0,0,0,0,0,0]
            # neitral -> other
            # 'active', 'passive' or 'neit'
            in_serie = self.__serializer(ball, 'active', 8)
            if (in_serie[0] == 1 and in_serie[1] == 1):
                ball_data['actv'] = 'active'
                self.chart['actv'][1] += 1
            elif (sum(in_serie) == 0):
                ball_data['actv'] = 'passive'
                self.chart['actv'][2] += 1
            else:
                ball_data['actv'] = 'neit'

            # 7. Rise or fall
            # 4.15 * 6 ~ 25 draws
            # 'rise', 'fall', 'neit'
            n = round(period[ball] * 6)
            res_map = self.__serializer(ball, 'rise', n)

            if (res_map >= 9):
                ball_data['rise'] = 'rise'
                self.chart['rise'][1] += 1
            if (res_map <= 3):
                ball_data['rise'] = 'fall'
                self.chart['rise'][2] += 1
            else:
                ball_data['rise'] = 'neit'

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
        Returns @ dict:
            {
                totl: [648, 215, 432],        # totals
                frst: [38, 'odd', 'lower'],   # first
                last: [43, 'even', 'higher'], # last
                lowe: [1, 'even', 'true'],    # lowest
                bige: [78, 'odd', 'false']    # bigest
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
            'totl': [s1, s2, s3],
            'frst': [first, first_even, first_half],
            'last': [last, last_even, last_half],
            'lowe': [lowest, lowest_even, lowest_numb],
            'bige': [bigest, bigest_even, bigest_numb]
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
