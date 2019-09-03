class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        return "I am an animal"

    def eat(self):
        return "I am eating"

    def get_name(self):
        raise NotImplementedError("Subclass must implement this abstract method")