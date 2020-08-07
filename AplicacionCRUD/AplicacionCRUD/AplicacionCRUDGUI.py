from tkinter import messagebox
from tkinter import *
import DataBaseManager



root=Tk()
frame = Frame(root)
frame.pack()


idTextVar=StringVar()
nameTextVar=StringVar()
passwordTextVar=StringVar()
lastNameTextVar=StringVar()
directionTextVar=StringVar()

#--------------- Function Button----------------------------

def Exit():
    value=messagebox.askquestion(title="Exit",message="Do you want to exit?")
    if value == "yes":
        root.destroy()

def DeleteMenu():
    global idTextVar
    global nameTextVar
    global passwordTextVar
    global lastNameTextVar
    global directionTextVar
    global commentText
    idTextVar.set("")
    nameTextVar.set("")
    passwordTextVar.set("")
    lastNameTextVar.set("")
    directionTextVar.set("")
    commentText.delete(1.0,"end")

def CreateMenu():
    try:
        DataBaseManager.CreateDataBase()
        messagebox.showinfo(title="Data base created",message="The data base has been created")
    except:
        messagebox.showwarning(title="Create Database",message="We have a data base")

def CreateButton():
    global nameTextVar
    global passwordTextVar
    global lastNameTextVar
    global directionTextVar
    global commentText
    DataBaseManager.InsertTuple(nameTextVar.get(),passwordTextVar.get(),lastNameTextVar.get(),
                                directionTextVar.get(),commentText.get(1.0,"end"))
    messagebox.showinfo(title="Tuple Inserted",message="The tuple has been inserted")

def ReadButton():
    global idTextVar
    global nameTextVar
    global passwordTextVar
    global lastNameTextVar
    global directionTextVar
    global commentText   
    try:
        ret=DataBaseManager.ReadTuple(int(idTextVar.get()))
        nameTextVar.set(ret[0][1])
        passwordTextVar.set(ret[0][2])
        lastNameTextVar.set(ret[0][3])
        directionTextVar.set(ret[0][4])
        commentText.delete(1.0,"end")
        commentText.insert(1.0,ret[0][5])
    except:
        messagebox.showerror(title="Index_Error",message="Id its not found")
        DeleteMenu()


def UpdateButton():
    global idTextVar
    global nameTextVar
    global passwordTextVar
    global lastNameTextVar
    global directionTextVar
    global commentText   
    DataBaseManager.UpdateTuple(idTextVar.get(),nameTextVar.get(),passwordTextVar.get(),lastNameTextVar.get(),
                                directionTextVar.get(),commentText.get(1.0,"end"))
    messagebox.showinfo(title="Tuple Update",message="The tuple with id: {}, has been updated".format(idTextVar.get()))

 
def DeleteButton():
    global idTextVar
    DataBaseManager.DeleteTuple(idTextVar.get())
    DeleteMenu()

#-----------------Create the menu bar--------------------------
menuBar = Menu(root)
root.config(menu=menuBar)


baseDataMenu = Menu(menuBar,tearoff=0)
deleteMenu = Menu(menuBar,tearoff=0)
crudMenu = Menu(menuBar,tearoff=0)
helpMenu = Menu(menuBar,tearoff=0)

menuBar.add_cascade(label="BBDD",menu=baseDataMenu)
baseDataMenu.add_command(label="Conect",command=CreateMenu)
baseDataMenu.add_command(label="Exit",command=Exit)


menuBar.add_cascade(label="Delete",menu=deleteMenu)
deleteMenu.add_command(label="Clear Fields",command=DeleteMenu)

menuBar.add_cascade(label="CRUD",menu=crudMenu)
crudMenu.add_command(label="Create",command=CreateButton)
crudMenu.add_command(label="Read",command=ReadButton)
crudMenu.add_command(label="Update",command=UpdateButton)
crudMenu.add_command(label="Delete",command=DeleteMenu)

menuBar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="License")
helpMenu.add_command(label="About...")

#-------------------------------------------------------
#-----------------------Create text box---------------
idLabel= Label(frame,text="Id: ",pady=10,padx=10)
idLabel.grid(row=0,column=0)
idText = Entry(frame,textvariable=idTextVar)
idText.grid(row=0,column=1,columnspan=3)


nameLabel= Label(frame,text="Name: ",pady=10,padx=10)
nameLabel.grid(row=1,column=0)
nameText= Entry(frame,textvariable=nameTextVar)
nameText.grid(row=1,column=1,columnspan=3)

passwordLabel=Label(frame,text="Password: ",pady=10,padx=10)
passwordLabel.grid(row=2,column=0)
passwordText=Entry(frame,textvariable=passwordTextVar)
passwordText.grid(row=2,column=1,columnspan=3)
passwordText.config(show="*")

lastNameLabel=Label(frame,text="Last Name: ",pady=10,padx=10)
lastNameLabel.grid(row=3,column=0)
lastNameText=Entry(frame,textvariable=lastNameTextVar)
lastNameText.grid(row=3,column=1,columnspan=3)

directionLabel=Label(frame,text="Direcction: ",pady=10,padx=10)
directionLabel.grid(row=4,column=0)
directionText=Entry(frame,textvariable=directionTextVar)
directionText.grid(row=4,column=1,columnspan=3)

commentLabel = Label(frame,text = "Comment: ",pady=10,padx=10)
commentLabel.grid(row=5,column=0)
commentText= Text(frame,width = 20,height=10,pady=10,padx=10)
commentText.grid(row=5,column=1,columnspan=3)
commentScrollBar = Scrollbar(frame,command=commentText.yview)
commentScrollBar.grid(row=5,column=4,sticky="nsew")
commentText.config(yscrollcommand=commentScrollBar.set)


#------------------------------------------------------------



#-----------------Crear botones inferiores ------------------

createButton = Button(frame,text="Create",command=CreateButton)
createButton.grid(row=6,column=0,pady=10)
readButton = Button(frame,text="Read",command=ReadButton)
readButton.grid(row=6,column=1,pady=10)
updateButton = Button(frame,text="Update",command=UpdateButton)
updateButton.grid(row=6,column=2,pady=10)
deleteButton = Button(frame,text="Delete",command=DeleteButton)
deleteButton.grid(row=6,column=3,pady=10)






root.mainloop();


