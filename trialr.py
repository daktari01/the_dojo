dict_A = {
    'red':['Morris', 'Roy'],
    'blue':['Oliver', 'Otos', 'Justo'],
    'cyan':['Kipsangui'],
    'magenta':['Eunice', 'Kenga', 'Galo', 'Orkoiyot']
}
'''
dict_from_file = {}
dict_A = {
    'red':['Morris', 'Roy'],
    'blue':['Oliver', 'Otos', 'Justo'],
    'cyan':['Kipsangui'],
    'magenta':['Eunice', 'Kenga', 'Galo', 'Orkoiyot']
}

fout = "members.txt"
fout_r = "members_r.txt"
fo = open(fout, "w")
fo_r = open(fout_r, "w")

for k, v in dict_A.items():
    fo.write(str(k) + '\n' + ' ---------------------------------------- '+ '\n' + str(v) + '\n\n')
    fo_r.write(str(k) + ' = ' + str(v) + '\n')
fo_r.close()
fo.close()


with open('members_r.txt') as f:
    for line in f:
        k, v = line.strip().split(' = ')
        dict_from_file[k.strip()] = v.strip()

f.close()
print(dict_from_file)
'''
def write_read_dict_text(dict_to_read, write_file, read_file):
    dict_from_file = {}
    fout = write_file
    fout_r = read_file
    fo = open(fout, "w")
    fo_r = open(fout_r, "w")
    
    for k, v in dict_to_read.items():
        fo.write(str(k) + '\n' + ' ---------------------------------------- '+ '\n' + str(v) + '\n\n')
        fo_r.write(str(k) + ' = ' + str(v) + '\n')
    fo_r.close()
    fo.close()
    
    
    with open(read_file) as f:
        for line in f:
            k, v = line.strip().split(' = ')
            dict_from_file[k.strip()] = v.strip()
    
    f.close()
    return dict_from_file
    
dict_b = write_read_dict_text(dict_A, 'trias.txt', 'trias_r.txt')
print(dict_b)
    

