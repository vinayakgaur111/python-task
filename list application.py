import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def get_tasks(self):
        return [task.description for task in self.tasks]

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].is_completed = True

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.task_manager = TaskManager()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack()

        self.add_task_entry = tk.Entry(root, width=50)
        self.add_task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.mark_completed_button = tk.Button(root, text="Mark Task Completed", command=self.mark_task_completed)
        self.mark_completed_button.pack()

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.update_task_list()

    def add_task(self):
        description = self.add_task_entry.get()
        if description:
            self.task_manager.add_task(description)
            self.add_task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def mark_task_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.mark_task_completed(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.delete_task(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
