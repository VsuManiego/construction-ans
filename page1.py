from tkinter import *


ws = Tk()
ws.geometry('1000x500')
ws.title('PythonGuides')
ws['bg']='#5d8a82'

f = ("Times bold", 14)


def nextPage1():
    ws.destroy()
    import page2

def prevPage():
    ws.destroy()
    import page3
    
def nextPage2():
    ws.destroy()
    import page4
    
def nextPage3():
    ws.destroy()
    
Label(
    ws,
    text="Construction Project Data Storage System", 
    padx=10,
    pady=10,
    bg='#5d8a82',
    font=("Cooper Black", 30)
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="WORKERS", 
    padx=30,
    pady=30,
    font=f,
    bg="blue",
    command=nextPage1
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="TOOLS", 
    padx=30,
    pady=30,
    font=f,
     bg="green",
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

    
Button(
    ws, 
    text="EQUIPMENTS", 
    font=f,
    bg="yellow",
    padx=30,
    pady=30,
    command=nextPage2
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="EXIT", 
    padx=30,
    pady=30,
    font=f,
    command=nextPage3
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()


