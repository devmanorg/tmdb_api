from own_db_helpers import load_data

def search_for_film(keyword, films_data):
    films_found = set()
    for film in films_data:
        if keyword.lower() in film['original_title'].lower():
            films_found.add(film['original_title'])
    return films_found

if __name__ == '__main__':
    path = input('Enter path to DataBase:')
    films_data = load_data(path)
    if not films_data:
        print('File not found, sorry...')
        raise SystemExit
    keyword = input('Enter film to search for:')
    result = search_for_film(keyword, films_data)
    for film in sorted(result):
        print(film)
        
        
