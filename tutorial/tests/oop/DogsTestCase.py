import unittest
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
        self.assertNotEquals(my_schnauzer, my_dalmatian)

        self.assertTrue("Fido", my_schnauzer.name) # get name attribute
        self.assertTrue("Fido", my_schnauzer.get_name()) # get name function
        self.assertTrue("Chejs", my_dalmatian.get_name())
        self.assertTrue("mammal", my_dalmatian.species) # should be class object attribute
        self.assertTrue("mammal", Dog.species) # another way to access class object attributes

    # Make Dog inherit Animal and write the same test against Animal. Don't forget to call the super constructor and pass the Dog reference to Animal
    # Test if all Dog objects can eat if created this way
    # Overwrite eating method to return "I am a dog eating"

if __name__ == '__main__':
    unittest.main()
