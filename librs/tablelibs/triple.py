#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored, cprint
from librs.lottdb import LottDB
from librs.tablelibs.helpers import counter, true_false, summ_amnt


def triple(company, dlina=12):

    troika = LottDB('triple')
    resp = troika.find_many(company, dlina)
    meta_data = []
    draw_balls = []
    ball_line = []     # выпавшие шары
    one_two_tri = []
    small_large = []   # наименьш и наибольш
    neighbors = []     # + 1й > 2 & 1й > 3го; 1й, 2й & 3й
    multiple = []      # кратный 2, 3, 4
    odd_even = []      # чет и нечет
    all_win_amnt = []  # к-во и сумма

    for r in resp:
        draw = r['rslt']
        sort_arr = sorted(draw)
        suma = sum(draw)
        keys = r.keys()
        ballOne, ballTwo, ballTri = draw

        """  meta data  """
        meta_data.append(' {} {} {} {}'.format(
            str(r['draw']) if 'draw' in r.keys() else '',
            r['date'].strftime("%d-%m-%Y"),
            r['suit'][0] if 'suit' in keys else '   ',
            r['suit'][1] if 'suit' in keys and len(r['suit']) == 2 else ''))

        """  draw balls  """
        draw_balls.append(' '.join([str(b) for b in draw]))

        """  ball_line  """
        tenth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # [0] * 10
        for d in draw:
            tenth[d] += 1
        clrd_line = [colored(str(n), 'magenta' if n > 0 else 'red') for n in tenth]
        ball_line.append(' ' .join(clrd_line))

        """ one_two_tri
         +  1-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92
         +  1-й номер: четный 1.92;  нечетный 1.92
         +  2-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92
         +  2-й номер: четный 1.92;  нечетный 1.92
         +  3-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92
         +  3-й номер: четный 1.92;  нечетный 1.92
        """
        data_list_8 = [
            counter(ballOne, 4.5, 'zero'),
            true_false('odds', 'even', ballOne % 2 == 0),
            counter(ballTwo, 4.5, 'zero'),
            true_false('odds', 'even', ballTwo % 2 == 0),
            counter(ballTri, 4.5, 'zero'),
            true_false('odds', 'even', ballTri % 2 == 0)]
        one_two_tri.append(' '.join(data_list_8))

        """ neighbors
         +  Выпадут соседние номера: да 2.19;  нет 1.71
         +  Выпадут совпадающие номера: да 3.43;  нет 1.33
         +  Первый выпавший номер больше, чем последний: да 2.13;  нет 1.75
         +  Первый выпавший номер больше, чем второй: да 2.13;  нет 1.75
        """
        neighbor = True in [(d + 1 in draw or d - 1 in draw) for d in draw]
        povtor = set([d for d in draw if draw.count(d) > 1])
        data_list_3 = [
            true_false('true', 'fals', neighbor),
            true_false('true', 'fals', True if povtor else False),
            colored('more' if ballOne > ballTwo else 'less' if ballOne < ballTwo else 'eqal',
                    'magenta' if ballOne > ballTwo else 'red' if ballOne < ballTwo else 'yellow'),
            colored('more' if ballOne > ballTri else 'less' if ballOne < ballTri else 'eqal',
                    'magenta' if ballOne > ballTri else 'red' if ballOne < ballTri else 'yellow')]
        neighbors.append(' '.join(data_list_3))

        """ small_large
         +  Наименьший выпавший номер: бол. (1.5) 2.34;  мен. (1.5) 1.63
         +  Наименьший выпавший номер: четный 1.60;  нечетный 2.40
         +  Наибольший выпавший номер : бол. (7.5) 1.63;  мен. (7.5) 2.34
         +  Наибольший выпавший номер: четный 2.40;  нечетный 1.60
         +  Сумма наименьшего и наибольшего из выпавших номеров: четная 1.98;  нечетная 1.86
         +  Сумма наименьшего и наибольшего из выпавших номеров: бол. (9.5) 2.40;  мен. (9.5) 1.60
         +  Разность наибольшего и наименьшего из выпавших номеров: четная 1.98;  нечетная 1.86
         +  Разность наибольшего и наименьшего из выпавших номеров: бол. (6.5) 2.24;  мен. (6.5) 1.68
        """
        smallest, largest = sort_arr[0], sort_arr[2]
        data_list_2 = [
            true_false('more', 'less', True in [d in [0, 1] for d in draw]),
            true_false('odds', 'even', smallest % 2 == 0),
            true_false('more', 'less', True in [d in [8, 9] for d in draw]),
            true_false('odds', 'even', largest % 2 == 0),
            counter(smallest + largest, 9.5, 'zero'),
            true_false('odds', 'even', (smallest + largest) % 2 == 0),
            counter(largest - smallest, 6.5, 'zero'),
            true_false('odds', 'even', (largest - smallest) % 2 == 0)]
        small_large.append(' '.join(data_list_2))

        """ odd_even
         +  Четных номеров выпадет больше, чем нечетных: да 1.92;  нет 1.92
         +  Из выпавших номеров сумма четных больше, чем сумма нечетных : да 2.26;  нет 1.67
         -  Из выпавших номеров сумма нечетных больше, чем сумма четных : да 1.76;  нет 2.11
         +  Ко-во выпавших четных номеров : 2 или 3 номера 1.92;  1 номер 2.55;  0 номеров 7.00
         +  Ко-во выпавших нечетных номеров : 2 или 3 номера 1.92;  1 номер 2.55;  0 номеров 7.00
         +  Сумма всех выпавших четных номеров: бол. (4.5) 1.75;  мен. (4.5) 2.13
         +  Сумма всех выпавших нечетных номеров : бол. (7.5) 2.02;  мен. (7.5) 1.83
        """
        odds_arr = [d for d in draw if d % 2 == 0]
        even_arr = [d for d in draw if d % 2 != 0]
        oddsSumm, evenSumm = sum(odds_arr), sum(even_arr)
        data_list_5 = [
            true_false('more', 'less', len(odds_arr) > len(even_arr)),
            true_false('more', 'less', oddsSumm > evenSumm),
            counter(len(odds_arr), 1.5),
            counter(len(even_arr), 1.5),
            counter(oddsSumm, 4.5, 'zero'),
            counter(evenSumm, 7.5, 'zero')]
        odd_even.append(' '.join(data_list_5))

        """ multiple
         +  Хотя бы один из выпавших номеров кратен 2 (0-не кратное): да 1.22;  нет 4.44
         +  Сумма всех вып. ном. кратна 2 (0-не кратное): да 1.92;  нет 1.92
         +  Хотя бы один из выпавших номеров кратен 3 (0-не кратное): да 1.46;  нет 2.80
         +  Сумма всех вып. ном. кратна 3 (0-не кратное): да 2.88;  нет 1.44
         +  Хотя бы один из выпавших номеров кратен 4 (0-не кратное): да 1.97;  нет 1.88
         +  Сумма всех вып. ном. кратна 4 (0-не кратное): да 3.87;  нет 1.28
        """
        d2 = [d for d in draw if d > 0 and d % 2 == 0]
        d3 = [d for d in draw if d > 0 and d % 3 == 0]
        d4 = [d for d in draw if d > 0 and d % 4 == 0]
        data_list_4 = [
            counter(len(d2), 0.5),
            true_false('m', 'u', suma % 2 == 0),
            counter(len(d3), 0.5),
            true_false('m', 'u', suma % 3 == 0),
            counter(len(d4), 0.5),
            true_false('m', 'u', suma % 4 == 0)]
        multiple.append(' '.join(data_list_4))

        """ all_win_amnt
         +  К-во вып. ном. от 0 до 3 включ: 2 или 3 номера 2.70;  1 номер 2.20;  0 номеров 4.40
         +  Сумма всех вып. ном. от 0 до 3 включ: бол. (1.5) 1.88;  мен. (1.5) 1.96
         +  К-во вып. ном. от 0 до 4 включ: 2 или 3 номера 1.90;  1 номер 2.55;  0 номеров 7.30
         +  Сумма всех вып. ном. от 0 до 4 включ: бол. (2.5) 1.75;  мен. (2.5) 2.13
         +  К-во вып. ном. от 0 до 5 включ: 3 номера 4.40;  2 номера 2.20;  0 или 1 номер 2.70
         +  К-во вып. ном. от 4 до 6 включ: 2 или 3 номера 4.40;  1 номер 2.20;  0 номеров 2.70
         +  Сумма всех вып. ном. от 4 до 6 включ: бол. (4.5) 1.88;  мен. (4.5) 1.96
         +  К-во вып. ном. от 4 до 9 включ: 3 номера 4.40;  2 номера 2.20;  0 или 1 номер 2.70
         +  К-во вып. ном. от 5 до 9 включ: 2 или 3 номера 1.90;  1 номер 2.55;  0 номеров 7.30
         +  Сумма всех вып. ном. от 5 до 9 включ : бол. (10.5) 1.98;  мен. (10.5) 1.86
         +  К-во вып. ном. от 7 до 9 включ: 2 или 3 номера 4.40;  1 номер 2.20;  0 номеров 2.70
         +  Сумма всех вып. ном. от 7 до 9 включ: бол. (7.5) 1.88;  мен. (7.5) 1.96
         +  Сумма всех вып. ном.: бол. (13.5) 1.92;  мен. (13.5) 1.92
        """
        data_list_6 = [
            summ_amnt(draw, 0, 3),
            summ_amnt(draw, 0, 3, 1.5),
            summ_amnt(draw, 0, 4),
            summ_amnt(draw, 0, 4, 2.5),
            summ_amnt(draw, 0, 5),
            summ_amnt(draw, 4, 6),
            summ_amnt(draw, 4, 6, 4.5),
            summ_amnt(draw, 4, 9),
            summ_amnt(draw, 5, 9),
            summ_amnt(draw, 5, 9, 10.5),
            summ_amnt(draw, 7, 9),
            summ_amnt(draw, 7, 9, 7.5),
            summ_amnt(draw, 0, 9, 13.5)]
        all_win_amnt.append(' '.join(data_list_6))

    upper = ' draw    data    tron| Balls | 0 1 2 3 4 5 6 7 8 9 |   1й      2й      3й    | Сос  Повт 1>2  1>3 '
    cprint(upper, 'blue', 'on_white')
    [print('{:>20} | {} | {} | {} | {}'.format(meta_data[i], draw_balls[i], ball_line[i], one_two_tri[i], neighbors[i])) for i in range(dlina)]

    lower = ' [  0, 1 ] [  8, 9 ]    Summ   Diff  |      odd / even     |Кратн 2, 3, 4| 0-3  0-4  n-m 4-6  5-9  7-9  all'
    cprint(lower, 'blue', 'on_white')
    [print(' {} | {} | {} | {}'.format(small_large[i], odd_even[i], multiple[i], all_win_amnt[i])) for i in range(dlina)]

if __name__ == '__main__':
    triple('УНЛ', 12)
