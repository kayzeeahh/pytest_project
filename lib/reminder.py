class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None
        
    def reminder_me_to(self, task):
        self.task = task
        
    def remind(self):
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"