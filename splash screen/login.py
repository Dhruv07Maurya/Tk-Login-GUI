from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from subprocess import call

login=Tk()
def openn():
    call(["python","splaash.py"])
    login.destroy()
    
def get_data():
        
    username=usernameEntry.get()
    password=PasswordEntry.get()
    if username=='' or password=='' :
        messagebox.showerror('Error','Username or Password cannot be empty')
        return
    elif username=='a' or password=='a':
        #  messagebox.showinfo('Success','Loggedin Successfully')
         openn()
         

    else:
        messagebox.showerror('Incorrect','password or Username must be Incorrect')
    # heading.configure(text=username)
    print(username + " " + password)

login.geometry('990x660+200+10')
bgImage=ImageTk.PhotoImage(file='bglog.png')
bgLabel=Label(login,image=bgImage)
bgLabel.pack()
login.title('Login Page')


heading=Label(login,text='USER LOGIN',font=('Georgia',23,'bold'),bg='white',fg='green')
heading.place(x=124,y=120)
usernameEntry=Entry(login,width=25,font=('Times',13),bd=0,fg='black')
usernameEntry.place(x=124,y=200)
usernameEntry.insert(0,'Username')
frame1=Frame(login, width=250,height=2,bg='green')
frame1.place(x=124,y=220)

PasswordEntry=Entry(login,width=25,font=('Times',13),bd=0,fg='black')
PasswordEntry.place(x=124,y=260)
PasswordEntry.configure(show='*')
frame2=Frame(login, width=250,height=2,bg='green').place(x=124,y=282)

forgetbutton=Button(login,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',fg='green').place(x=270,y=295)

loginbutton=Button(login,text='Login',font=('open sans',16,'bold'),fg='white',bg='green',activeforeground='white',activebackground='green',cursor='hand2',bd=0,width=19, command=get_data).place(x=124,y=360)

orlabel=Label(login,text="--------------- OR -------------- ",font=('open sans',16),bg='white',fg='green').place(x=124,y=420)


facebook=PhotoImage(file='facebook.png')
fb=Label(login,image=facebook,bg='white').place(x=180,y=470)

google=PhotoImage(file='google.png')
fb=Label(login,image=google,bg='white').place(x=230,y=470)

twitter=PhotoImage(file='twitter.png')
fb=Label(login,image=twitter,bg='white').place(x=280,y=470)


dha=Label(login,text="Don't have an Account?",font=('open sans',9,'bold'),bg='white',fg='green').place(x=124,y=530)

dhabutton=Button(login,text='Create New One',font=('open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='white',activebackground='grey',cursor='hand2',bd=0).place(x=270,y=530)



login.mainloop()
