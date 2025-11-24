import mysql.connector

def koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Ubah jika username MySQL berbeda
        password="",         # Isi password MySQL jika ada
        database="uas_pmi"       # Sesuaikan nama database
    )

def kembali(window, target):
    window.destroy()
    target()
