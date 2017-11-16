list_a = ('Oluwafemi Sule - lacks office space', 'Cate Patterson - lacks office space')

for item in list_a:
    item = item.split()
    print('{} {} {}'.format(item[0], item[1], item[4]))