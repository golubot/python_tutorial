import unittest

from tutorial.solutions.oop.Animal import Animal
from tutorial.solutions.oop.Dog import Dog


class MyTestCase(unittest.TestCase):

    def test_dogs(self):
        """
        Create dog class that will be used to instantiate different dog objects.
        """
        my_schnauzer = Dog(breed="Schnauzer", name="Fido", spots=False)
        type(my_schnauzer)
        my_dalmatian = Dog(breed="Dalmatian", name="Chejs", spots=True)
        type(my_dalmatian)
        self.assertNotEqual(my_schnauzer, my_dalmatian)

        self.assertEqual("Fido", my_schnauzer.name) # get name attribute
        self.assertEqual("Fido", my_schnauzer.get_name()) # get name function
        self.assertEqual("Chejs", my_dalmatian.get_name())
        self.assertEqual("mammal", my_dalmatian.species) # should be class object attribute
        self.assertEqual("mammal", Dog.species) # another way to access class object attributes

    # Make Dog inherit Animal and write the same test against Animal. Don't forget to call the super constructor and pass the Dog reference to Animal

    def test_dog_from_animals(self):
    # Test if all Dog objects can eat if created this way
        my_rottweiler = Dog("Rottweiler", "Butch", False)
        my_boxer = Dog("Boxer", "Vane", True)

        self.assertEqual("I am a dog eating", my_rottweiler.eat())
        self.assertEqual("I am a dog eating", my_boxer.eat())
    # Overwrite eating method to return "I am a dog eating"

    def test_animal(self):
        my_lion = Animal()

        self.assertEqual("I am eating", my_lion.eat())
        self.assertRaises(NotImplementedError, my_lion.get_name)

if __name__ == '__main__':
    unittest.main()
