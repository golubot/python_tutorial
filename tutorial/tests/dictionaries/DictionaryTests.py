import unittest

from tutorial.solutions.dictionaries.DictionaryOperations import add_elements_if_number_of_elements_is_odd, \
    write_input_csv_to_file, event_from_dictionary_to_csv


class DictionaryTestCase(unittest.TestCase):
    # global variable, reference it with self.
    JSON_EVENT_HEADER_MISSING = '''{"dataset_id":"custom_dataset_id","event_id":"0ff28e2d-698f-4e82-919a-ca617be82a03","environment_id":"local","payload":{"payload_version":"3.0","header":{"event_type":"learning","event_timestamp":"2019-07-25T10:18:31.814608Z","event_origin":"test-event-origin","source_id":"test-source-id","source_version":"$LATEST","domain":"loopback"},"data":{"producer":{"actor_type":"local","system_id":"test-system"},"consumer":{"actor_type":"system","system_id":"My system id"},"facts":{"claim_reference":"4002807892","original_id":0,"new_id":37}},"status":{"status_code":"100","status_message":"Success"}},"retention":{"delete":true,"deletion_date":"2068-04-23T18:25:43.511Z","obfuscate":false}}'''

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

    def test_publish_events_happy(self):
        """
        Tests the happy path of the publishing events. The subject under test is to confirm if the dialog box is shown to the user
        """
        # open file under '../resources/event_positive.json'
        # load it as json
        # call publish_event_if_stated_in_header
        # Assert something
        self.assertFalse(True)

    def test_publish_events_happy_no_publish(self):
        """
        Tests the happy path of the publishing events. The subject under test is to confirm if the dialog box is NOT shown to the user
        """
        # open file under '../resources/event_negative.json'
        # load it as json
        # call publish_event_if_stated_in_header
        # Assert something
        self.assertFalse(True)

    def test_publish_events_unhappy_publish_missing(self):
        """
        Tests the unhappy path of the publishing events. The publish field in the json is missing
        """
        # open file under '../resources/event_publish_missing.json'
        # load it as json
        # call publish_event_if_stated_in_header
        # Assert something
        self.assertFalse(True)

    def test_publish_events_unhappy_header_missing(self):
        """
        Tests the unhappy path of the publishing events. The header field in the json is missing
        """
        # Serialize string variable DictionaryTestCase.JSON_EVENT_HEADER_MISSING (or self.JSON_EVENT_HEADER_MISSING)
        # as dictionary call publish_event_if_stated_in_header

        # Assert something
        self.assertFalse(True)

    def test_dict_to_csv(self):
        """
        Tests the creation of csv from passed input dictionary. Use the experience gained from previous tests to
        load a json file as dictionary and pass it to this method asserting the output created from the file's contents
        """
        out = event_from_dictionary_to_csv({})
        # assert output to be as expected (create expected output as list containing header and data)
        self.assertTrue(False)

    def test_write_csv_to_file(self):
        """
        Tests the creation of csv file from csv list. Load event_positive.json  event_positive_alternative.json
        to create the input (you can use previous function as utility) which will be passed to the create file function.
        """

        csv_struct = list()  # create empty list
        csv_struct.append(list()) # add empty list as header
        csv_struct.append(list()) # add empty list as data row 1
        csv_struct.append(list()) # add empty list as data row 2

        write_input_csv_to_file(csv_struct)
        # assert that the file exists and is populated as expected
        self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()
