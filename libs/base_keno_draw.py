#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DrawCount(object):
    """
    Some Class
    """
    def __init__(self, draws, tirag):
        """
        Explenetion of inicialization
        """
        self.draws = draws
        self.draw = draws[0]
        self.chart = {
            'hot': [tirag, 0, 0],
            'odd': [tirag, 0, 0],
            'more': [tirag, 0, 0],
            'twenty': [tirag, 0, 0, 0, 0],
            'povtor': [tirag, 0],
            'active': [tirag, 0, 0],
            'rise': [tirag, 0, 0]
        }

    def ball_counter(self):
        #  потом данные брать из тиража из db.keno.balls
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
                position=position + 1,
                hot='',
                odd='',
                more='',
                twenty='',
                vypad='',
                active='',
                rise=''
            )

            # 1 Hot or Cold
            if (period[ball] <= 3.91):
                ball_data['hot'] = 'hot'
                self.chart['hot'][1] += 1
            elif (period[ball] >= 4.09):
                ball_data['hot'] = 'cold'
                self.chart['hot'][2] += 1
            else:
                ball_data['hot'] = 'neit'

            # 2 Odd or Even
            if (ball % 2 == 0):
                ball_data['odd'] = 'even'
                self.chart['odd'][1] += 1
            else:
                ball_data['odd'] = 'odd'
                self.chart['odd'][2] += 1

            # 3 More or Less
            if (ball % 2 == 0):
                ball_data['more'] = 'more'
                self.chart['more'][1] += 1
            else:
                ball_data['more'] = 'less'
                self.chart['more'][2] += 1

            # 4 First, Second, Third or Fourth
            if (ball > 0 and ball <= 20):
                ball_data['twenty'] = 'first'
                self.chart['twenty'][1] += 1
            elif (ball > 20 and ball <= 40):
                ball_data['twenty'] = 'second'
                self.chart['twenty'][2] += 1
            elif (ball > 40 and ball <= 60):
                ball_data['twenty'] = 'third'
                self.chart['twenty'][3] += 1
            else:
                ball_data['twenty'] = 'fourth'
                self.chart['twenty'][4] += 1

            # 5 Once, Twice, Threce, Fource or More
            # сколько раз подряд выпадал
            podr = self.podryad(ball)
            obj_podr = {
                0: 'once', 1: 'twice', 2: 'threce',
                3: 'fource', 4: 'fifce', 5: 'sixce'
            }

            ball_data['vypad'] = obj_podr[podr]
            if (ball_data['vypad'] != 'once'):
                self.chart['povtor'][1] += 1

            # 6 Active, Passive or Neit
            # active [1,1....]
            # passive [0,0,0,0,0,0]
            # neitr -> other
            repeat = self.activator(ball)
            if (repeat[0] == 1 and repeat[1] == 1):
                ball_data['active'] = 'active'
                self.chart['active'][1] += 1
            elif (sum(repeat) == 0):
                ball_data['active'] = 'passive'
                self.chart['active'][2] += 1
            else:
                ball_data['active'] = 'neit'

            # 7 Rise or Fall
            # 4.15 * 6 ~ 25 draws
            n = round(period[ball] * 6)
            res_map = self.reise_reise(ball, n)

            if (res_map >= 9):
                ball_data['rise'] = 'rise'
                self.chart['rise'][1] += 1
            if (res_map <= 3):
                ball_data['rise'] = 'fall'
                self.chart['rise'][2] += 1
            else:
                ball_data['rise'] = 'neit'

            balls.append(ball_data)

        return balls

    def get_chart(self):
        return self.chart

    def activator(self, ball):
        """
        как переписать в одну строку
        """
        rep_draws = self.draws[1:7]
        summ = []
        for d in rep_draws:
            if ball in d:
                summ.append(1)
            else:
                summ.append(0)

        return summ

    def podryad(self, ball):
        """
        как обединить с 'repeat_cntr'
        """
        draws = self.draws[1:8]
        summ = 0
        for draw in draws:
            if ball in draw:
                summ += 1
            else:
                return summ
        return summ

    def reise_reise(self, ball, n):
        """
        как обединить с 'repeat_cntr'
        """
        draws = self.draws[:n]
        summ = 0
        for draw in draws:
            if ball in draw:
                summ += 1
        return summ

    def booker(self):
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
            'summ': [s1, s2, s3],
            'first': [first, first_even, first_half],
            'last': [last, last_even, last_half],
            'lowest': [lowest, lowest_even, lowest_numb],
            'bigest': [bigest, bigest_even, bigest_numb]
        }
