import unittest
from demo import show_aggie_pride


# https://docs.python.org/3/library/unittest.html
class MyTestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        df = show_aggie_pride()

        self.assertEqual(df.loc[0, 'Text'], 'Aggie County')
        self.assertEqual(df.loc[1, 'Text'], 'Aggie State')
        self.assertEqual(df.loc[2, 'Text'], 'Aggie Nation')
        self.assertEqual(df.loc[3, 'Text'], 'Aggie.S.A!')

if __name__ == '__main__':
    unittest.main()
