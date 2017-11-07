import random

room_capacity = 6

room_dict = {
    'red':['Odhiambo', 'Okumu', 'Okiya', 'Nyagem', 'Atiende', 'Onyi'],
    'blue':['Odhiambo', 'Okumu', 'Okiya', 'Nyagem'],
    'orange':['Odhiambo', 'Okumu', 'Okiya', 'Nyagem', 'Onyi'],
    'green':['Odhiambo', 'Okumu', 'Okiya', 'Nyagem', 'Onyi'],
    'purple':['Odhiambo', 'Okumu'],
    'cyan':['Odhiambo', 'Okumu', 'Okiya', 'Nyagem', 'Atiende', 'Onyi']
}

def get_random_room(room_dict, room_capacity):

    """Returns a random room that has available space"""
    # Pick a random key from the dictionary
    
    random_key = random.choice(list(room_dict))

    while room_capacity == len(room_dict[random_key]):
        random_key = random.choice(list(room_dict))
    return random_key
    
    

#print(get_random_room(room_dict, room_capacity))
#room_dict[random_key].append('Kenyaa')
room_to_add_to = get_random_room(room_dict, room_capacity)
room_dict[room_to_add_to].append('NYOFUUUUUUU')
#print(room_dict)
room_dict[room_to_add_to].append('PAKAAAAA')
#print(room_dict)
room_dict[room_to_add_to].append('KWENDAAAA')
room_dict[room_to_add_to].append('KWUNGUUU')
room_dict[room_to_add_to].append('KOPLUUU')
room_dict[room_to_add_to].append('KAKAAAAA')
print(room_dict)
#print(room_dict['red'])
#print(len(room_dict['red']))
