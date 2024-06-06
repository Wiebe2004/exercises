import pytest
from calendars import CalendarStub
from tasks import TaskList, Task
from datetime import date, timedelta


@pytest.fixture
def today():
    return date(2000, 1, 1)


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)


@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)


@pytest.fixture
def calendar(today):
    return CalendarStub(today)


@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    # arrange

    # act

    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks
    assert [] == sut.overdue_tasks


def test_adding_task_with_due_day_in_future(tomorrow,sut):
    # Arrange

    task = Task("Climbing", tomorrow)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past(yesterday,sut):
    # Arrange

    task = Task("Climbing", yesterday)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue(tomorrow,calendar,sut,today):
    # Arrange
    next_week = today + timedelta(weeks=1)

    task = Task("description", tomorrow)

    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished(tomorrow,sut):
    # Arrange

    task = Task("Climbing", tomorrow)

    sut.add_task(task)

    # act
    task.finished = True

    # assert
    assert 1 == len(sut.finished_tasks)
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
