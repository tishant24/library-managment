from tkinter import *
import tkinter.messagebox
import backend
root=Tk()
root.title('LMS')

def callback():
  if tkinter.messagebox.askokcancel("quit","Do You want to quit?"):
    root.destroy()

def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)

def add_entry():
  backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),book_id.get())
  listing.delete(0,END)
  listing.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),book_id.get()))
  clear()

def view_all():
  listing.delete(0,END)
  for row in backend.view():
    listing.insert(END,row)
  clear()

def update():
  global selected_tuple
  backend.update(selected_tuple[0],title_txt.get(),author_txt.get(),year_txt.get(),book_id.get())
  view_all()

def get_selected_row(event):
  global selected_tuple
  clear()
  index=listing.curselection()[0]
  selected_tuple=listing.get(index)
  e1.insert(END,selected_tuple[1])
  e2.insert(END,selected_tuple[3])
  e3.insert(END,selected_tuple[2])
  e4.insert(END,selected_tuple[4])

def delete():
  global selected_tuple
  backend.delete(selected_tuple[0])
  view_all()

def search():
  listing.delete(0,END)
  search_data=backend.search(title_txt.get(),author_txt.get(),year_txt.get(),book_id.get())
  if len(search_data)!=0:
    for row in search_data:
      listing.insert(END,row)
  else:
    tkinter.messagebox.showinfo('Message','NO BOOKS FOUND')
  clear()

selected_tuple=tuple()
title_txt=StringVar()
author_txt=StringVar()
year_txt=StringVar()
book_id=StringVar()
l=Label(root,text='BOOK',fg='blue',relief=RAISED)
l.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')
l=Label(root,text='PUBLISH',fg='red',relief=RAISED)
l.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
e1=Entry(root,textvariable=title_txt)
e1.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
e2=Entry(root,textvariable=year_txt)
e2.grid(row=1,column=1,padx=5,pady=5,sticky='nswe')

l=Label(root,text='AUTHOR',fg='blue',relief=RAISED)
l.grid(row=0,column=2,padx=5,pady=5,sticky='nswe')
l=Label(root,text='BOOK_ID',fg='red',relief=RAISED)
l.grid(row=1,column=2,padx=5,pady=5,sticky='nswe')
e3=Entry(root,textvariable=author_txt)
e3.grid(row=0,column=3,padx=5,pady=5,sticky='nswe')
e4=Entry(root,textvariable=book_id)
e4.grid(row=1,column=3,padx=5,pady=5,sticky='nswe')

b1=Button(root,text='View All',command=view_all)
b1.grid(row=2,column=3,padx=5,pady=5,sticky='nswe')
b2=Button(root,text='Search BOOK',command=search)
b2.grid(row=3,column=3,padx=5,pady=5,sticky='nswe')
b3=Button(root,text='Add BOOK',command=add_entry)
b3.grid(row=4,column=3,padx=5,pady=5,sticky='nswe')
b4=Button(root,text='Update',command=update)
b4.grid(row=5,column=3,padx=5,pady=5,sticky='nswe')
b5=Button(root,text='Delete Selected',command=delete)
b5.grid(row=6,column=3,padx=5,pady=5,sticky='nswe')
b6=Button(root,text='Close',command=root.destroy)
b6.grid(row=7,column=3,padx=5,pady=5,sticky='nswe')

listing=Listbox(root)
listing.grid(row=2,column=0,rowspan=6,columnspan=3,padx=5,pady=5,sticky='nswe')
listing.bind('<<ListboxSelect>>',get_selected_row)

for i in range(4):
  root.grid_columnconfigure(i,weight=1)
for i in range(8):
  root.grid_rowconfigure(i,weight=1)

root.protocol("WM_DELETE_WINDOW",callback)
root.mainloop()