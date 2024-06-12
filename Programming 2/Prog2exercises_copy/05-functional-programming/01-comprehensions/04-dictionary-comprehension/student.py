def title_to_director(movies):
    return {a.title : a.director for a in movies}


def director_to_titles(movies):
    return {k.director : [v.title for v in movies if k.director == v.director] for k in movies}