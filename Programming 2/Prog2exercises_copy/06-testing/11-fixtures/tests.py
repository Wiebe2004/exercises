import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList


# def setup_function():
#     global today, tomorrow, yesterday, calendar, sut
#     today = date(2000, 1, 1)
#     yesterday = today - timedelta(days=1)
#     tomorrow = today + timedelta(days=1)
#     calendar = CalendarStub(today)
#     sut = TaskList(calendar)

@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    # Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future(tomorrow, sut):
    # Arrange
    task = Task('description', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past(yesterday, sut):
    # Arrange
    task = Task('description', yesterday)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue(today, tomorrow, sut, calendar):
    # Arrange
    next_week = today + timedelta(weeks=1)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished(tomorrow, sut):
    # Arrange
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
