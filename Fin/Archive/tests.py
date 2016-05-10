import unittest
from contacts_rank import main


class TestContactsRank(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_matches(self):
        """Test the function with an input that should return no matching contacts."""

        self.assertEqual(main(7), [])

    def test_correct_matches(self):
        """Test that the function returns the correct match for a given input."""

        self.assertEqual(main('zz'), [(0.4, {u'phone': u'111.111.4444', u'name': u'zed', u'email': u'zz@zed.com'})])

    def test_incorrect_matches(self):
        """Confirm that a result is not equal to what should be returned for a given input."""

        self.assertNotEqual(main('enny'), [(0.8888888888888888, {u'phone': u'646.444.4567', u'name': u'Jenny'}), (0.7272727272727273, {u'name': u'Jenny J', u'email': u'jj@aol.com'}), (0.7272727272727273, {u'name': u'Jenny J', u'email': u'jj@Yahoo.com'})])

    def test_object_type(self):
        """Confirm that the object returned by the function is a list."""

        self.assertTrue(type(main('jenny')), 'list')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()