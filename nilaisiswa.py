from tkinter.constants import FALSE, TRUE
import pymysql
import math

database = pymysql.connect(
    host="localhost", user="root", passwd="", db="lorentz")
cur = database.cursor()

with open("session_guru.txt", "r") as file:
    nip = file.read()

query = "SELECT * FROM siswa WHERE NIP = %s"
r = (nip)
cur.execute(query, r)
data = cur.fetchall()
print(data)


def totalNilai(hasil):
    total = hasil.count(TRUE)
    return total


def nilai(data):
    results = []
    for i in range(len(data)):
        if data[i][0] == data[i][1]:
            result = TRUE
        else:
            result = FALSE
        results.append(result)
    return results


for i in range(len(data)):
    query = "SELECT jawabansiswa, jawabanalat FROM jawaban WHERE NIS = %s"
    record = (data[i][0])
    cur.execute(query, record)
    result = cur.fetchall()
    temp = nilai(result)
    print(temp)
    total = totalNilai(temp)
    print(total)
    s = """UPDATE siswa SET nilai = %s WHERE NIS = %s"""
    r = (total, data[i][0])
    cur.execute(s, r)
    database.commit()
