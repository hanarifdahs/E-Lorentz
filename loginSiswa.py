from tkinter import *
from tkinter import messagebox
import pymysql
import os


def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    winLogin.withdraw()

##________________LOGIN___________________##


def login():
    if nis.get() == "" or password.get() == "":
        messagebox.showerror(
            "Error", "Masukkan NIS dan Password", parent=winLogin)
    else:
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="lorentz")
            cur = con.cursor()

            cur.execute("SELECT * FROM siswa WHERE NIS = %s AND password = %s",
                        (nis.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "NIS atau Password Salah", parent=winLogin)
            else:
                messagebox.showinfo("Success", "Login Sukses", parent=winLogin)
                # createSession()
                close()
                openSoal()
                # question()
            con.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error Due to : {str(es)}", parent=winLogin)


def openSoal():
    close()
    os.system('python soal.py')


def signup():
    def action():
        if nis.get() == "" or nama.get() == "" or kelas.get() == "" or password.get() == "" or verify_pass.get() == "":
            messagebox.showerror(
                "Error", "Semua Data Harus Terisi", parent=winSignup)
        elif password.get() != verify_pass.get():
            messagebox.showerror(
                "Error", "Password dan Confirm Password harus sama", parent=winSignup)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="lorentz")
                cur = con.cursor()
                cur.execute("SELECT * FROM siswa WHERE NIS=%s", nis.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User Sudah Terdaftar", parent=winSignup)
                else:
                    cur.execute("INSERT INTO siswa (NIS, password, Nama, Kelas) VALUES(%s,%s,%s,%s)",
                                (
                                    nis.get(),
                                    password.get(),
                                    nama.get(),
                                    kelas.get()
                                )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Resgistrasi Berhasil", parent=winSignup)
                    clear()
                    switch()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=winSignup)

    # Close signup function

    def switch():
        winSignup.destroy()

    # Clear data funct
    def clear():
        nis.delete(0, END)
        password.delete(0, END)
        verify_pass.delete(0, END)
        nama.delete(0, END)
        kelas.delete(0, END)

    winSignup = Tk()
    winSignup.title("E-Lorentz - Signup")
    winSignup.maxsize(width=500, height=600)
    winSignup.minsize(width=500, height=600)
    winSignup.resizable(0, 0)

    heading = Label(winSignup, text="Signup", font="Verdana 20 bold")
    heading.place(x=80, y=60)

    nis = Label(winSignup, text="NIS : ", font="Verdana 20 bold")
    nis.place(x=80, y=60)

    nama = Label(winSignup, text="Nama", font="Verdana 20 bold")
    nama.place(x=80, y=193)

    kelas = Label(winSignup, text="Kelas", font="Verdana 20 bold")
    kelas.place(x=80, y=253)

    password = Label(winSignup, text="Password", font="Verdana 20 bold")
    password.place(x=80, y=313)

    verivyPass = Label(winSignup, text="Confirm Password :",
                       font="Verdana 20 bold")
    verivyPass.place(x=80, y=373)

    nis = StringVar()
    nama = StringVar()
    kelas = StringVar()
    password = StringVar()
    verify_pass = StringVar()

    nis = Entry(winSignup, width=30, textvariable=nis)
    nis.place(x=230, y=133)

    nama = Entry(winSignup, width=30, textvariable=nama)
    nama.place(x=230, y=193)

    kelas = Entry(winSignup, width=30, show="*", textvariable=kelas)
    kelas.place(x=230, y=253)

    password = Entry(winSignup, width=30, show="*", textvariable=password)
    password.place(x=230, y=313)

    verify_pass = Entry(winSignup, width=30, show="*",
                        textvariable=verify_pass)

    btnSignup = Button(winSignup, text="Signup",
                       font="Verdana 10 bold", command=action)
    btnSignup.place(x=200, y=413)

    btnLogin = Button(winSignup, text="Clear")
    btnLogin.place(x=280, y=413)

    btnBack = Button(winSignup, text="Kembali ke Login", command=switch)
    btnBack.place(x=350, y=20)

    winSignup.mainloop()


winLogin = Tk()
winLogin.title("E-Lorentz - Siswa Login")
winLogin.maxsize(width=500, height=500)
winLogin.minsize(width=500, height=500)
winLogin.resizable(0, 0)

heading = Label(winLogin, text="Login Siswa", font='Verdana 25 bold')
heading.place(x=80, y=150)

nis = Label(winLogin, text="NIS :", font='Verdana 10 bold')
nis.place(x=80, y=220)

userpass = Label(winLogin, text="Password :", font='Verdana 10 bold')
userpass.place(x=80, y=260)

nis = StringVar()
password = StringVar()

userentry = Entry(winLogin, width=40, textvariable=nis)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(winLogin, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

# button login and clear

btn_login = Button(winLogin, text="Login",
                   font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)


btn_login = Button(winLogin, text="Clear",
                   font='Verdana 10 bold', command=clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(winLogin, text="Registrasi User", command=signup)
sign_up_btn.place(x=350, y=20)


winLogin.mainloop()
