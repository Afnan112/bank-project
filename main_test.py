import unittest
from main import create_new_customer

class TestInputs(unittest.TestCase):
    def test_user_input_string(self):
        result = create_new_customer()
        self.assertIsInstance(result, str)



if __name__ == '__main__':
    unittest.main()