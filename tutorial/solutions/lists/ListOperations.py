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
    arr2.reverse()

    return arr1 + arr2


def concatenate_reversed_input_lists(arr1, arr2):
    """
    Function that reverses both input lists and concatenates them

    :param arr1: first list that will start from index 0 - in reverse order
    :param arr2: second list that comes after the end of the first - in reverse order
    :return: list of first + second
    """

    arr1.reverse()
    arr2.reverse()

    return arr1 + arr2


def concatenate_and_sort(arr1, arr2):
    """
    Concatenates two lists and returns sorted array of the concatenated result
    :param arr1: first list that will start from index 0
    :param arr2: second list that comes after the end of the first
    :return: arr1 + arr2 sorted in ascending order
    """
    concat = arr1 + arr2
    concat.sort()
    return concat


def switch_elements_by_index(arr1, arr2, switch_ind):
    """
    Switches the elements of the first and second list on the given index
    :param arr1: first list that will start from index 0
    :param arr2: second list that will start from index 0
    :param switch_ind: integer that shows index of the element to be switched
    :return: arr1 and arr2 with switched elements on index
    """
    if switch_ind > len(arr1):
        print("first list is too short! Len is {}".format(len(arr1)))
    elif switch_ind > len(arr2):
        print("second list is to short!")
    else:
        print("Index applicable")
        arr1[switch_ind], arr2[switch_ind] = arr2[switch_ind], arr1[switch_ind]
        return arr1, arr2
    return


def extract_even_elements(input_list):
    """
    Returns new list (old list intact) with only the even elements extracted from the original
    :param list:- Original list
    :return: New list with extracted odd elements from the list passed as input parameter
    """
    even_list = list()
    for n in input_list:
        if n % 2 == 0:
            even_list.append(n)

    return even_list


def delete_even_elements(input_list):
    """
    Returns the same list with only the odd elements.
    :param list: Original list
    :return: Modified original list with even elements omitted
    """
    for n in input_list:
        if n % 2 == 0:
            input_list.remove(n)

    return input_list


def extract_every_third_element_using_slices(input_list):
    """
    Write the implementation of function that extracts every third element using slices technique
    :param input_list: input list for slicing
    :return: list with every third element or empty list if not applicable
    """
    return input_list[3::3]


def delete_element_from_list_if_present(input_list, element):
    """
    Write implementation of method that tests if element is present and deletes it if true modifying the original list
    (no copy is made in the process)
    :param input_list: input list that might or might not contain the element for deletion
    :param element: element for deletion
    :return: the original list with deleted element if present
    """
    for n in input_list:
        if n == element:
            input_list.remove(n)

    return input_list
