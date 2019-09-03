from tutorial.solutions.oop.Animal import Animal


class Dog(Animal):

    #class attributes
    species = "mammal"

    #instance attributes
    def __init__(self, breed, name, spots):
        super().__init__()
        self.breed = breed
        self.name = name
        self.spots = spots

    def get_name(self):
        return(self.name)

    def eat(self):
        return "I am a dog eating"