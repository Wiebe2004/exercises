import pytest
from calendars import CalendarStub
from tasks import TaskList, Task
from datetime import date, timedelta


def test_creation():
    # Arrange
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)

    # Act
    tasks = TaskList(calendar)

    # Assert
    assert 0 == len(tasks)
    assert [] == tasks.due_tasks
    assert [] == tasks.overdue_tasks
    assert [] == tasks.finished_tasks


def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)
    next_week = date(2001, 1, 8)
    sut = TaskList(calendar)
    task = Task("Climbing", next_week)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    # Arrange
    today = date(2001, 1, 8)
    calendar = CalendarStub(today)
    past_week = date(2001, 1, 1)
    sut = TaskList(calendar)
    task = Task("Climbing", past_week)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(sut.add_task(task))
    assert 0 == len(sut)


def test_task_becomes_finished():
    # Arrange
    today = date(2001, 1, 1)
    tomorrow = date(2001, 1, 2)
    calendar = CalendarStub(today)
    task = Task("Climbing", tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    #Act
    task.finished = True

    #Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
