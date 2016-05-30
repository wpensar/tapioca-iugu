# coding: utf-8

import unittest

from tapioca_iugu import Iugu


class TestTapiocaIugu(unittest.TestCase):

    def setUp(self):
        self.wrapper = Iugu()


if __name__ == '__main__':
    unittest.main()
