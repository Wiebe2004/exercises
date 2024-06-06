from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tommorow = date(2000,1,2)
    next_week = date(2000, 1, 8)
    callendar = CalendarStub(today)
    task = Task('Some description', tommorow)
    tasks = TaskList(callendar)

    tasks.add_task(task)
    callendar.today = next_week

    assert [task] == tasks.overdue_tasks