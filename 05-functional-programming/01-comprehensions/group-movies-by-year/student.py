import movie as movies

def group_movies_by_year(movies):
    return {
        year: [movie.title for movie in movies if movie.year == year]
        for year in {movie.year for movie in movies}
    }


print(group_movies_by_year(movies.movies))