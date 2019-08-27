import unittest

from tutorial.solutions.dictionaries.DictionaryOperations import add_elements_if_number_of_elements_is_odd


class DictionaryTestCase(unittest.TestCase):

    def test_add_elements_on_odd_dict(self):
        test_dict = {'name': 'ford', 'make': 'mondeo', 'door_count': 5}
        is_added, number_of_added_elements = add_elements_if_number_of_elements_is_odd(test_dict,
                                                                                       {'engine_displacement': 2000})
        self.assertTrue(is_added)
        self.assertEqual(1, number_of_added_elements)
        self.assertEqual(test_dict, {'name': 'ford', 'engine_displacement': 2000, 'make': 'mondeo', 'door_count': 5})

    def test_add_elements_on_even_dict(self):
        """
        Write the test only. The subject of the test is to prove that when called add_elements_if_number_of_elements_is_odd()
        with even number of elements - it does not add it to the input dict.
        """
        self.assertEqual(True, False)

    def test_add_empty_dict(self):
        """
        Write the test only. The subject of the test is to prove that when called with empty dict there is no error
        in the implementation (the program won't brake)
        """
        self.assertEqual(True, False)

    def test_add_element_that_exist_in_input_dict(self):
        """
        Finish writing the test only. The subject of the test is to prove that when called with empty dict there is no
        error in the implementation
        """
        test_dict = {'name': 'ford', 'make': 'mondeo', 'door_count': 5}
        add_element = {'engine_displacement': 2000}
        is_added = True  # delete this
        self.assertFalse(is_added)

        self.assertEqual(True, False)  # delete this

    def test_add_elements_that_exist_in_input_dict(self):
        """
        Finish writing the test only. The subject of the test is to prove that when called with empty dict there is no
        error in the implementation
        """
        test_dict = {'name': 'ford', 'make': 'mondeo', 'door_count': 5}
        add_element = {'door_count': 5, 'engine_displacement': 2000,
                       'drivers': [{'name': 'john', 'surname': 'doe'}, {'name': 'jane', 'surname': 'doe'}]
                       }
        is_added = False  # delete this
        number_of_added_elements = -1  # delete this

        self.assertTrue(is_added)
        self.assertEqual(2, number_of_added_elements)


if __name__ == '__main__':
    unittest.main()
