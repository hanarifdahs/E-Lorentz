# import paho mqtt
import paho.mqtt.client as mqtt
import pymysql
# import time for sleep()
import time
import json

db = pymysql.connect(host="localhost", user="root", password="",
                     database="datacenter")
cur = db.cursor()


def on_message(client, userdata, message):
    # print pesan
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    if message.topic == "fisika/soal":
        mdata = message.payload.decode()
        mdata = json.loads(mdata)
        print(mdata)
        print(mdata['iter'])
        miter = mdata["iter"]
        msoal = mdata["soal"]
        sql = """INSERT INTO soal (iter, soal) 
                                VALUES (%s, %s) """
        record = (miter, msoal)
        cur.execute(sql, record)
        db.commit()
    elif message.topic == "fisika/jawaban":
        mdata = message.payload.decode()
        mdata = json.loads(mdata)
        miter = mdata["iter"]
        msiswa = mdata["siswa"]
        mjawaban = mdata["jawaban"]
        malat = mdata["alat"]
        sql = "INSERT INTO datacenter ( iter, siswa, jawaban, alat ) VALUES ( %s, %s, %s, %s )", (
            miter, msiswa, mjawaban, malat)
        cur.execute(sql)
    else:
        print("tes")


########################################


def on_connect(client, userdata, flags, rc):
    client.subscribe("fisika/#")


# buat definisi nama broker yang akan digunakan
broker_address = "localhost"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

client.on_message = on_message
client.on_connect = on_connect

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)
client.loop_start()
# # jalankan loop client
#

# client melakukan subsribe ke topik 1
print("Subscribe to Topic", "fisika/#")

while True:
    time.sleep(1)
# stop loop
