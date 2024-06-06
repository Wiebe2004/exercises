import pytest
from calendars import CalendarStub
from tasks import TaskList,Task
from datetime import date, timedelta


def test_creation():
    # arrange
    today = date(2020, 1, 1)
    calendar = CalendarStub(today)

    # act
    sut = TaskList(calendar)

    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks
    assert [] == sut.overdue_tasks


def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2020, 1, 1)
    tommorow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task("Climbing", tommorow)
    sut = TaskList(calendar)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    # Arrange
    today = date(2020, 1, 1)
    due_date_past = today - timedelta(days=5)
    calendar = CalendarStub(today)
    task = Task("Climbing", due_date_past)
    sut = TaskList(calendar)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)
    calendar = CalendarStub(today)
    task = Task("description", tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks

def test_task_becomes_finished():
    # Arrange
    today = date(2020, 1, 1)
    tommorow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task("Climbing", tommorow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # act
    task.finished = True

    # assert
    assert 1 == len(sut.finished_tasks)
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
