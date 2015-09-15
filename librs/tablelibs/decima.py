#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 'blue', 'green', 'yellow', 'magenta', 'red' # 'grey', 'white'
from termcolor import colored, cprint
from librs.lottdb import LottDB
from librs.tablelibs.helpers import counter, true_false, summ_amnt


def decima(company, dlina=12):
    # название колекции
    troika = LottDB('decima')
    resp = troika.find_many(company, dlina)

    meta_data = []
    draw_balls = []
    small_large = []  # наименьш и наибольш
    multiple = []  # кратный 2, 3, 4
    odd_even = []  # чет и нечет
    ball_rept = []  # ball repetetition
    bigger_forty = []
    odd_even_20 = []
    summ_by_10, summ_by_20, summ_by_40 = [], [], []

    last_draw = resp[0]['rslt']

    for r in resp:
        draw = r['rslt']
        sort_arr = sorted(draw)
        suma = sum(draw)
        keys = r.keys()

        """  meta data  """
        meta_data.append(' {} {} {} {}'.format(
            str(r['draw']) if 'draw' in r.keys() else '',
            r['date'].strftime("%d-%m-%Y"),
            r['suit'][0] if 'suit' in keys else '      ',
            r['suit'][1] if 'suit' in keys and len(r['suit']) == 2 else ''))

        """  draw balls  """
        draw_balls.append(' '.join([str(b) for b in draw]))

        """ ball repeats """
        temp_list = ''
        for r in range(0, 20):
            if draw[r] in last_draw:
                temp_list += colored(' 1', 'magenta')
            else:
                temp_list += colored(' 0', 'red')
        ball_rept.append(temp_list)

        """ small_large
         +  Наименьший выпавший номер: бол. (1.5) 2.34;  мен. (1.5) 1.63
         +  Наименьший выпавший номер: четный 1.60;  нечетный 2.40
         +  Наибольший выпавший номер : бол. (7.5) 1.63;  мен. (7.5) 2.34
         +  Наибольший выпавший номер: четный 2.40;  нечетный 1.60

         +  Сумма наименьшего и наибольшего из выпавших номеров: четная 1.98;  нечетная 1.86
         +  Сумма наименьшего и наибольшего из выпавших номеров: бол. (9.5) 2.40;  мен. (9.5) 1.60
         +  Разность наибольшего и наименьшего из выпавших номеров: четная 1.98;  нечетная 1.86
         -  Разность наибольшего и наименьшего из выпавших номеров: бол. (6.5) 2.24;  мен. (6.5) 1.68
        """
        smallest, largest = sort_arr[0], sort_arr[19]
        data_list_2 = [
            true_false('more', 'less', True in [d in [0, 1] for d in draw]),
            true_false('odds', 'even', smallest % 2 == 0),
            true_false('more', 'less', True in [d in [79, 80] for d in draw]),
            true_false('odds', 'even', largest % 2 == 0),
            counter(smallest + largest, 80.5, 'zero'),
            true_false('odds', 'even', (smallest + largest) % 2 == 0),
            counter(largest - smallest, 75.5, 'zero'),
            true_false('odds', 'even', (largest - smallest) % 2 == 0)]
        small_large.append(' '.join(data_list_2))

        """ odd_even
         +  Четных номеров выпадет больше, чем нечетных: да 1.92;  нет 1.92
         !  Четных и нечетных номеров выпадет поровну: да 2.56;  нет 1.54
         +  Из выпавших номеров сумма четных больше, чем сумма нечетных : да 2.26;  нет 1.67
         -  Из выпавших номеров сумма нечетных больше, чем сумма четных : да 1.76;  нет 2.11
         +  Ко-во выпавших четных номеров : 3 или 4 номера 1.92;  1 номер 2.55;  0 номеров 7.00
         +  Ко-во выпавших нечетных номеров : 3 или 4 номера 1.92;  1 номер 2.55;  0 номеров 7.00
         +  Сумма всех выпавших четных номеров: бол. (4.5) 1.75;  мен. (4.5) 2.13
         +  Сумма всех выпавших нечетных номеров : бол. (7.5) 2.02;  мен. (7.5) 1.83
        """
        odds_arr = [d for d in draw if d % 2 == 0]
        even_arr = [d for d in draw if d % 2 != 0]
        oddsSumm, evenSumm = sum(odds_arr), sum(even_arr)
        data_list_5 = [
            true_false('more', 'less', len(odds_arr) > len(even_arr)),
            true_false('more', 'less', oddsSumm > evenSumm),
            # добавить ничью, когда 2 на 2
            # counter(len(odd_arr), 1.5),
            # counter(len(even_arr), 1.5),
            # counter(oddsSumm, 7.5, 'zero'),
            # counter(evenSumm, 9.5, 'zero')
        ]
        odd_even.append(' '.join(data_list_5))

        """ multiple
         +  Хотя бы один из выпавших номеров кратен 2 (0-не кратное): да 1.22;  нет 4.44
         +  Сумма всех вып. ном. кратна 2 (0-не кратное): да 1.92;  нет 1.92
         +  Хотя бы один из выпавших номеров кратен 3 (0-не кратное): да 1.46;  нет 2.80
         +  Сумма всех вып. ном. кратна 3 (0-не кратное): да 2.88;  нет 1.44
         +  Хотя бы один из выпавших номеров кратен 4 (0-не кратное): да 1.97;  нет 1.88
         +  Сумма всех вып. ном. кратна 4 (0-не кратное): да 3.87;  нет 1.28
        """
        d15 = [d for d in draw if d > 0 and d % 15 == 0]
        d20 = [d for d in draw if d > 0 and d % 20 == 0]
        data_list_4 = [
            counter(len(d15), 0.5),
            true_false('m', 'u', suma % 2 == 0),
            counter(len(d20), 0.5),
            true_false('m', 'u', suma % 3 == 0)]
        multiple.append(' '.join(data_list_4))

        """ 1-20 больше 40.5 """
        data_list_9 = [colored('1', 'magenta') if d > 40.5 else colored('0', 'red') for d in draw]
        bigger_forty.append(' '.join(data_list_9))

        """ 1-20 чет/нечет """
        data_list_3 = [colored('1', 'magenta') if d % 2 == 0 else colored('0', 'red') for d in draw]
        odd_even_20.append(' '.join(data_list_3))

        """ all_win_amnt
         + Количество выпавших номеров от 1 до 40 включительно: бол. (10) 1.90 мен. (10) 1.90
         + Количество выпавших номеров от 41 до 80 включительно: бол. (10) 1.90 мен. (10) 1.90
         + Сумма всех выпавших номеров от 1 до 40 включительно: бол. (205) 1.90 мен. (205) 1.90
         + Сумма всех выпавших номеров от 41 до 80 включительно: бол. (605) 1.90 мен. (605) 1.90
        """
        data_list_8 = [
            summ_amnt(draw, 1, 40),
            summ_amnt(draw, 41, 80),
            summ_amnt(draw, 1, 40, 205.5),
            summ_amnt(draw, 41, 80, 605.5),
        ]
        summ_by_40.append((' {:>11} {:>11} {:>13} {:>13}').format(*data_list_8))
        """ all_win_amnt
         + количество выпавших номеров от 1 до 20 включительно: бол. (4.5) 1.58 мен. (4.5) 2.45
         + количество выпавших номеров от 21 до 40 включительно: бол. (4.5) 1.58 мен. (4.5) 2.45
         + количество выпавших номеров от 41 до 60 включительно: бол. (4.5) 1.58 мен. (4.5) 2.45
         + количество выпавших номеров от 61 до 80 включительно: бол. (4.5) 1.58 мен. (4.5) 2.45
         + Сумма всех выпавших номеров от 1 до 20 включительно: бол. (51.5) 1.91 мен. (51.5) 1.93
         + Сумма всех выпавших номеров от 21 до 40 включительно: бол. (152.5) 1.96 мен. (152.5) 1.88
         + Сумма всех выпавших номеров от 41 до 60 включительно: бол. (252.5) 1.96 мен. (252.5) 1.89
         + Сумма всех выпавших номеров от 61 до 80 включительно: бол. (352.5) 1.96 мен. (352.5) 1.89
        """
        data_list_6 = [
            summ_amnt(draw, 1, 20),
            summ_amnt(draw, 21, 40),
            summ_amnt(draw, 41, 60),
            summ_amnt(draw, 61, 80),
            summ_amnt(draw, 1, 20, 51.5),
            summ_amnt(draw, 21, 40, 152.5),
            summ_amnt(draw, 41, 60, 252.5),
            summ_amnt(draw, 61, 80, 352.5)
        ]
        summ_by_20.append((' {:>11}' * 4 + ' {:>13}' * 4).format(*data_list_6))

        """ all_win_10
         + Количество выпавших номеров от 1 до 10 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 11 до 20 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 21 до 30 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 31 до 40 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 41 до 50 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 51 до 60 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 61 до 70 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Количество выпавших номеров от 71 до 80 включительно: бол. (2.5) 2.00 мен. (2.5) 1.84
         + Сумма всех выпавших номеров от 1 до 10 включительно: бол. (13.5) 1.98 мен. (13.5) 1.86
         + Сумма всех выпавших номеров от 11 до 20 включительно: бол. (36.5) 1.91 мен. (36.5) 1.93
         + Сумма всех выпавших номеров от 21 до 30 включительно: бол. (56.5) 1.90 мен. (56.5) 1.94
         + Сумма всех выпавших номеров от 31 до 40 включительно: бол. (76.5) 1.90 мен. (76.5) 1.94
         + Сумма всех выпавших номеров от 41 до 50 включительно: бол. (96.5) 1.90 мен. (96.5) 1.94
         + Сумма всех выпавших номеров от 51 до 60 включительно: бол. (116.5) 1.90 мен. (116.5) 1.94
         + Сумма всех выпавших номеров от 61 до 70 включительно: бол. (136.5) 1.90 мен. (136.5) 1.94
         + Сумма всех выпавших номеров от 71 до 80 включительно: бол. (156.5) 1.90 мен. (156.5) 1.94
        """
        data_list_7 = [
            summ_amnt(draw, 1, 10),
            summ_amnt(draw, 11, 20),
            summ_amnt(draw, 21, 30),
            summ_amnt(draw, 31, 40),
            summ_amnt(draw, 41, 50),
            summ_amnt(draw, 51, 60),
            summ_amnt(draw, 61, 70),
            summ_amnt(draw, 71, 80),
            summ_amnt(draw, 1, 10, 13.5),
            summ_amnt(draw, 11, 20, 36.5),
            summ_amnt(draw, 21, 30, 56.5),
            summ_amnt(draw, 31, 40, 76.5),
            summ_amnt(draw, 41, 50, 96.5),
            summ_amnt(draw, 51, 60, 116.5),
            summ_amnt(draw, 61, 70, 136.5),
            summ_amnt(draw, 71, 80, 156.5),
        ]
        summ_by_10.append((' {:>11}' * 8 + ' {:>13}' * 8).format(*data_list_7))

    cprint(' draw    data    tron | [  0, 1 ] [  8, 9 ]    Summ   Diff  | odd/even  | %15 %20 ', 'blue', 'on_white')
    [print(' {} | {} | {} | {}'.format(meta_data[i], small_large[i], odd_even[i], multiple[i])) for i in range(dlina)]

    cprint(' {:^20} {:^32} {:^62}  '.format('by 40', 'by 20th', 'by 10th'), 'blue', 'on_white')
    [print(' {} | {} | {}'.format(summ_by_40[i], summ_by_20[i], summ_by_10[i])) for i in range(dlina)]

    cprint(' {:^40} {:^40} {:^40}  '.format('rept', '40.5', 'odd/even'), 'blue', 'on_white')
    [print(' {} | {} | {}'.format(ball_rept[i], bigger_forty[i], odd_even_20[i])) for i in range(dlina)]

if __name__ == '__main__':
    decima('УНЛ', 12)
