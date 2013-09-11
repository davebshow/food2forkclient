# -*- coding: utf-8 -*-
import os
import unittest

import config
import food2forkclient

test_path = os.path.dirname(__file__)

class TestFood2ForkClient(unittest.TestCase):

	@classmethod
	def setUpInstance(cls):
		api_key = getattr(config, API_KEY, None)
		if api is not None:
        	cls.f2fclient = food2fork.Food2ForkClient(api_key=config.get('api_key'))
        else:
        	assert('Please set up a config file with your API Key')


    def test_api_url(self):
    	self.assertEqual(self.URL_API, 'http://food2fork.com/api')

    def test_search

if __name__ == '__main__':
    unittest.main()