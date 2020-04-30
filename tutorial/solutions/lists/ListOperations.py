
def concatenate_lists(arr1, arr2):
    """
    Function that concatenates two lists

    :param arr1: first list that will start from index 0
    :param arr2: second list that comes after the end of the first
    :return: list of first + second
    """

    return arr1 + arr2


def concatenate_list_with_reverse_second_list(arr1, arr2):
    """
    Function that reverses the second parameter and concatenates as such to the first

    :param arr1: first list that will start from index 0
    :param arr2: second list that comes after the end of the first - in reverse order
    :return: list of first + second
    """

    arr3 = list(arr2)
    arr3.reverse()

    return arr1 + arr3


def concatenate_list_from_reverse_input_lists(arr1, arr2):
    """
    Function that concatenates 2 reversed lists
    :param arr1: list to be reversed
    :param arr2: list to be reversed and concatenated to the end of the first reversed list
    :return: arr1(in reversed order) concatenated with arr2(in reversed order)
    """
    rev1 = list(arr1)
    rev1.reverse()

    rev2 = list(arr2)
    rev2.reverse()

    return rev1 + rev2


def concatenate_and_sort(arr1, arr2):
    """
    Concatenates two lists and returns sorted array of the concatenated result
    :param arr1: first list that will start from index 0
    :param arr2: second list that comes after the end of the first
    :return: arr1 + arr2 sorted in ascending order
    """
    concat = (arr1 + arr2)
    concat.sort()
    return concat


def switch_list_elements_by_index(arr1, arr2, pos):
    """
    Switches the i-th element from the two lists
    :param arr1: list with starting index 0
    :param arr2: list with starting index 0
    :param pos: index number of the element that needs to be switched
    :return: list with switched i-th element in both lists
    """

    try:

        if arr1 is None or arr2 is None:
            raise ValueError
        elif (len(arr1) - 1) < pos or (len(arr2) - 1) < pos:
            raise IndexError

        switched_list_1 = list(arr1)
        switched_list_2 = list(arr2)

        temp = switched_list_1[pos]
        switched_list_1[pos] = switched_list_2[pos]
        switched_list_2[pos] = temp

    except (ValueError, IndexError, TypeError):
        raise ValueError("Validation of input parameters failed")

    return switched_list_1, switched_list_2
