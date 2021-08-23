import paho.mqtt.client as mqtt
import pymysql
import time
import json

db = pymysql.connect(host="localhost", user="root", password="",
                     database="lorentz")
cur = db.cursor()

jawabanAlat = []


def on_message(client, userdata, message):
    # print pesan
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    msg = str(message.payload.decode())
    jawabanAlat.append(msg)
    print(jawabanAlat)


with open("session_nis.txt", "r") as file:
    nis = file.read()

query = "SELECT * FROM jawaban WHERE NIS = %s ORDER BY nomor"
record = nis
cur.execute(query, record)
result = cur.fetchall()


# queryNIS = "SELECT NIS FROM jawaban WHERE NIS = %s"
# cur.execute(queryNIS)
# mnis = [i[0] for i in cur.fetchall()]
# cur.execute("SELECT nomor FROM soal")
# nomor = [i[0] for i in cur.fetchall()]
# print(mnis)
# print(nomor)
# with open("session_nis.txt", "r") as file:
#     nis = file.read()
# for i in range(len(nomor)):
#     if nis == mnis[i]:
#         sql = """UPDATE jawaban SET jawabanalat = %s WHERE NIS = %s AND nomor = %s"""
#         r = (jawabanAlat[i], mnis[i], nomor[i])
#         cur.execute(sql, r)
# db.commit()
# db.close()


def on_connect(client, userdata, flags, rc):
    client.subscribe("fisika/#")


try:
    broker_address = "broker.hivemq.com"
    print("creating new instance")
    client = mqtt.Client("P1")

    client.on_message = on_message
    client.on_connect = on_connect

    print("connecting to broker")
    client.connect(broker_address, port=1883)
    client.loop_start()
    print("Subscribe to Topic", "fisika/#")
    with open("jawaban.txt", "w") as file:
        json.dump([], file)
        file.close()

    while True:
        print("ok", len(result))
        print(len(jawabanAlat))
        with open("jawaban.txt", "r") as f:
            jawaban = json.load(f)
            # f.close()
        if len(result) == len(jawabanAlat) and len(result) == len(jawaban):

            print(jawaban)
            for i in range(len(jawabanAlat)):
                query = """UPDATE jawaban SET jawabanalat = %s , jawabansiswa = %s WHERE NIS = %s AND nomor = %s"""
                record = (jawabanAlat[i], jawaban[i], nis, result[i][1])
                print(record)
                cur.execute(query, record)
            db.commit()
            db.close()
            break
        time.sleep(1)
    # stop loop

except KeyboardInterrupt:
    print("Received Messages:")
    for message in jawabanAlat:
        print(message)
