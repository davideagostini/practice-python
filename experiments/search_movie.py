"""
Search a movie in The Open Movie Database
www.omdbapi.com
"""

import json
import requests

#search for specific movie
def search_movie(the_movie):
    req = requests.get('http://www.omdbapi.com/', params={'t': the_movie, 'plot': 'short'})
    if req.status_code == requests.codes.ok:
        movie = json.loads(req.text)
        print("Title: {}".format(movie['Title']))
        print("Year: {}".format(movie['Year']))
        print("Runtime: {}".format(movie['Runtime']))
        print("Genre: {}".format(movie['Genre']))
        print("Director: {}".format(movie['Director']))
        print("Writer: {}".format(movie['Writer']))
        print("Actors: {}".format(movie['Actors']))
        print("Plot: {}".format(movie['Plot']))
        print("Awards: {}".format(movie['Awards']))
    else:
        print("Movie not found")


# search for generic term
def generic_search(search_term):
    req = requests.get('http://www.omdbapi.com/', params={'s': search_term, 'type': 'movie'})
    if req.status_code == requests.codes.ok:
        movies = json.loads(req.text)
        if 'Search' in movies:
            lines = sorted(movies['Search'], key=lambda m: m['Year'], reverse=True)

            for movie in lines:
                print("Title: {} - Year: {}".format(movie['Title'], movie['Year']))
        else:
            print("Nothing found")


def main():
    next_search = True
    while next_search:
        tipology = input("\n\nInsert 0) for a specific movie:\nInsert 1) for generic search:\n")
        if tipology.strip():
            if int(tipology) == 0:
                search = input('Insert a movie title: ')
                if search.strip():
                    print("\n\n")
                    search_movie(search)
            elif int(tipology) == 1:
                search = input('Search for a movie: ')
                if search.strip():
                    print("\n\n")
                    generic_search(search)
        else:
            next_search = False


if __name__ == '__main__':
    main()
