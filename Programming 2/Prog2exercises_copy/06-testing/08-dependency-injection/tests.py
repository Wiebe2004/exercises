from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList

def test_task_becomes_overdue():
    today =  date(2024, 5, 6)
    tomorrow = date(2024, 5, 7)
    next_week = date(2024, 5, 15)
    calendar = CalendarStub(today)
    task = Task('some description', tomorrow)
    tasks = TaskList(calendar)

    tasks.add_task(task)
    calendar.today = next_week

    assert [task] == tasks.overdue_tasks