from tkinter import *
from tkinter import messagebox
import paho.mqtt.client as mqtt
import time
import os
import json


class Uploadquestion:
    def __init__(self, root):
        self.root = root
        self.question = StringVar()
        self.questionIter = 0
        self.questionNumber = 1
        self.initUI()

    def initUI(self):
        t = Label(self.root, text="Upload Soal", width=50, bg="blue",
                  fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        self.question.set(str(self.questionNumber))
        questionNumber = Label(
            self.root, textvariable=self.question, width=60, font=("times", 16, "bold"), anchor="w")
        questionNumber.place(x=110, y=170)
        self.entryColumn = Entry(
            self.root, width=50, font=("times", 16, "bold"))
        self.entryColumn.get()
        self.entryColumn.place(x=150, y=170)
        submitBtn = Button(self.root, text="Submit", command=self.btnSubmit,
                           width=10, bg="red", fg="white", font=("times", 16, "bold"))
        submitBtn.place(x=245, y=380)
        listnilaiBtn = Button(self.root, text="List Nilai", command=self.openListnilai,
                              width=10, bg="green", fg="white", font=("times", 16, "bold"))
        listnilaiBtn.place(x=475, y=380)

    def btnSubmit(self):

        def on_publish(client, userdata, result):
            print("Data Published \n")

        broker_address = "localhost"
        port = 1883
        print("Creating New Instance")
        client = mqtt.Client("NIP-123")
        client.on_publish = on_publish
        print("Connecting to Broker")
        client.connect(broker_address, port=port)

        client.loop_start()
        print("Publish Question")
        time.sleep(1)
        self.questionIter += 1
        mdata = {"iter": self.questionIter,
                 "soal": self.entryColumn.get()}
        print(mdata)
        mdata = json.dumps(mdata)
        client.publish("fisika/soal", mdata)
        print(self.entryColumn.get())
        client.loop_stop()
        self.questionNumber += 1
        self.entryColumn.delete(0, END)

    def openListnilai(self):
        close()
        os.system("python listnilai.py")

    def exit():
        sure = messagebox.askyesno(
            "exit", "Apakah Yakin Ingin Keluar")
        if sure == True:
            root.destroy()


def close():
    root.destroy()


root = Tk()
root.geometry("800x500")
root.resizable(0, 0)
root.title("E-Lorentz - Guru")
Uploadquestion(root)
root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()
