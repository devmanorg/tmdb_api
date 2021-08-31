from tmdb_helpers import get_user_api_key
from tmdb_helpers import make_tmdb_api_request

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    if not user_api_key:
        print('Invalid api key')
        raise SystemExit
    movie_number = 215
    print(make_tmdb_api_request(method='/movie/%d' % movie_number, api_key=user_api_key)['budget'])

