#!usr/bin/python
#-*- coding: utf-8 -*-

import os
import unittest

from get_data import ratings

test_ratings = {'title': 'A Simple Plan',
                'rating': '6.4',
                'image': 'p01j0bky',
                'prog': 'b0078cwc'
                }

class TestGetData(unittest.TestCase):
    '''
        class to test data from get_data file
    '''

    def test(self):
        self.assertIn(test_ratings, ratings)

if __name__ == "__main__":
    unittest.main()
