import unittest
import uuid

import mock

from .. import foo


class TestFoo(unittest.TestCase):

    def test_happy_path(self):
        self.assertEqual(foo.bar(), 'bar')

    def test_make_sure_mock_works(self):
        desired_bar = uuid.uuid4().hex

        def patched_underscore_bar():
            return desired_bar

        with mock.patch(__name__ + '.foo._bar', patched_underscore_bar):
            self.assertEqual(foo.bar(), desired_bar)
