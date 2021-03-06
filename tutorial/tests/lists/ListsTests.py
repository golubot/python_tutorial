import unittest
from tutorial.solutions.lists.ListOperations import concatenate_lists, concatenate_list_with_reverse_second_list, \
    concatenate_and_sort, extract_even_elements, delete_even_elements, extract_every_third_element_using_slices, \
    delete_element_from_list_if_present


class ListConcatenationTestCase(unittest.TestCase):

    def test_list_concatenation(self):
        """
        Write implementation in tutorial.solutions.lists which will be tested by the test below
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]

        result = concatenate_lists(first_list, second_list)

        self.assertIsNotNone(result)
        self.assertEquals(7, len(result))
        self.assertEquals([1, 2, 3, 4, 11, 22, 33], result)

    def test_list_concatenation_with_empty_second_list(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        # write test
        self.assertEqual(True, False)

    def test_list_concatenation_with_empty_first_list(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        # write test
        self.assertEqual(True, False)

    def test_list_concatenation_with_two_empty_lists(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        # write test
        self.assertEqual(True, False)

    def test_list_concatenation_with_second_reversed(self):
        """
        Write implementation in tutorial.solutions.lists which will be tested by the test below
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]

        result = concatenate_list_with_reverse_second_list(first_list, second_list)

        self.assertIsNotNone(result)
        self.assertEquals(7, len(result))
        self.assertEquals([1, 2, 3, 4, 33, 22, 11], result)

    def test_reversed_input_lists_concatenated(self):
        """
        Fill the missing test and function implementation to make sure that the desired result is [4, 3, 2, 1, 33, 22, 11]
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]
        self.assertEqual(True, False)

    def test_sorted_list(self):
        """
        Write the implementation that tests the following function call
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]
        result = concatenate_and_sort(first_list, second_list)

        # Add result assertions here

        first_list = [ "a", "b", "c"]
        second_list = ["x", "i", "p"]
        result = concatenate_and_sort(first_list, second_list)

        # Add result assertions here

        first_list = [ "banana", "curiosity", "ana"]
        second_list = ["killed", "the", "cat"]
        result = concatenate_and_sort(first_list, second_list)

        # Add result assertions here

        self.assertEqual(True, False)

    def test_switch_elements_by_index(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """
        self.assertEqual(True, False)

    def test_extract_even_elements(self):
        seq = range(0, 100)
        input_list = list(seq)

        result = extract_even_elements(input_list)
        self.assertTrue(100, len(input_list))
        self.assertTrue(50, len(result))

        expected = range(0, 100, 2)
        self.assertEqual(result, list(expected))

    def test_delete_even_elements(self):
        seq = range(0, 100)
        input_list = list(seq)

        result = delete_even_elements(input_list)
        self.assertEqual(50, len(result))
        self.assertEqual(50, len(input_list))
        self.assertEqual(input_list, result)

    def test_extract_every_third_element(self):
        result = extract_every_third_element_using_slices(list(range(0, 100)))
        self.assertEqual(result, list(range(3, 100, 3)))

        result = extract_every_third_element_using_slices(list(range(0, 1)))
        self.assertEqual(result, list())

        result = extract_every_third_element_using_slices(list(range(0, 2)))
        self.assertEqual(result, list())

        result = extract_every_third_element_using_slices(list(range(0, 3)))
        self.assertEqual(result, list())

    def test_delete_element_from_list_if_present(self):
        input_list = ["john", "Doe", "foo"]
        self.assertEqual(["john", "Doe", "foo"], delete_element_from_list_if_present(input_list, "bar"))
        self.assertEqual(["john", "Doe", "foo"], delete_element_from_list_if_present(input_list, "Foo"))
        self.assertEqual(["john", "Doe", "foo"], delete_element_from_list_if_present(input_list, "FOO"))
        self.assertEqual(["john", "Doe"], delete_element_from_list_if_present(input_list, "foo"))
        self.assertEqual(2, len(input_list))


if __name__ == '__main__':
    unittest.main()
