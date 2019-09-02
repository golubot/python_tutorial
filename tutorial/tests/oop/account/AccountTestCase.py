import unittest


class MyTestCase(unittest.TestCase):
    """
        Write all the tests for Account:
        # 1. Instantiate the class several types (create several objects)
        # 2. Print those objects (notice how override of __str__ works)
        # 3. Assert the accounts owners attributes
        # 4. Assert all accounts have the right balance (0 if not passed in constructor)
        # 5. Make a series of deposits and withdrawals
        # 6. Assert the new balance states
        # 7. Make a withdrawal that exceeds the available balance. Assert an exception has been raised

        # BONUS: Overload the constructor to accept another argument which will be account's allowed minus. Implement
        # the minus feature and `guard` the original constructor from passing negative values (validation of parameters)
        # GOOD JOB!

    """
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
