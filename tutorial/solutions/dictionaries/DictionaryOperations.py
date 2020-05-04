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

    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Hooray, you got an event!", json.dumps(in_dict, indent=4))


def event_from_dictionary_to_csv(in_dict):
    """
    Creates a flat csv representation from the nested input directory with one row as header and one row as data.
    :param in_dict dict: Input that will be translated to csv format
    :return: ist(list): List of lists of which the first list is the header, second third and any subsequent list represents data row
    """
    result = list()
    result.append(list()) # header
    result.append(list()) # data
    return result


def write_input_csv_to_file(in_csv):
    """
    Writes the csv passed as an argument to this function to a file.
    :param in_csv list(list()): List of lists of which the first list is the header, second third and any subsequent list represents data row
    """
    return
