def titles(movies):
    return [m.title for m in movies]





def titles_and_years(movies):
    return [(m.title, m.year) for m in movies]




def titles_and_actor_counts(movies):
    return [(m.title, len(m.actors)) for m in movies]





def reverse_words(sentence):
    words = sentence.split(' ')
    yep = ' '.join(word[::-1] for word in words)
    return yep