# -*- coding: utf-8 -*-
import os
import sys
import unittest


from client import Food2ForkClient

try:
    API_KEY = os.environ['API_KEY']
except KeyError:
    API_KEY = None
    sys.stderr.write('Please set os.environ["API_KEY"] = yourapikey, '
                     'or pass api_key param in Food2ForkClient')


class TestFood2ForkClient(unittest.TestCase):

    def setUp(self):
        self.f2fclient = Food2ForkClient(api_key=API_KEY)

    def test_api_url(self):
        self.assertEqual(
            self.f2fclient.URL_API, 'http://food2fork.com/api'
        )

    def test_search_url(self):
        self.assertEqual(self.f2fclient.URL_SEARCH,
                         'http://food2fork.com/api/search/?')

    def test_get_url(self):
        self.assertEqual(self.f2fclient.URL_GET,
                         'http://food2fork.com/api/get/?')

    def test_search(self):
        response = self.f2fclient.search()
        self.assertTrue(
            len(response) > 0
        )

    def test_query_search(self):
        response = self.f2fclient.search(q='chicken')
        self.assertTrue(
            len(response) > 0

        )

    def test_get(self):
        #not sure about this, what if they delete
        response = self.f2fclient.get(rid='47692')
        self.assertTrue(len(response) > 0)


if __name__ == '__main__':
    unittest.main()
