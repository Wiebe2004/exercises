import pytest
from search import binary_search
# I have to be honest, this exercise burnt my brain out.
# It was troublesome to understand the assignment correctly...
class Student:
    def __init__(self, id):
        self.id = id

students = [Student(i) for i in range(1, 11)]  # Students with IDs from 1 to 10

@pytest.mark.parametrize('students, target_id', [
    (students, 0),  # No student with ID 0
    (students, 1),  # Student with ID 1 is first in the list
    (students, 10),  # Student with ID 10 is last in the list
    (students, 5),  # Student with ID 5 is neither first nor last
    ([Student(i) for i in range(1, 21, 2)], 10),  # IDs have gaps, no student with ID 10
    ([], 1),  # Empty list
    (students, 11),  # ID higher than any student's ID
])
def test_binary_search(students, target_id):
    student = binary_search(students, target_id)
    if student is None:
        assert all(s.id != target_id for s in students)
    else:
        assert student.id == target_id