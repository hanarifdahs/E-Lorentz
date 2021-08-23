from tkinter import *
import pymysql
import json


class Quiz:
    def __init__(self, root):
        self.root = root
        self.question = StringVar()
        self.entryColumn = StringVar()
        self.btnNext = StringVar()
        self.btnQuit = StringVar()
        # self.alat = StringVar()
        self.itersoal = []
        self.iter = 0
        self.questionNumber = 1
        self.soal = []
        self.miter = []
        self.jawaban = []
        # self.mdatas = []
        self.getSoal()
        self.initUI()

    def initUI(self):
        judul = Label(self.root, text="Soal", width=50, bg="blue",
                      fg="white", font=("times", 20, "bold"))
        judul.place(x=0, y=2)
        dik = Label(self.root, text="Hitung Gaya Lorentz dengan memasukkan Diketahui sesuai soal ke dalam E-Lorentz \n dengan menggunakan Keypad yang tersedia, # untuk enter dan * untuk backspace", width=80,
                    fg="black", font=("times", 13, "bold"))
        dik.place(x=2, y=70)
        self.question.set(str(self.questionNumber)+". " +
                          self.soal[self.iter])

        questionIter = Label(self.root, textvariable=self.question, width=70,
                             font=("times", 12, "bold"), anchor="w")
        questionIter.place(x=70, y=160)
        self.entryColumn = Entry(self.root, width=60,
                                 font=("times", 16, "bold"))
        self.entryColumn.place(x=70, y=260)

        self.btnNext = Button(self.root, text="Next", command=self.nextQuest,
                              width=10, bg="green", fg="white", font=("times", 16, "bold"))
        self.btnNext.place(x=200, y=380)
        self.btnQuit = Button(self.root, text="Quit", command=self.root.destroy,
                              width=10, bg="red", fg="white", font=("times", 16, "bold"))
        self.btnQuit.place(x=400, y=380)

    def nextQuest(self):
        self.jawaban.append(self.entryColumn.get())
        if self.iter == len(self.soal)-1:
            print("selesai")
            selesai = Label(
                self.root, text="Anda Telah Menyelesaikan Praktikum Gaya Lorentz",
                width=60, font=("times", 16, "bold"))
            selesai.place(x=50, y=100)
            self.entryColumn.destroy()
            self.btnNext.destroy()
            self.btnQuit.place(x=325, y=380)
            self.insertjawaban()
        else:
            self.iter += 1
            self.questionNumber += 1
            self.question.set(str(self.questionNumber)+". " +
                              self.soal[self.iter])
            self.entryColumn.delete(0, END)

    def getSoal(self):
        db = pymysql.connect(host="localhost", user="root", password="",
                             database="lorentz")
        cur = db.cursor()
        sql = "SELECT soal FROM soal"
        cur.execute(sql)
        self.soal = [i[0] for i in cur.fetchall()]
        query = "SELECT nomor FROM soal"
        cur.execute(query)
        self.miter = [i[0] for i in cur.fetchall()]

    def insertjawaban(self):
        with open('jawaban.txt', 'w') as filehandle:
            # store the data as binary data stream
            json.dump(self.jawaban, filehandle)
            filehandle.close()
        # with open("session_nis.txt", "r") as file:
        #     self.nis = file.read()
        # db = pymysql.connect(host="localhost", user="root", password="",
        #                      database="lorentz")
        # cur = db.cursor()
        # for i in range(len(self.miter)):
        #     query = """UPDATE jawaban SET jawabansiswa = %s WHERE NIS = %s AND nomor = %s"""
        #     record = (self.jawaban[i], self.nis, self.miter[i])
        #     cur.execute(query, record)
        # db.commit()
        # db.close()
        # def on_publish(client, userdata, result):
        #     print("Data Published \n")
        # # broker = "localhost"
        # broker = "broker.hivemq.com"
        # port = 1883
        # print("Creating New Instance")
        # with open("session_nis.txt", "r") as file:
        #     self.nis = file.read()
        # # with open("alat.txt", "r") as f:
        # #     self.alat = f.read()
        # for i in range(len(self.miter)):

        #     client = mqtt.Client("Soal")
        #     client.on_publish = on_publish
        #     print("Connecting to Broker")
        #     client.connect(broker, port=port)
        #     client.loop_start()
        #     print("Send Question")
        #     time.sleep(1)
        #     mdata = {"iter": self.miter[i],
        #              "NIS": self.nis,
        #              "jawaban": self.jawaban[i],
        #              "alat": self.alat[i]}
        #     print(mdata)
        #     mdata = json.dumps(mdata)
        #     client.publish("fisika/jawaban", mdata)
        #     client.loop_stop()

    # def bacasensor(self):
    #     port = serial.Serial("COM7", 115200)
    #     time.sleep(1)
    #     while True:
    #         port.write('a')
    #         ch = port.readline().strip()
    #         lorentz = float(ch)
    #         print("Gaya Lorentz: ", lorentz)
    #         time.sleep(3)


root = Tk()
root.geometry("800x500")
root.resizable(0, 0)
root.title("E-Lorentz - Soal")
quiz = Quiz(root)
root.mainloop()
