from person import Person


class Staff(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, reg_number, first_name, second_name, salary=70000):
        super().__init__(reg_number, first_name, second_name, salary)