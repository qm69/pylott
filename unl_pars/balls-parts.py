        #############################
        # unl > keno > balls-parts: #
        #############################
        elif args['balls-parts']:

with open('results/keno.csv', 'r') as keno_file:

    # create a list of lists like
    # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
    draw_list = [
        [
            [int(n) for n in r.split(",")]
            if len(r) > 11 else r for r in res.split(";")
        ]
        for res in keno_file.read().split('\n')
    ]

    # if draw == None ...
    draw_numb = int(draw_list[0][0])
    bc = ball_counter(draw_list, draw_numb)
    pc = part_counter(draw_list, draw_numb)
    resp = keno_updt(draw_numb, comp="unl", type="balls", data=bc)
    pesp = keno_updt(draw_numb, comp="unl", type="tenth", data=pc)
    print(len(resp))
    print(len(pesp))


"""
{'n4': 0, 'all_prize': '0', 'n20': 0, 'n7': 0, 'ndraw': 1, 'n9': 0, 'n3': 0, 'year': None,
'n16': 0, 'n14': 0, 'n5': 0, 'n1': 0, 'day_name': None, 'n15': 0, 'amonth_name': None,
'pdraw': -1, 'n17': 0, 'n10': 0, 'month_name': None, 'n13': 0, 'lototron': None, 'n19': 0,
'n12': 0, 'ballset': None, 'n8': 0, 'all_humans': '0 <span>штук</span>', 'n18': 0,
'draw': None, 'n2': 0, 'month': None,
'copy_label': 'Щоб скопіювати комбінацію натисніть Ctrl+c, а потім Enter',
'n11': 0, 'n6': 0, 'day': None}
"""
