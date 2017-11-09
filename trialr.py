with open('members.txt') as file:
    mdict={}
    for line in file:
        a, b, c, d = line.strip().split(':')
        mdict[a] = b + ':' + c + ':' + d

a = input('ID: ')
if a not in mdict:
    print('ID {} not found'.format(a))
else:
    b, c, d = mdict[a].split(':')
    d = input('phone: ')
    mdict[a] = b + ':' + c + ':' + d  # update entry
    with open('members.txt', 'w') as file:  # rewrite file
        for id, values in mdict.items():
            file.write(':'.join([id] + values.split(':')) + '\n')