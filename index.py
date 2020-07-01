#imoporta as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#criar Nossa janela
jan = Tk()
jan.title("DP Systtems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9 )
jan.iconbitmap(default="icons/logoIcon.ico")

#img
logo = PhotoImage(file="icons/logo.png")

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#usuario
UserLabel = Label(RightFrame, text="Usuario:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=125, y=110)

#SENHA
PassLabel = Label(RightFrame, text="Senha", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = Entry(RightFrame, width=30, show="*")
PassEntry.place(x=125, y=160)

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=125, y=200)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=20 )
RegisterButton.place(x=150, y=250)



jan.mainloop()