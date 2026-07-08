from tkinter import *
from tkinter import messagebox

# Create Window
root = Tk()
root.title("To-Do List")
root.geometry("450x500")
root.configure(bg="lightblue")

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, "☐ " + task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        if task.startswith("☐"):
            task = task.replace("☐", "✔", 1)
            task_listbox.delete(selected)
            task_listbox.insert(selected, task)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        task_listbox.delete(0, END)

# Heading
Label(root, text="TO-DO LIST", font=("Arial", 20, "bold"),
      bg="lightblue").pack(pady=10)

# Entry Box
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add Button
Button(root, text="Add Task", width=20, bg="green",
       fg="white", command=add_task).pack(pady=5)

# Listbox
task_listbox = Listbox(root, width=40, height=12,
                       font=("Arial", 12), selectbackground="skyblue")
task_listbox.pack(pady=10)

# Buttons
Button(root, text="Mark Completed", width=20,
       bg="blue", fg="white", command=complete_task).pack(pady=5)

Button(root, text="Delete Selected", width=20,
       bg="red", fg="white", command=delete_task).pack(pady=5)

Button(root, text="Clear All", width=20,
       bg="orange", fg="white", command=clear_tasks).pack(pady=5)

# Run Application
root.mainloop()
