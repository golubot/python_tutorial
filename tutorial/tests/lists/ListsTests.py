import unittest
from tutorial.solutions.lists.ListOperations import concatenate_lists, concatenate_list_with_reverse_second_list, \
    concatenate_and_sort, concatenate_list_from_reverse_input_lists, switch_list_elements_by_index


class ListConcatenationTestCase(unittest.TestCase):

    def test_list_concatenation(self):
        """
        Write implementation in tutorial.solutions.lists which will be tested by the test below
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]

        result = concatenate_lists(first_list, second_list)

        self.assertIsNotNone(result)
        self.assertEqual(7, len(result))
        self.assertEqual([1, 2, 3, 4, 11, 22, 33], result)

    def test_list_concatenation_with_empty_second_list(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        name_list = ["Ana", "Vanja", "Dora", "Kalina"]
        empty_list = []

        return_list = concatenate_lists(name_list, empty_list)

        self.assertEqual(return_list, ["Ana", "Vanja","Dora", "Kalina"])
        self.assertEqual(len(return_list), len(name_list))

    def test_list_concatenation_with_empty_first_list(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        empty_list = []
        friends_list = ["Rachel", "Ross", "Monika", "Phoebe", "Joey", "Chandler"]

        return_from_method = concatenate_lists(empty_list, friends_list)

        self.assertEqual(return_from_method, friends_list)
        self.assertEqual(len(return_from_method), len(friends_list))

    def test_list_concatenation_with_two_empty_lists(self):
        """
        Test should be simple enough if you follow the above for guidance.
        """

        empty_list_to_start = []
        empty_list_to_concatenate = []

        returned_list = concatenate_lists(empty_list_to_start, empty_list_to_concatenate)

        self.assertEqual(0, len(returned_list))
        self.assertEqual([], returned_list)

    def test_list_concatenation_with_second_reversed(self):
        """
        Write implementation in tutorial.solutions.lists which will be tested by the test below
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]

        result = concatenate_list_with_reverse_second_list(first_list, second_list)

        self.assertIsNotNone(result)
        self.assertEqual(7, len(result))
        self.assertEqual([1, 2, 3, 4, 33, 22, 11], result)

        self.assertEqual([11, 22, 33], second_list)

    def test_reversed_input_lists_concatenated(self):
        """
        Fill the missing test and function implementation to make sure that the desired result is [4, 3, 2, 1, 33, 22, 11]
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]

        reversed_concat_list = concatenate_list_from_reverse_input_lists(first_list, second_list)

        self.assertEqual(reversed_concat_list, [4, 3, 2, 1, 33, 22, 11])
        self.assertEqual(first_list, [1, 2, 3, 4])
        self.assertEqual(second_list, [11, 22, 33])

    def test_sorted_list(self):
        """
        Write the implementation that tests the following function call
        """

        first_list = [1, 2, 3, 4]
        second_list = [11, 22, 33]
        result = concatenate_and_sort(first_list, second_list)

        self.assertEqual([1, 2, 3, 4, 11, 22, 33], result)

        first_list = ["a", "b", "c"]
        second_list = ["x", "i", "p"]
        result = concatenate_and_sort(first_list, second_list)

        self.assertEqual(["a", "b", "c", "i", "p", "x"], result)

        first_list = ["banana", "curiosity", "ana"]
        second_list = ["killed", "the", "cat"]
        result = concatenate_and_sort(first_list, second_list)

        self.assertEqual(["ana", "banana", "cat", "curiosity", "killed", "the"], result)

    def test_switch_elements_by_index_when_index_out_of_bounds(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """

        first_list = [1, 2, 3]
        second_list = [4, 5, 6, 7]

        self.assertRaises(ValueError, switch_list_elements_by_index, first_list, second_list, 3)

    def test_switch_elements_by_index_for_lists_of_same_type(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """

        first_list = [1, 2, 3]
        second_list = [4, 5, 6, 7]

        result = switch_list_elements_by_index(first_list, second_list, 2)

        self.assertEqual(([1, 2, 6], [4, 5, 3, 7]), result)

    def test_switch_elements_by_index_for_lists_of_different_type(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """

        first_list = [1, 2, 3]
        second_list = ["Go", "to", "bed", "now!"]

        result = switch_list_elements_by_index(first_list, second_list, 2)

        self.assertEqual(([1, 2, 'bed'], ['Go', 'to', 3, 'now!']), result)

    def test_switch_elements_by_index_for_none_type_argument(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """

        self.assertRaises(ValueError, switch_list_elements_by_index, None, [2], 1)
        self.assertRaises(ValueError, switch_list_elements_by_index, [2], None, 1)
        self.assertRaises(ValueError, switch_list_elements_by_index, None, None, 5)

    def test_switch_elements_by_index_for_invalid_type_argument(self):
        """
        Write test and implementation of substitution of elements in two list. Eg:
        For [1, 2, 3] [4, 5, 6] substitute(2) returns [1, 2, 6] [4, 5, 3]
        """

        self.assertRaises(ValueError, switch_list_elements_by_index, 0, [2], 1)


if __name__ == '__main__':
    unittest.main()
