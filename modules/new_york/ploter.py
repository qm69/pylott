from itertools import groupby
# import matplotlib.pyplot as plt

path = 'results/numbers.csv'
fail = open(path, 'r')
fail_data = fail.read().split('\n')
fail.closed

data_list = []
max_len = 0

for line in fail_data:
    draw_date = line[0]
    """ [8, 4, 3] """
    ball_list = line.split(';')[2].split('-')
    balls = [int(b) for b in ball_list]
    b1, b2, b3, b4 = balls

    resp = 1 if 0 in balls or 1 in balls else 0
    data_list.append(resp)

resp = [list(t)for k, t in groupby(data_list, lambda x: x > 0)]
# new_arr = [r for r in resp if r[0] == 1]

for n in resp:
    smth = len(n) if n[0] == 1 else -len(n)
    print(smth)