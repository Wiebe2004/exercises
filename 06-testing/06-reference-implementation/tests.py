# import pytest
# from search import linear_search, binary_search
# from student import Student


# @pytest.mark.parametrize(
#     "students",
#     [
#         [],
#         [Student(student_id) for student_id in range(0, 100)],
#         [
#             Student(student_id)
#             for student_id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]
#         ],
#     ],
# )
# @pytest.mark.parametrize("student_id", range(0, 100))
# def test_search(students, student_id):
#     linear_result = linear_search(students, student_id)
#     binary_result = binary_search(students, student_id)
#     assert linear_result == binary_result, f"Failed when looking for id: {id}"

import pytest
from search import linear_search, binary_search
from student import Student


@pytest.mark.parametrize('students', [
    [],
    [Student(id) for id in range(0, 100)],
    [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]],
])
@pytest.mark.parametrize('id', range(0, 100))
def test_search(students, id):
    linear_result = linear_search(students, id)
    binary_result = binary_search(students, id)
    assert linear_result is binary_result, f"Failed when looking for id={id}"
