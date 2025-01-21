import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Initialize main window
root = tk.Tk()
root.title("To-Do List")

# Task list
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add task function
def add_task():
    task_name = entry.get()
    if task_name:
        tasks.append(task_name)
        listbox.insert(tk.END, task_name)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Remove task function
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        listbox.delete(selected_task_index)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

# Update task function
def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        current_task = listbox.get(selected_task_index)
        new_task_name = simpledialog.askstring("Update Task", "Enter new task name:", initialvalue=current_task)
        if new_task_name:
            tasks[selected_task_index[0]] = new_task_name
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task_name)
            save_tasks()
    else:
        messagebox.showwarning("Warning", "You must select a task to update.")

# GUI Widgets
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=35)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

update_button = tk.Button(frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Load tasks on startup
load_tasks()

root.mainloop()
