'''
import random

def get_random_room(room_dict, room_capacity):
        """Returns a random room that has available space"""
        # Pick a random key from the dictionary
        random_key = random.choice(list(room_dict))

        while room_capacity == len(room_dict[random_key]):
            random_key = random.choice(list(room_dict))
        return random_key

'''
dict_A = {
    'red':['Samuel', 'Luke', 'Jonathan', 'Myles'],
    'blue':['Morris', 'Jason'],
    'cyan':['Eunice', 'Joan', 'Peter', 'Festus', 'Ezra'],
    'magenta':['Hannah', 'Joseph']
}
dict_B = {
    'blak':['Jillo', 'Mloi', 'Ryan', 'Sarah'],
    'brown':['Ann', 'John'],
    'grey':['Eric', 'Irene', 'Andreas', 'Kerian', 'Tony'],
    'white':['Fellaini', 'Romeo']
}
'''
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

'''
'''
# Remove person from unallocated list
file_allocated = open('./files/all_pple_unallocated_office.txt', 'r')
allocated_lines = file_allocated.readlines
file_allocated.close()
file_allocated = open('./files/all_pple_unallocated_office.txt', 'w')
for line in allocated_lines:
    if line != person_name + "\n":
        file_allocated.write(line)
file_allocated.close()
'''
# ##remember to compare len(dict[person_name]) to be less than 6 before allocating. 
# If it is >= 6, pick another random room 
# ##add the person to allocated list


'''
# Add people from fellow.txt file and staff.txt to get all_people.txt
filenames = [fellow_path, staff_path]
with open(all_people_path, 'w') as all_people_file:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                all_people_file.write(line)
all_people_file.close()
'''
'''
def write_to_dict(dict_to_read_a, dict_to_read_b, write_file):
    fout = write_file
    fo_w = open(fout, "w")
    fo_a = open(fout, "a")
    
    for key, value in dict_to_read_a.items():
        fo_w.write(str(key).upper() + '\n' + ' ---------------------------------------- '+ '\n' + str(', '.join(value)) + '\n\n')
    for key, value in dict_to_read_b.items():
        fo_a.write(str(key).upper() + '\n' + ' ---------------------------------------- '+ '\n' + str(', '.join(value)) + '\n\n')
    fo_a.close()
    fo_w.close()
    
    
write_to_dict(dict_A, dict_B, 'members.txt')

'''
#dict_C = dict_B.update(dict_B)


dict_C = dict(dict_A, **dict_B)
print(dict_C)