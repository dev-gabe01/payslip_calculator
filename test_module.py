import unittest
from tax_module import main

class TaxTests(unittest.TestCase):

    def test_get_tax_module(self):
        self.assertEqual(main("Sally",20000), 1666)
        self.assertEqual(main("Sally",40000), 3167)
        self.assertEqual(main("Sally",60000), 4500)
        self.assertEqual(main("Sally",90000), 6417)
        self.assertEqual(main("Sally",190000), 12167)

if __name__ == '__main__':
    unittest.main()
