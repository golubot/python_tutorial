import json
from tkinter import messagebox
import tkinter


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


def publish_event_if_stated_in_header(in_dict):
    """
    Publishes the input dictionary to the user, if dataset_id -> payload -> header -> publish_event is set to true
    :param in_dict: Dictionary for user display, if there is a header flag set to true
    """
    # write conditions
    if 'header' not in in_dict['payload']:
        return 'Missing [header] key in dictionary!'

    if 'publish_event' not in in_dict['payload']['header']:
        return 'Missing [publish_event] key in dictionary!'

    if not in_dict['payload']['header']['publish_event']:
        return False
    else:
        # hide main window
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("Hooray, you got an event!", json.dumps(in_dict, indent=4))
        return True


def event_from_dictionary_to_csv(in_dict):
    """
    Creates a flat csv representation from the nested input directory with one row as header and one row as data.
    :param in_dict: Input that will be translated to csv format
    :return: list(list): List of lists of which the first list is the header, second third and any subsequent list
    represents data row
    """
    # header: extract all keys before you append

    key_list = list(in_dict.keys())
    value_list = list()
    for key in key_list:
        value = in_dict[key]
        if not isinstance(value, dict):
            if type(value) in (bool, int):
                value_list.append(str(value))
            else:
                value_list.append(value)
        else:
            value_list.append('')
            rec_keylist, rec_valuelist = event_from_dictionary_to_csv(value)
            key_list = key_list + rec_keylist
            value_list = value_list + rec_valuelist

    return key_list, value_list


def m2(in_dict):
    keys, values = event_from_dictionary_to_csv(in_dict)

    return [",".join(keys), ",".join(values)]


def write_input_csv_to_file(in_csv):
    """
    Writes the csv passed as an argument to this function to a file.
    :param in_csv list(list()): List of lists of which the first list is the header, second third and any subsequent
    list represents data row
    """

    my_file = open("my_first_test.txt", "a")
    for row in in_csv:
        my_file.write(row)
        my_file.write("\n")
    # my_file.writelines(in_csv)
    my_file.close()

    return
