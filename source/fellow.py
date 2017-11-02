from person import Person


class Fellow(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, reg_number, first_name, second_name, salary=40000, wants_accommodation=False):
        super().__init__(reg_number, first_name, second_name, salary)
        self.wants_accommodation = wants_accommodation