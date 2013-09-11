# -*- coding: utf-8 -*-
import os
import unittest
import food2forkclient

test_path = os.path.dirname(__file__)

class TestFood2ForkClient(unittest.TestCase):

	@classmethod
	def setUpInstance(cls):
        config_file = os.path.join( test_path, 'config.json' )
        with open('config.json') as f:
            config = json.load(f)
        cls.f2fclient = food2fork.Food2ForkClient(api_key=config.get('api_key'))


    def test_api_url(self):
    	self.assertEqual(self.URL_API, 'http://food2fork.com/api')