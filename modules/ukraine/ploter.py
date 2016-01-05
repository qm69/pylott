# %matplotlib inline

import collections
from itertools import groupby
import matplotlib.pyplot as plt

path = 'results/troika_1_4226.csv'
fail = open(path, 'r')
fail_data = fail.read().split('\n')
fail.closed

data_list = []
max_len = 0

temp_varb = 0

for index, line in enumerate(fail_data):
    draw = line.split(';')[0]
    """ [8, 4, 3] """
    balls = [int(b) for b in line.split(';')[4:7]]
    b1, b2, b3 = balls
    """
    # resp = 1 if 8 in balls or 9 in balls else 0
    resp = 1 if 8 in balls else 0
    if resp == 1:
        if max_len > 0.5:
            # print(max_len, line)
            max_len = 0
    else:  # меньше 7.5
        max_len += 1  # 3659
    """
    if 9 in balls:
        for item, count in collections.Counter(balls).items():
            if item == 9 and count > 1:
                print(draw, count, fail_data[index + 1].split(';')[4:7])
    # data_list.append(resp)
"""
# False for невыпад 8,9, а True for выпад
grouped = groupby(data_list, key=lambda n: n == 1)

nevypad = [len(list(numb)) for key, numb in grouped if key is False]
for n in nevypad:
    if n > 15:
        print(n)
"""
