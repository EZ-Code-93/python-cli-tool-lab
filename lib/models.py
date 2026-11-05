# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        # TODO: Assign the title
        # TODO: Set completed to False
        self.title = title
        self.completed = False

    def complete(self):
        # TODO: Mark the task as complete
        # TODO: Print a confirmation message
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

# TODO: Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        # TODO: Store the user's name
        # TODO: Initialize an empty list of tasks
        self.name = name
        self.tasks = []

    def add_task(self, task):
        # TODO: Add the task to the user's task list
        # TODO: Print a message confirming the task was added
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # TODO: Search for a task by its title in the user's task list
        # TODO: Return the matching task or None
        for task in self.tasks:
            if task.title == title:
                return task
        return None