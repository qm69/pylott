#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest

# http://stackoverflow.com/questions/714063/
# Add the ptdraft folder path to the sys.path list
sys.path.append('/home/qm69/code/python/lottery')
from libs.base_keno_draw import DrawCount

res_arr = [
    [65, 26, 14, 49, 51, 63, 47, 31, 61, 69, 25, 70, 24, 78, 74, 21, 77, 2, 18, 56], [65, 42, 7, 38, 17, 45, 44, 74, 11, 69, 21, 43, 37, 64, 3, 59, 70, 36, 57, 31], [19, 10, 24, 36, 3, 59, 55, 74, 37, 14, 4, 5, 6, 9, 30, 62, 58, 33, 45, 52], [9, 22, 54, 49, 7, 56, 18, 50, 17, 27, 72, 65, 24, 53, 1, 36, 23, 42, 26, 4], [22, 49, 56, 42, 79, 55, 51, 73, 16, 7, 34, 32, 70, 6, 53, 23, 26, 54, 40, 75], [45, 23, 34, 26, 73, 22, 5, 80, 55, 3, 78, 46, 49, 7, 58, 72, 24, 28, 21, 9], [48, 73, 79, 30, 18, 53, 42, 57, 44, 25, 65, 50, 3, 75, 20, 11, 8, 45, 43, 14], [9, 33, 19, 43, 3, 66, 34, 44, 75, 47, 18, 60, 59, 13, 41, 61, 11, 4, 57, 71], [26, 24, 55, 73, 45, 63, 2, 5, 49, 75, 76, 18, 12, 71, 65, 31, 8, 72, 79, 52], [63, 52, 16, 39, 78, 28, 50, 62, 26, 17, 1, 6, 57, 45, 68, 59, 46, 9, 66, 15], [53, 72, 24, 58, 49, 34, 75, 67, 62, 56, 41, 16, 51, 55, 60, 63, 73, 23, 22, 19], [79, 23, 10, 29, 49, 33, 26, 25, 27, 22, 9, 5, 18, 37, 28, 43, 36, 78, 7, 14], [64, 48, 79, 70, 40, 69, 20, 59, 66, 61, 80, 53, 78, 57, 28, 13, 76, 72, 26, 65], [57, 65, 66, 36, 77, 20, 51, 59, 71, 79, 50, 52, 15, 49, 62, 47, 80, 6, 69, 54], [28, 5, 21, 61, 4, 54, 11, 73, 42, 31, 71, 38, 9, 48, 24, 20, 63, 27, 50, 58], [33, 71, 13, 56, 19, 24, 3, 25, 1, 30, 63, 18, 35, 76, 7, 49, 74, 75, 48, 16], [26, 65, 38, 4, 11, 48, 75, 23, 34, 6, 68, 27, 31, 14, 74, 80, 67, 54, 20, 19], [61, 76, 42, 54, 75, 55, 10, 46, 40, 14, 15, 73, 52, 59, 26, 51, 71, 8, 11, 33], [54, 68, 7, 6, 14, 69, 51, 59, 79, 55, 65, 2, 73, 75, 13, 39, 17, 21, 74, 35], [68, 23, 65, 39, 62, 4, 52, 73, 5, 15, 3, 31, 29, 59, 79, 34, 75, 26, 41, 40], [23, 20, 11, 49, 9, 32, 41, 37, 74, 36, 55, 43, 33, 60, 72, 21, 12, 46, 59, 35], [67, 8, 38, 74, 25, 44, 33, 5, 70, 53, 15, 14, 40, 4, 18, 79, 24, 56, 28, 65], [14, 39, 78, 80, 42, 33, 28, 61, 13, 3, 35, 69, 9, 11, 15, 29, 57, 17, 7, 26], [3, 12, 30, 65, 28, 34, 4, 79, 62, 77, 40, 76, 5, 67, 59, 18, 58, 35, 27, 48], [42, 68, 32, 76, 63, 14, 21, 50, 3, 77, 52, 75, 71, 25, 41, 67, 55, 31, 13, 35], [6, 10, 64, 5, 55, 77, 29, 48, 35, 30, 16, 73, 47, 36, 27, 25, 50, 17, 53, 78], [24, 51, 31, 43, 25, 27, 2, 46, 61, 11, 45, 80, 17, 47, 13, 15, 74, 53, 8, 1], [61, 24, 26, 65, 35, 78, 38, 34, 66, 31, 77, 80, 37, 16, 13, 44, 76, 6, 67, 72], [57, 69, 77, 51, 56, 49, 19, 2, 33, 50, 74, 70, 65, 1, 79, 43, 27, 64, 3, 35], [56, 57, 7, 43, 4, 38, 22, 32, 68, 74, 29, 58, 73, 50, 44, 8, 28, 2, 61, 11]]


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.draws = res_arr
        draw_init = DrawCount(self.draws, '4568')
        self.balls = draw_init.ball_counter()
        self.chart = draw_init.get_chart()
        self.bookies = draw_init.booker()

    def test_ball_counter(self):
        # smth in the dark
        self.assertEqual(len(self.balls), 20)
        for ball in self.balls:
            # 1 Hot or Cold
            val_hot = ['hot', 'cold', 'neit']
            self.assertIn(ball['hot'], val_hot)

            # 2 Odd or Even
            self.assertIn(ball['odd'], ['odd', 'even'])

            # 3 More or Less
            self.assertIn(ball['more'], ['more', 'less'])

            # 4 First, Second, Third or Fourth
            twenty_val = ['first', 'second', 'third', 'fourth']
            self.assertIn(ball['twenty'], twenty_val)

            # 5 Once, Twice, Threce, Fource or More
            rep_val = ['once', 'twice', 'threce', 'fource', 'fifce', 'sixce']
            self.assertIn(ball['vypad'], rep_val)

            # 6 Active, Passive or Neit
            act_val = ['active', 'passive', 'neit']
            self.assertIn(ball['active'], act_val)

            # 7 Rise or Fall
            rise_val = ['rise', 'fall', 'neit']
            self.assertIn(ball['rise'], rise_val)

    def test_get_chart(self):
        # 'hot'

        # 'odd'
        sum_odd = sum(self.chart['odd'][1:])
        self.assertEqual(sum_odd, 20)

        # 'more'
        sum_more = sum(self.chart['more'][1:])
        self.assertEqual(sum_more, 20)

        # 'twenty'
        sum_twenty = sum(self.chart['twenty'][1:])
        self.assertEqual(sum_twenty, 20)

        # 'povtor'

        # 'active'

        # 'rise'
        self.assertLess(self.chart['rise'][1], 20)
        self.assertLess(self.chart['rise'][2], 20)

    def test_booker(self):
        # summ from 61 - 80
        self.assertLess(self.bookies['summ'][2], 1331)
        # summ of first and second halfs == total summ
        two_halfs = self.bookies['summ'][0] + self.bookies['summ'][1]
        self.assertEqual(two_halfs, self.bookies['summ'][2])

        for k, v in self.bookies.items():
            if (k != 'summ'):
                self.assertGreater(v[0], 0)
                self.assertLess(v[0], 81)
                self.assertNotEqual(v[1], '')
                self.assertNotEqual(v[2], '')

if __name__ == '__main__':
    unittest.main()
