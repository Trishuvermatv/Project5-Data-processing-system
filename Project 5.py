from tkinter import *
from tkinter import messagebox

from db import Database

db=Database("Data.dat")

def populate_list():
    ID_NUMs_list.delete(0,END)
    for row in db.fetch():
        ID_NUMs_list.insert(END, row)
    updateTextFile()

    
def add_item():
    if ID_NUM_text.get()=='' or Name_text.get()=='' or DOB_text.get()=='' or Gender_text.get()=='' or School_text.get()=='' or City_text.get()=='':
        messagebox.showerror('Required Fields','Please include all fields')
        return
    db.insert(ID_NUM_text.get(),Name_text.get(),DOB_text.get(),Gender_text.get(),School_text.get(),City_text.get())
    ID_NUMs_list.delete(0,END)
    ID_NUMs_list.insert(END,(ID_NUM_text.get(),Name_text.get(),DOB_text.get(),Gender_text.get(),School_text.get(),City_text.get()))
    clear_item()
    populate_list()
    
    
def select_item(event):
    try:
        global selected_item
        index=ID_NUMs_list.curselection()[0]
        selected_item=ID_NUMs_list.get(index)
        ID_NUM_entry.delete(0,END)
        ID_NUM_entry.insert(END,selected_item[1])
        Name_entry.delete(0,END)
        Name_entry.insert(END,selected_item[2])
        DOB_entry.delete(0,END)
        DOB_entry.insert(END,selected_item[3])
        Gender_entry.delete(0,END)
        Gender_entry.insert(END,selected_item[4])
        School_entry.delete(0,END)
        School_entry.insert(END,selected_item[5])
        City_entry.delete(0,END)
        City_entry.insert(END,selected_item[6])
    except IndexError:
        pass
    
def update_item():  
    db.update(selected_item[0],ID_NUM_text.get(),Name_text.get(),DOB_text.get(),Gender_text.get(),School_text.get(),City_text.get())
    populate_list()
    
    
def remove_item():
    db.remove(selected_item[0])
    clear_item()
    populate_list()
    
    
def clear_item():
    ID_NUM_entry.delete(0,END)
    Name_entry.delete(0,END)
    DOB_entry.delete(0,END)
    Gender_entry.delete(0,END)
    School_entry.delete(0,END)
    City_entry.delete(0,END)
    

def search_item():
    searched_item=db.search(Search_text.get())
    ID_NUM_entry.delete(0,END)
    ID_NUM_entry.insert(END,searched_item[0][1])
    Name_entry.delete(0,END)
    Name_entry.insert(END,searched_item[0][2])
    DOB_entry.delete(0,END)
    DOB_entry.insert(END,searched_item[0][3])
    Gender_entry.delete(0,END)
    Gender_entry.insert(END,searched_item[0][4])
    School_entry.delete(0,END)
    School_entry.insert(END,searched_item[0][5])
    City_entry.delete(0,END)
    City_entry.insert(END,searched_item[0][6])
        
    
#create window object
app =Tk()
#ID_NUM
ID_NUM_text =StringVar()
ID_NUM_label=Label(app,text='ID_NUM',font=('bold',14), pady=10,padx=20)
ID_NUM_label.grid(row=0,column=0,sticky=W)
ID_NUM_entry=Entry(app,textvariable=ID_NUM_text)
ID_NUM_entry.grid(row=0,column=1)

#Name
Name_text =StringVar()
Name_label=Label(app,text='Name',font=('bold',14),padx=40)
Name_label.grid(row=0,column=2,sticky=W)
Name_entry=Entry(app,textvariable=Name_text)
Name_entry.grid(row=0,column=3)

#DOB
DOB_text =StringVar()
DOB_label=Label(app,text='DOB',font=('bold',14),padx=20)
DOB_label.grid(row=1,column=0,sticky=W)
DOB_entry=Entry(app,textvariable=DOB_text)
DOB_entry.grid(row=1,column=1)

#Gender
Gender_text =StringVar()
Gender_label=Label(app,text='Gender',font=('bold',14),padx=40)
Gender_label.grid(row=1,column=2,sticky=W)
Gender_entry=Entry(app,textvariable=Gender_text)
Gender_entry.grid(row=1,column=3)

#School
School_text =StringVar()
School_label=Label(app,text='School',font=('bold',14), pady=10,padx=20)
School_label.grid(row=2,column=0,sticky=W)
School_entry=Entry(app,textvariable=School_text)
School_entry.grid(row=2,column=1)

#City
City_text =StringVar()
City_label=Label(app,text='City',font=('bold',14), pady=10,padx=40)
City_label.grid(row=2,column=2,sticky=W)
City_entry=Entry(app,textvariable=City_text)
City_entry.grid(row=2,column=3)

#ID_NUM list(Listbox)
ID_NUMs_list=Listbox(app,height=8,width=50,border=2)
ID_NUMs_list.grid(row=4,column=0,columnspan=4,rowspan=6,pady=20,padx=10)

#create scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=4,column=4,pady=20,ipady=50,sticky=W)

#set scroll to listbox
ID_NUMs_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=ID_NUMs_list.yview)


#Bind Select
ID_NUMs_list.bind('<<ListboxSelect>>',select_item)



#Buttons
add_btn=Button(app,text='Add Entry',width=12,command=add_item)
add_btn.grid(row=3,column=0,pady=20)

add_btn=Button(app,text='Clear',width=12,command=clear_item)
add_btn.grid(row=3,column=1,pady=20)

add_btn=Button(app,text='Update',width=12,command=update_item)
add_btn.grid(row=3,column=2,pady=20)

add_btn=Button(app,text='Remove',width=12,command=remove_item)
add_btn.grid(row=3,column=3,pady=20)


#Search Box
Search_text =StringVar()
Search_entry=Entry(app,textvariable=Search_text)
Search_entry.grid(row=5,column=1)
add_btn=Button(app,text='Search',width=12,command=search_item)
add_btn.grid(row=5,column=2,pady=20)

#Write file to txt file
def updateTextFile():
    data = db.fetch()
    f = open("dbData.txt", "w+")
    for s in data:
        f.write(str(s)+"\n")
    f.close()
    f = open("dbData.txt", "r")

#populate data
populate_list()


app.title("Data Manager")
app.geometry("550x500")
#start program
app.mainloop()
