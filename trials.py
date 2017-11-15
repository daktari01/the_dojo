dict_a = {
    'Mandela': ['David', 'Samuel', 'Turi'],
    'Machel':['Anne', 'Linet', 'Turi']
}
dict_b = {
    'Nyerere': ['Myles', 'Reginald', 'Booker'],
    'Obote':['Memo', 'Liliosa']
}

#person_name = 'Liliosa'

def load_people():
    with open('load_popo.txt', 'r') as load_file:
        for line in load_file:
            line = line.split() 
            print(line)
            
load_people()