from operator import attrgetter

def sort_by_age(people):
    people.sort(key=lambda person: person.age)
    return people


def sort_by_decreasing_age(people):
    people.sort(key=attrgetter('age'), reverse=True)
    return people

def sort_by_name(people):
    people.sort(key=attrgetter('name'))
    return people

def sort_by_name_then_age(people):
    people.sort(key=attrgetter('name','age'))
    return people

def sort_by_name_then_decreasing_age(people):
    people.sort(key=lambda person: (person.name, -person.age))
    return people