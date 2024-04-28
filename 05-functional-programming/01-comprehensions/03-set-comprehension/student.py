def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {k for k in xs if k in ys}
