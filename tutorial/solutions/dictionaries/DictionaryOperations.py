def add_elements_if_number_of_elements_is_odd(in_dict, element):
    """
    Adds dictionary element {'key': value} if number of current elements in the input dictionary is odd.
    DO NOT REPLACE THE EXISTING VALUE IF THE ELEMENT IS ALREADY IN THE DICTIONARY

    :param in_dict: Input dictionary which will possibly hold the element passed as a second parameter
    :param element: Element for potential addition
    :return (Boolean, int): Tuple with first parameter True if added False otherwise, and second - number of elements
    added
    """

    is_added = False
    no_elements = 0

    if not element:
        return False, 0

    if len(in_dict) % 2 != 0:
        for key in element.keys():
            if key not in in_dict:
                in_dict[key] = element[key]
                is_added = True
                no_elements += 1

    return is_added, no_elements
