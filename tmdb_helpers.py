import requests

from getpass import getpass

def make_tmdb_api_request(method, api_key, extra_params={}):
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    response = requests.get(
        f"https://api.themoviedb.org/3{method}",
        params=params,
    )
    response.raise_for_status()
    return response.json()

def get_user_api_key():
    user_api_key = getpass('Enter your api key v3:')
    try:
        make_tmdb_api_request(method='/movie/2', api_key = user_api_key)
        return user_api_key
    except requests.HTTPError as err:
        if err.code == 401:
            return None
        else:
            raise

