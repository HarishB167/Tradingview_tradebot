import unittest

from tests import test_login

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(test_login.TestLogin)
    unittest.TextTestRunner().run(suite)