import tkinter as tk
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg)
import matplotlib.pyplot as plt
import booksearch
import bookcheckout
import bookreturn
import bookweed

def bksrh():
    """Book search button function"""
    global userData
    userData=e1.get()
    booksearch.booksearch(userData)
    v.set(booksearch.booksearch.output)
    
def bkchk():
    """Book check button function"""
    bookID=e3.get()
    userID=e2.get()
    bookcheckout.book_check_sys(userID,bookID)
    w.set(bookcheckout.book_check_sys.final_output_1)
    x.set(bookcheckout.book_check_sys2.final_output_2)
    if bookcheckout.book_check_sys2.final_output_2==\
       "Available! Do you want to loan it?":
        bkchk.but=tk.Button(text="y",width=5,height=1,command=resulty)\
                   .place(x=240,y=280)
        bkchk.but1=tk.Button(text="n",width=5,height=1,command=resultn)\
                    .place(x=300,y=280)
        
def resulty():
    """yes button"""
    bookcheckout.book_check_sys3("y")
    y.set(bookcheckout.book_check_sys3.final_output_3)
    but2=tk.Button(text="Reset",width=5,height=1,command=reset).place(x=270,y=300)

def resultn():
    """no button"""
    bookcheckout.book_check_sys3("n")
    y.set(bookcheckout.book_check_sys3.final_output_3)
    but2=tk.Button(text="Reset",width=5,height=1,command=reset).place(x=270,y=300)

def reset():
    """Clears previous entries"""
    w.set("")
    x.set("")
    y.set("")
    e2.delete(0,200)
    e2.insert(0, "")
    e3.delete(0,200)
    e3.insert(0, "")

def ret():
    """Return book button"""
    bookid=e4.get()
    bookreturn.book_return(bookid)
    z.set(bookreturn.book_return.result)
    
def graph():
    """Produces graph button"""
    bookweed.weeding()
    x=bookweed.weeding.books_to_weed
    y=bookweed.weeding.num_days
    f=plt.Figure(figsize=(5,4),dpi=100)
    a=f.add_subplot(111)
    data=a.bar(x,y)
    a.set_title('Books to remove from library')
    a.set_xlabel('Book ID')
    a.set_ylabel('Days since last checkout')
    chart=FigureCanvasTkAgg(f,master=window)
    chart.get_tk_widget().place(x=500,y=100)
  
window=tk.Tk()
canvas1=tk.Canvas(window,width=1000,height=600)
welcome=tk.Label(text="Welcome to the Library",font=(None,25))
options=tk.Label(text="Please select an options from the list below:",\
                 font=(None,15))
welcome.pack()
options.pack()

#Search
e1=tk.Entry(window)
e1.place(x=200,y=70)
searchlabel=tk.Label(text="Book Search:",font=(None,15)).place(x=100,y=70)
searchbutton=tk.Button(text="Search",width=10,height=1,command=bksrh)\
              .place(x=400,y=74)
search_table=tk.Label(text="ID:ISBN:Title:Author:Purchase Date:Member ID",\
                      font=(None,15))
search_table.place(x=140,y=500)
v=tk.StringVar()
result=tk.Label(window,textvariable=v).place(x=140,y=520)
v.set('')

#Book checkout
chklabel=tk.Label(text="Checkout:",font=(None,15)).place(x=250,y=120)
idlabel=tk.Label(text="ID:",font=(None,15)).place(x=194,y=150)
e2=tk.Entry(window,width=4)
e2.place(x=220,y=150)
ckbknum=tk.Label(text="Book ID:",font=(None,15)).place(x=268,y=150)
e3=tk.Entry(window,width=4)
e3.place(x=330,y=150)
chkbutton1=tk.Button(text="Check ID",width=10,height=1,command=bkchk)\
            .place(x=245,y=190)
w=tk.StringVar()
result=tk.Label(window,textvariable=w).place(x=200,y=220)
w.set('')
x=tk.StringVar()
result=tk.Label(window,textvariable=x).place(x=200,y=240)
x.set('')
y=tk.StringVar()
result=tk.Label(window,textvariable=y).place(x=200,y=260)
y.set('')

#Book Return
retlabel=tk.Label(text="Book Return:",font=(None,15)).place(x=245,y=320)
booklabel=tk.Label(text="Book ID:",font=(None,15)).place(x=235,y=350)
e4=tk.Entry(window,width=4)
e4.place(x=310,y=350)
ret1=tk.Button(text="Return",width=10,height=1,command=ret)\
      .place(x=245,y=380)
z=tk.StringVar()
result=tk.Label(window,textvariable=z).place(x=255,y=400)
z.set('')

#Weeding
weedingbut=tk.Button(text="Weeding",width=10,height=1,command=graph)\
            .place(x=245,y=450)

canvas1.pack()
window.mainloop()
