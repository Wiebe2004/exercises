import util

def count_older_than(people, min_age):
    def people_older_than(people, min_age):
        return people > min_age

    return util.count(people, people_older_than)