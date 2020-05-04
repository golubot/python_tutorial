class Dog():

    species = "mammal"

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots

    def get_name(self):
        return self.name