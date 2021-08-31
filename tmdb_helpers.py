import urllib.request
import urllib.parse
import json
from getpass import getpass

def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)

def get_user_api_key():
    user_api_key = getpass('Enter your api key v3:')
    try:
        make_tmdb_api_request(method='/movie/2', api_key = user_api_key)
        return user_api_key
    except urllib.error.HTTPError as err:
        if err.code == 401:
            return None
        else:
            raise

