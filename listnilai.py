from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
import os

from pymysql.connections import DEFAULT_USER
from pymysql.cursors import Cursor


#### CONNECT DB ###
db = pymysql.connect(host="localhost", user="root", passwd="", db="lorentz")
cursor = db.cursor()

#### MAIN WINDOW ###
root = Tk()
root.title("List Nilai")
root.state('zoomed')


wrapper1 = LabelFrame(root, text="List Nilai")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Tambah Siswa")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

###  WRAPPER 1 ###


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)


trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4),
                   show="headings", height="5")
trv.pack()


trv.heading(1, text="nip")
trv.heading(2, text="Nama")
trv.heading(3, text="Kelas")
trv.heading(4, text="Nilai")


query = "SELECT nip, Nama, Kelas, Nilai from siswa"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# WRAPPER 2

### SEARCH BY NAME ###

q = StringVar()


def searchall():
    q2 = q.get()
    query = "SELECT nip, Nama, Kelas FROM siswa WHERE Nama LIKE '%" + \
        q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


def clear():
    ent.delete(0, END)
    query = "SELECT nip, Nama, Kelas, Nilai FROM siswa"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=searchall)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)

### SEARCH BY CLASS ####
sql = "SELECT Kelas FROM siswa"
kelaslist = []
cursor.execute(sql)
results = cursor.fetchall()
for a in results:
    data = (a[0])
    if data not in kelaslist:
        kelaslist.append(data)
        print(data)
selected = StringVar(root)
selected.set("Pilih kelas")
dropdown = OptionMenu(wrapper2, root, selected.get(), *kelaslist)
dropdown.pack(side=tk.LEFT, padx=100)

# USER DATA SECTION - WRAPPER 3#
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()


def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])


trv.bind('<Double 1>', getrow)


def update_siswa():
    nip = ent1.get()
    nama = ent2.get()
    kelas = ent3.get()
    # query = "UPDATE siswa SET nip = '%s', Nama = '%s', Kelas = '%s' WHERE nip = '%s'"
    query = "UPDATE SISWA SET nip = '{0}', Nama = '{1}', Kelas = '{2}' WHERE nip = '{0}'".format(
        nip, nama, kelas)
    cursor.execute(query)
    db.commit()
    clear()


def add_new():
    nip = t1.get()
    nama = t2.get()
    kelas = t3.get()
    query = "INSERT INTO siswa(nip, Nama, Kelas) VALUES ('{0}','{1}','{2}')".format(
        nip, nama, kelas)
    cursor.execute(query)
    db.commit()
    clear()


def delete_siswa():
    nip = t1.get()
    query = "DELETE FROM siswa WHERE nip = "+nip
    cursor.execute(query)
    db.commit()
    clear()


def clear_search():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)


def close():
    root.destroy()


def callUploadSoal():
    close()
    os.system('python upload.py')


lbl1 = Label(wrapper3, text='nip')
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Nama")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Kelas")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

up_btn = Button(wrapper3, text="Update Siswa", command=update_siswa)
addbtn = Button(wrapper3, text="Tambah Siswa", command=add_new)
delete_btn = Button(wrapper3, text="Delete Siswa", command=delete_siswa)
clear_btn = Button(wrapper3, text="Clear", command=clear_search)

up_btn.grid(row=4, column=1, padx=5, pady=3)
addbtn.grid(row=4, column=0, padx=5, pady=3)
delete_btn.grid(row=4, column=2, padx=5, pady=3)
clear_btn.grid(row=4, column=3, padx=30, pady=3)

btnUploadSoal = Button(wrapper3, text="Upload Soal Guru",
                       command=callUploadSoal,
                       width=20, bg="green", fg="white", font=("times", 11, "bold"))
btnUploadSoal.place(x=700, y=97)


### END ###
root.mainloop()
db.close()
