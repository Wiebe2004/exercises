from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def test_task_becomes_overdue():
    today = date(2001, 1, 1)
    tommorow = date(2001, 1, 2)
    next_week = date(2001, 1, 8)

    calendar = CalendarStub(today)
    task = Task('Climbing', tommorow)
    tasks = TaskList(calendar)

    tasks.add_task(task)
    calendar.today = next_week

    assert [task] == tasks.due_tasks

