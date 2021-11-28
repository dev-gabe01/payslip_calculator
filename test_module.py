import unittest
from tax_module import main

class TaxTests(unittest.TestCase):

    def test_get_tax_module(self):
        self.assertEqual(main("Sally",60000), 4500)

if __name__ == '__main__':
    unittest.main()
