# -*- coding: utf-8 -*-
import os
import unittest

import config
import food2forkclient

test_path = os.path.dirname(__file__)

class TestFood2ForkClient(unittest.TestCase):

	@classmethod
	def setUpInstance(cls):
		api_key = getattr(config, 'API_KEY', None)
		if api is not None:
        	cls.f2fclient = food2fork.Food2ForkClient(
        		api_key=config.get('api_key')
        	)
        else:
        	assert('Please set up a config.py file with API Key')


    def test_api_url(self):
    	self.assertEqual(
    		self.URL_API, 'http://food2fork.com/api'
    	)

    def test_search_url(self):
    	self.assertEqual(self.URL_SEARCH, 'http://food2fork.com/api/search/?')

    def test_get_url(self):
    	self.assertEqual(self.URL_SEARCH, 'http://food2fork.com/api/get/?')

    def test_search(self):
    	header, response = self.search()
    	self.assertTrue(
    		len(header) > 0 and \
    		response['count'] == 30 and \
    		len(response['recipes'] == 30)
    	)

    def test_query_search(self):
    	header, response = self.search(q='chicken')
    	self.assertTrue(
    		len(header) > 0 and \
    		len(response['recipes']) > 0
    	)

    def test_get(self):
    	#not sure about this, what if they delete
    	header, response = self.get(rid='47692')
    	self.assertTrue(len(response['recipe']) == 1)



if __name__ == '__main__':
    unittest.main()