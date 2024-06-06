import pytest
from calendars import CalendarStub
from tasks import TaskList, Task
from datetime import date, timedelta


def setup_function():
    global today
    today = date(2020, 1, 1)
    global tommorow
    tommorow = today + timedelta(days=1)
    global yesterday
    yesterday = today - timedelta(days=1)
    global calendar
    calendar = CalendarStub(today)
    global sut
    sut = TaskList(calendar)


def test_creation():
    # arrange

    # act

    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks
    assert [] == sut.overdue_tasks


def test_adding_task_with_due_day_in_future():
    # Arrange

    task = Task("Climbing", tommorow)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    # Arrange

    task = Task("Climbing", yesterday)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue():
    # Arrange
    next_week = today + timedelta(weeks=1)

    task = Task("description", tommorow)

    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished():
    # Arrange
    task = Task("Climbing", tommorow)
    sut.add_task(task)

    # act
    task.finished = True

    # assert
    assert 1 == len(sut.finished_tasks)
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
