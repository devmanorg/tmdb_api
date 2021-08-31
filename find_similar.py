from own_db_helpers import load_data
from collections import OrderedDict

def find_my_film(keyword, films_data):
    for film in films_data:
        if keyword == film['original_title']:
            return film
    return None

def get_rating(my_film, films_data, num_to_recommend=8):
    params = {
        'belongs_to_collection': 1000,
        'original_language': 300,
        'budget': 100,
        'genres': 500
    }
    rating = {}
    for film in films_data:
        film_rate = 0
        for parameter in params:
            if film[parameter] == my_film[parameter]:
                film_rate += params[parameter]
        rating[film['original_title']] = film_rate
    del rating[my_film['original_title']]
    rating = OrderedDict(sorted(rating.items(), key=lambda t: t[1], reverse=True))
    final_recommendation = []
    for film in rating:
        if len(final_recommendation) > num_to_recommend:
            break
        final_recommendation.append(film)
    return final_recommendation

if __name__ == '__main__':
    path = input('Enter path to DataBase:')
    films_data = load_data(path)
    if not films_data:
        print('File not found, sorry...')
        raise SystemExit
    keyword = input('Enter film to search for:')
    my_film = find_my_film(keyword, films_data)
    if not my_film:
        print('No such film in FilmsDB')
        raise SystemExit
    recommendation = get_rating(my_film, films_data)
    for film in sorted(recommendation):
        print(film)

