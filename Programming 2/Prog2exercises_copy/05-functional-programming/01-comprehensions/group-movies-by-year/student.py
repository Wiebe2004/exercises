def group_movies_by_year(movies):
    years = {m.year for m in movies}
    return {year: [m.title for m in movies if m.year == year] for year in years}
    # Groups up the title if it equals the unique years within the parameter.
    # It goes in a loop through "years" and checks the titles for every movie.