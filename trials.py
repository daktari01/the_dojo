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

print("Hello")
a = str(print("Hello"))
print(a)