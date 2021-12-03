
from tkinter import *
from tkinter import messagebox
import os

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
  
  
def deleteTask():
    lb.delete(ANCHOR)
   
def nextPage3():
    w.destroy()
    import main0
    
def nextPage4():
    w.destroy()
    
w = Tk()
w.geometry('1000x500')
w.title('WORKERS')
w.config(bg="blue")
w.resizable(width=False, height=False)

frame = Frame(w)
frame.pack(pady=10)


lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = ()
    


for item in task_list:
    f.insert(tk.END, line.strip())

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    w,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(w)
button_frame.pack(pady=20)



addTask_btn = Button(
    button_frame,
    text='Add Worker',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


   

delTask_btn = Button(
    button_frame,
    text='Delete Worker',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn1 = Button(
    button_frame,
    text='DONE',
    font=('times 14'),
    bg='#fff',
    padx=20,
    pady=10,
    command=nextPage3
)
delTask_btn1.pack(fill=BOTH)

delTask_btn2 = Button(
    button_frame,
    text='EXIT',
    font=('times 14'),
    bg='#fff',
    padx=20,
    pady=10,
    command=nextPage4
)
delTask_btn2.pack(fill=BOTH, expand=True, side=RIGHT)


w.mainloop()
