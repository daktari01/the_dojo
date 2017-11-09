import random

def get_random_room(room_dict, room_capacity):
        """Returns a random room that has available space"""
        # Pick a random key from the dictionary
        random_key = random.choice(list(room_dict))

        while room_capacity == len(room_dict[random_key]):
            random_key = random.choice(list(room_dict))
        return random_key


dict_A = {
    'red':[],
    'blue':[],
    'cyan':[],
    'magenta':[]
}

print(dict_A)
chosen_room = get_random_room(dict_A, 4)
print(chosen_room)

if len(dict_A[chosen_room]) > 4:
    chosen_room = get_random_room(dict_A, 4)

dict_A[chosen_room].append('Boy')
print(dict_A)
dict_A[chosen_room].append('Girl')
print(dict_A)
dict_A[chosen_room].append('Papa')
print(dict_A)
dict_A[chosen_room].append('Mama')
print(dict_A)
if len(dict_A[chosen_room]) > 4:
    chosen_room = get_random_room(dict_A, 4)
dict_A[chosen_room].append('Grandma')
print(dict_A)
dict_A[chosen_room].append('Grandpa')
print(dict_A)