'''
import random


def get_random_room(self, room_dict, room_capacity):
    """Returns a random room"""
    # Pick a random key from the dictionary
    
    random_key = random.choice(list(room_dict))
    while room_capacity == len(room_dict[random_key]):
        random_key = random.choice(list(room_dict))
    return random_key
'''

'''
def check_available_space(room_dict, room_capacity): # Remember to add self
    return any(room_capacity > len(values) for values in room_dict.values())
            

dict_a = {
    'boy': ['David', 'Samuel', 'Turi'],
    'girl':['Anne', 'Linet', 'Turi']
}
dict_b = {
    'boy': ['David', 'Samuel', 'Turi'],
    'girl':['Anne', 'Linet']
}

print(check_available_space(dict_a, 3)) #False
print(check_available_space(dict_b, 3)) #True

#pairs = { 'word1':0, 'word2':0, 'word3':2000, 'word4':64, 'word5':0, 'wordn':8 }
#print(any(v > 0 for v in pairs.values()))
'''
dict_a = {
    'Mandela': ['David', 'Samuel', 'Turi'],
    'Machel':['Anne', 'Linet', 'Turi']
}
dict_b = {
    'Nyerere': ['Myles', 'Reginald', 'Booker'],
    'Obote':['Memo', 'Liliosa']
}

#person_name = 'Liliosa'

def check_person_in_room(person_name, room_dict):
    for room_name, name_list in room_dict.items():
        for name in name_list:
            if person_name == name:
                return room_name
        return False

print(check_person_in_room('Liliosa', dict_b))

def check_which_room_person_is(person_name, room_dict):
    for room_name, name_list in room_dict.items():
        if person_name in name_list:
            return room_name
    return False
        
print(check_which_room_person_is('Liliosa', dict_b))
        
#def get_person_current_room()
def room_has_space(self, capacity):
    pass

office1 = ['Juja', 'Njoro', 'Ruiru']

print(len(office1))