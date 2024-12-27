def field(items, *args):
    assert len(args) > 0
    dict_list = []
    for s in range(len(items)):
        d = dict()
        for i in items[s].items():
            for j in args:
                if i[0] == j:
                    d[j] = i[1]
        dict_list.append(d)
    if len(args) == 1:
        for i in range(len(dict_list)):
            for j in args:
                print(dict_list[i][j],end = " ")
        print()
    else:
      print(*dict_list)


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

field(goods, 'title')
field(goods, 'title', 'price')