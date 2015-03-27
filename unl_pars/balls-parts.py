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


draw_data = [
    [int(n) for n in r.split(",")]
    if len(r) > 11 else r
    for r in line_data.split(";")
]
