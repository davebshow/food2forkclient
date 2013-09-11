# -*- coding: utf-8 -*-
import json
import urllib
import urllib2

def error_handler(fn):
    def request_wrapper(self, *args, **kwargs):
        try:
            response = fn(self, *args, **kwargs)
        except urllib2.HTTPError, e:
            message = u'HTTPError - {0}:{1}'.format(e.code, e.reason)
            raise Food2ForkClientError(message)
        except urllib2.URLError, e:
            message = u'URLError - {0}'.format(e.reason)
            raise Food2ForkClientError(message)
        except httplib.HTTPException:
            raise Food2ForkClientError('HTTPException')
        except Exception:
            import traceback
            message = u'Exception - {0}'.format(traceback.format_exc())
            raise Food2ForkClientError(message)
        if response.code != 200:
            raise Food2ForkClientError('Problem with Food2Fork API')
        return response
    return requestion_wrapper

class Food2ForkClientError(Exception):
    pass

class Food2ForkClient(object):
    URL_API = 'http://food2fork.com/api'
    URL_SEARCH = URL_API + '/search/?'
    URL_GET = URL_API + '/get/?'
    HEADERS = {"Content-Type":"application/json"}

    def __init__(self, api_key):
        self.api_key = api_key #put in settings

    def search(self,**kwargs):
        """
        kwargs:
        q: search_query
        sort: how respones are sorted
        page: used to get additional results
        """
        query_params = [
            (key, value) for key, value in kwargs.items()
        ] 
        query_params.append(('key', self.api_key))
        query_string = urllib.urlencode(query_params)
        self.url = self.URL_SEARCH + query_string
        response = self.request()
        return self.parse_json(response)

    def get_recipe(self, rid):
        """
        rid: rId (recipe_id) of recipe returned by search query
        """
        query_params = [('key', self.api_key), ('rId', rid)]
        query_string = urllib.urlencode(query_params)
        self.url = self.URL_GET + query_string
        response = self.request()
        return self.parse_json(response)

    @error_handler
    def request(self):
        req = urllib2.Request(self.url)
        for key, value in self.HEADERS.items():
            req.add_header(key, value)
        response = urllib2.urlopen(req)
        return response

    def parse_json(self, response):
        response_headers = json.loads(response.info().headers)
        python_response = json.loads(response.read())
        return response_headers, python_response


