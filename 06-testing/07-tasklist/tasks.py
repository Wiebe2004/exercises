from datetime import date

class Task:
    def __init__(self,description,due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date
    

class Tasklist:
    def __init__(self):
        self.__tasks = []

    def add_task(self,task):
        if Task.due_date < date.today():
            raise RuntimeError("Data cannot be in the past!")
        self.__tasks.append(task)
        
    def __len__(self):
        return len(self.__tasks)
    
    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished == True]
    
    @property
    def due_tasks(self):
        return [task for task in self.__tasks if task.finished == False]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.__tasks if not task.finished and task.due_date < date.today()]