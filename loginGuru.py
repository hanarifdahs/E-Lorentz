from tkinter import *
from tkinter import messagebox
import pymysql
import os


def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    winlogin.withdraw()


def exit():
    sure = messagebox.askyesno(
        "exit", "Apakah Yakin Ingin Keluar")
    if sure == True:
        winlogin.destroy()

##________________LOGIN___________________##


def login():
    if nip.get() == "" or password.get() == "":
        messagebox.showerror(
            "Error", "Masukkan NIP dan Password", parent=winlogin)
    else:
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="lorentz")
            cur = con.cursor()

            cur.execute("SELECT * FROM guru WHERE NIP = %s AND password = %s",
                        (nip.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "NIP atau Password Salah", parent=winlogin)
            else:
                messagebox.showinfo("Success", "Login Sukses", parent=winlogin)
                createSession()
                close()
                uploadSoal()
                # subscriber()

            con.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error Due to : {str(es)}", parent=winlogin)


def createSession():
    with open("session_guru.txt", "w") as file:
        file.write(nip.get())
        file.close()


def uploadSoal():
    close()
    os.system('python upload.py')


def subscriber():

    os.system('pythonw subscribe.pyw')

###_______________________SIGNUP___________________##


def signup():
    def action():
        if nip.get() == "" or nama.get() == "" or password.get() == "" or verify_pass.get() == "":
            messagebox.showerror(
                "Error", "Semua Data Harus Terisi", parent=winsignup)
        elif password.get() != verify_pass.get():
            messagebox.showerror(
                "Error", "Password dan Confirm Password harus sama", parent=winsignup)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="lorentz")
                cur = con.cursor()
                cur.execute("SELECT * FROM guru WHERE NIP=%s", nip.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User Sudah Terdaftar", parent=winsignup)
                else:
                    cur.execute("INSERT INTO guru (nip, password, Nama) VALUES(%s,%s,%s)",
                                (
                                    nip.get(),
                                    password.get(),
                                    nama.get()
                                )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Resgistrasi Berhasil", parent=winsignup)
                    clear()
                    switch()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=winsignup)

    # Close signup function

    def switch():
        winsignup.destroy()

    # Clear data funct
    def clear():
        nip.delete(0, END)
        password.delete(0, END)
        verify_pass.delete(0, END)
        nama.delete(0, END)

    # Start Signup Window
    winsignup = Tk()
    winsignup.title("E-Lorentz")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    # Heading Label
    heading = Label(winsignup, text="Signup", font="Verdana 20 bold")
    heading.place(x=80, y=60)

    # Form data signup label
    nip = Label(winsignup, text="NIP :", font='Verdana 10 bold')
    nip.place(x=80, y=133)

    nama = Label(winsignup, text="Nama: ", font="Verdana 10 bold")
    nama.place(x=80, y=193)

    password = Label(winsignup, text="Password :", font="Verdana 10 bold")
    password.place(x=80, y=253)

    verify_pass = Label(winsignup, text="Confirm Password :",
                        font="Verdana 10 bold")
    verify_pass.place(x=80, y=313)

    # Form data signup Entry box
    nip = StringVar()
    nama = StringVar()
    password = StringVar()
    verify_pass = StringVar()

    nip = Entry(winsignup, width=30, textvariable=nip)
    nip.place(x=230, y=133)

    nama = Entry(winsignup, width=30, textvariable=nama)
    nama.place(x=230, y=193)

    password = Entry(winsignup, width=30, show="*", textvariable=password)
    password.place(x=230, y=253)

    verify_pass = Entry(winsignup, width=30, show="*",
                        textvariable=verify_pass)
    verify_pass.place(x=230, y=315)

    # Button Login and Clear

    btn_signup = Button(winsignup, text="Signup",
                        font="verdana 10 bold", command=action)
    btn_signup.place(x=200, y=413)

    btn_login = Button(winsignup, text="Clear",
                       font='Verdana 10 bold', command=clear)
    btn_login.place(x=280, y=413)

    sign_up_btn = Button(winsignup, text="Kembali ke Login", command=switch)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()

# ------------------------------------------------------------ Login Window -----------------------------------------


winlogin = Tk()

# app title
winlogin.title("E-Lorentz")

# window size
winlogin.maxsize(width=500,  height=500)
winlogin.minsize(width=500,  height=500)

winlogin.protocol("WM_DELETE_WINDOW", exit)

# heading label
heading = Label(winlogin, text="Login Guru", font='Verdana 25 bold')
heading.place(x=80, y=150)

nip = Label(winlogin, text="NIP :", font='Verdana 10 bold')
nip.place(x=80, y=220)

userpass = Label(winlogin, text="Password :", font='Verdana 10 bold')
userpass.place(x=80, y=260)

# Entry Box
nip = StringVar()
password = StringVar()

userentry = Entry(winlogin, width=40, textvariable=nip)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(winlogin, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)


# button login and clear

btn_login = Button(winlogin, text="Login",
                   font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)


btn_login = Button(winlogin, text="Clear",
                   font='Verdana 10 bold', command=clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(winlogin, text="Registrasi User", command=signup)
sign_up_btn.place(x=350, y=20)


winlogin.mainloop()
