import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Create UI elements
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Mark Task as Completed", command=self.mark_task)
        self.mark_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]["task"]
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index]["task"] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Update Task", "Select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

    def mark_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Mark Task", "Select a task to mark.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            display_task = task["task"]
            if task["completed"]:
                display_task += " (Completed)"  # Indicate completed task
            self.task_listbox.insert(tk.END, display_task)  # Add tasks to the listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
