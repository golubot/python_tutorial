class Dog():

    #class attributes
    species = "mammal"

    #instance attributes
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def get_name(self):
        return(self.name)




