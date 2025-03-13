# Note! 
# I had several problems testing input so I used "unittest.mock"
# I used "unittest.mock import patch" to simplify testing input()

#1-  try test using unittest.mock  <= Test not appear
import unittest
from unittest.mock import patch
from main import create_new_customer, write_to_csv, check_customer_exists

class TestBankFunctions(unittest.TestCase):
    
    def setUp(self):
        print('Setting up tests')

    # Here using @patch  to mock input() function rather than manually enter 
    @patch('builtins.input', side_effect=["1000", "Afnan", "Matari", "afnan123"]) 
    def test_add_new_customer(self, mock_input):

        customer = create_new_customer("1000", "Afnan", "Matari", "afnan123")
        write_to_csv(customer)

        self.assertTrue(check_customer_exists("1000"))
        self.assertFalse(check_customer_exists("1001"))

    # Test check_customer_exists
    def test_check_user_in_file(self):
        customer = create_new_customer("1000", "Afnan", "Matari", "afnan123")
        write_to_csv(customer)

        #check from user 
        self.assertTrue(check_customer_exists("1000"))
        self.assertFalse(check_customer_exists("1001"))

if __name__ == "__main__":
    unittest.main()

# 2-  try test without unittest.mock <= Test not appear

# import unittest
# from main import create_new_customer, check_customer_exists

# class TestBankFunctions(unittest.TestCase):
#     def test_create_new_customer(self, mock_input):
#         customer = create_new_customer("1000", "Afnan", "Matari", "afnan123")
#         self.assertEqual(customer["account_id"], "1000")
#         self.assertEqual(customer["first_name"], "Afnan")
#         self.assertEqual(customer["last_name"], "Matari")
#         self.assertEqual(customer["password"], "afnan123")

#     def test_check_user_in_file(self):
#         # اختبار تحقق وجود المستخدم في الملف
#         self.assertTrue(check_customer_exists("1000"))
#         self.assertFalse(check_customer_exists("1001"))

# if __name__ == "__main__":
#     unittest.main()

