# the_dojo

[![CircleCI](https://circleci.com/gh/daktari01/the_dojo.svg?style=svg)](https://circleci.com/gh/daktari01/the_dojo)
[![Maintainability](https://api.codeclimate.com/v1/badges/f7da29e64a716b46a869/maintainability)](https://codeclimate.com/github/daktari01/the_dojo/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f7da29e64a716b46a869/test_coverage)](https://codeclimate.com/github/daktari01/the_dojo/test_coverage)


The Dojo Project - Andela

The Dojo is program that ensures fair distribution of resources to avoid wastage.

### Requiremts

Before setting up the project, ensure that you have the following:

1. A working Opertating System (UNIX/LINUX or MAC preferred)
2. Python3 installed in your computer

### How To Set Up

The setup below will work for UNIX/LINUX and MAC users. If you are running Windows,
kindly liase with your adminstrator to help you set up the program.

1. Navigate to the folder you want the project in.
2. Download or clone it by running the command:   
`git clone https://github.com/daktari01/the_dojo.git`
3. Install the virtual environment:  
`pip3 install virtualenv`
4. Change directory to the program folder and run:  
`virtualenv -p python3 venv`
5. Activate the virtual environment:  
`source venv/bin/activate`
6. Install requirements in your virtual environment:  
`pip3 install -r requirements.txt`


### How To Use 

1. __Launch the program by running:__    
`python3 app.py`

2. __To get a list of commands, run:__    
`help`

3. __To create one or more rooms, run:__   
`create_room <room_type> <room_name> ...`

__Examples__   
    a. `create room office Mandela Machel`   
        The above command creates offices called 'Mandela' and 'Machel'   
    b. `create room living Freedom Longonot`
        The above command creates living spaces called 'Freedom' and 'Longonot'   

4. __To add people, run:__   
`add_person <first_name>  <second_name> (FELLOW|STAFF) [wants_accommodation]`   

__Examples__   
    a. `add_person John Doe FELLOW Y`   
        The above command adds a new person called 'John Doe' who wants accomodation.
        'John Doe' will be assigned an office space and living space automatically if they are available.
        Fellows are allocated living spaces only if they want by adding the `Y`.
    b. `add_person Jane Doe FELLOW`   
        The above command adds a new person called 'Jane Doe' who does not want accomodation.
        'Jane Doe' will be assigned an office space automatically if it is available.
        Fellows are by default not given living spaces, unless they want it by adding the `Y`.
    c. `add_person Harry Winks STAFF`   
        The above command adds a new person called 'Harry Winks'.
        'Harry Winks' will be assigned an office space automatically if it is available.
        Staff cannot be allocated living spaces.

5. __To see the people in a specific room, run:__   
`print_room <room_name>`   

__Examples__
    a. `print_room Mandela`   
        The above command prints a list of the people in 'Mandela' office   
    b. `print_room Longonot`   
        The above command prints a list of the people in 'Longonot' living room   
      
6. __To see all the people and the rooms they have been allocated, run:__   
`print_allocations [-o=filename]`   

__Examples__   
    a. `print_allocations`   
        The above command prints to the screen all people and the various rooms they have been allocated.   
    b. `print_allocations -o`   
        The above command prints to a text file all people and the various rooms they have been allocated.   
        The file can be found at `./files/allocations.txt`   

7. __To see all the people who have not been allocated rooms, run:__   
`print_unallocated [-o=filename]`   
Persons added are allocated rooms automatically.   
However, if by the time the person was added, either all rooms were full, or no room had been created, the person(s) added will not be allocated rooms.    

__Examples__   
    a. `print_unallocated`   
        The above command prints to the screen all people who have not been allocated rooms.   
    b. `print_allocations -o`   
        The above command prints to a text file all people who have not been allocated rooms.   
        The file can be found at `./files/unallocated.txt`   

### How To Contribute

1. Create a branch    
`git checkout -b samplebranch`
2. Make changes as deemed necessary    
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/)

### Licence

The program has [MIT Licence](https://github.com/daktari01/the_dojo/blob/master/LICENSE)


### Contributors

1. [James Dindi](https://github.com/daktari01)





