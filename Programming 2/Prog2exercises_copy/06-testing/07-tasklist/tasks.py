from datetime import date, timedelta

class Task:
    def __init__(self, description, due_date, finished=False):
        self.__description = description
        self.__due_date = due_date
        self.__finished = finished

    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property 
    def finished(self):
        return self.__finished
    
    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    
    @finished.setter
    def finished(self, value):
        self.__finished = value  

    def __str__(self):
        return f"Task(description={self.__description}, due_date={self.__due_date}, finished={self.__finished})"


task = Task('bake birthday cake', date(2023, 10, 1))
print(task.description)
print(task.due_date)
print(task.finished)
task.finished = True
print(task.finished)



class TaskList:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError("Task's due date must be in the future")
        self.__tasks.append(task)

    def __len__(self):
        return len(self.__tasks)
    
    def __str__(self):
        return "\n".join(str(task) for task in self.__tasks)
    
    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.__tasks if not task.finished and task.due_date < date.today()]

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value




# Create a new TaskList
tasks = TaskList()
print(len(tasks))  # Output: 0

# Define tomorrow and yesterday
tomorrow = date.today() + timedelta(days=1)
yesterday = date.today() - timedelta(days=1)

# Try to add a task with a due date in the past
try:
    task_in_past = Task('some description', yesterday)
    tasks.add_task(task_in_past)
except RuntimeError:
    print("RuntimeError: Task's due date must be in the future")

# Add a task with a due date in the future
task = Task('some description', tomorrow)
tasks.add_task(task)

# Print the tasks as strings
print("\n1)Due Tasks\nFinished tasks:")
print("\n".join(str(task) for task in tasks.finished_tasks))

print("Due tasks:")
print("\n".join(str(task) for task in tasks.due_tasks))

print("Overdue tasks:")
print("\n".join(str(task) for task in tasks.overdue_tasks))

# To simulate waiting 2 days, we can just change the due date of the task to yesterday
task.due_date = yesterday

# Print the tasks as strings
print("\n2)Overdue Tasks\nFinished tasks:")
print("\n".join(str(task) for task in tasks.finished_tasks))

print("Due tasks:")
print("\n".join(str(task) for task in tasks.due_tasks))

print("Overdue tasks:")
print("\n".join(str(task) for task in tasks.overdue_tasks))

# Mark the task as finished
task.finished = True

# Print the tasks as strings
print("\n3)Finished Tasks\nFinished tasks:")
print("\n".join(str(task) for task in tasks.finished_tasks))

print("Due tasks:")
print("\n".join(str(task) for task in tasks.due_tasks))

print("Overdue tasks:")
print("\n".join(str(task) for task in tasks.overdue_tasks))