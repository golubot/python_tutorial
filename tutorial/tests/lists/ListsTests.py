import unittest
from tutorial.solutions.lists.ListOperations import concatenate_lists, concatenate_list_with_reverse_second_list, \
    concatenate_and_sort


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


if __name__ == '__main__':
    unittest.main()
