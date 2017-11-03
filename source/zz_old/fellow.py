from person import Person


class Fellow(Person):
    """Class Fellow inheriting from Person"""
    wants_accommodation = False
    def __init__(self, person_name):
        super().__init__(person_name)
        
fello = Fellow('Kaka')
print(fello.wants_accommodation)
        