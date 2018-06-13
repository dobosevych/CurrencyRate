from unittest import TestCase

from structures.currency import Currency


class TestCurrency(TestCase):
    def setUp(self):
        self.curr_usd = Currency('USD')

    def test_str(self):
        self.assertEqual(str(self.curr_usd), 'USD')