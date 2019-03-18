import unittest

from .. import foo


class TestFoo(unittest.TestCase):

    def test_happy_path(self):
        self.assertEqual(foo.bar(), 'bar')
