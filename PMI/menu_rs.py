import tkinter as tk
from tkinter import messagebox
import mysql.connector
from utils_file import kembali_login

# koneksi database
def koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uas_pmi"
    )

def menu_rs(parent):
    if parent is not None:
        parent.destroy()

    win = tk.Tk()
    win.title("Menu Rumah Sakit")
    win.geometry("350x300")

    tk.Label(win, text="Menu Rumah Sakit", font=("Arial", 14)).pack(pady=10)

    tk.Button(win, text="Cek Stok Darah", width=20, command=lambda: cek_stok(win)).pack(pady=5)
    tk.Button(win, text="Permintaan Darah", width=20, command=lambda: minta_darah(win)).pack(pady=5)
    tk.Button(win, text="Kembali ke Login", width=20, command=lambda: kembali_login(win)).pack(pady=20)

    win.mainloop()

# ====== CEK STOK DARAH =======
def cek_stok(parent):
    parent.destroy()
    win = tk.Tk()
    win.title("Cek Stok Darah")

    tk.Label(win, text="Stok Darah PMI", font=("Arial", 14)).pack(pady=10)

    db = koneksi()
    cur = db.cursor()
    cur.execute("SELECT golongan_id, jumlah_kantong FROM stok_darah")
    data = cur.fetchall()

    for row in data:
        tk.Label(win, text=f"Golongan {row[0]} : {row[1]} kantong").pack()

    db.close()

    tk.Button(win, text="Kembali", command=lambda: menu_rs(win)).pack(pady=10)
    win.mainloop()

# ====== PERMINTAAN DARAH =======
def minta_darah(parent):
    parent.destroy()
    win = tk.Tk()
    win.title("Permintaan Darah")

    tk.Label(win, text="Permintaan Darah", font=("Arial", 14)).pack(pady=10)

    tk.Label(win, text="Golongan Darah:").pack()
    g = tk.Entry(win)
    g.pack()

    tk.Label(win, text="Jumlah Kantong:").pack()
    j = tk.Entry(win)
    j.pack()

    def kirim_permintaan():
        gol = g.get()
        try:
            jumlah = int(j.get())
        except:
            messagebox.showerror("Error", "Jumlah harus angka!")
            return

        db = koneksi()
        cur = db.cursor()

        # cek stok
        cur.execute("SELECT jumlah_kantong FROM stok_darah WHERE golongan_id=%s", (gol,))
        cek = cur.fetchone()

        if not cek:
            messagebox.showerror("Error", "Golongan tidak tersedia!")
            return
        
        if cek[0] < jumlah:
            messagebox.showerror("Error", "Stok tidak mencukupi!")
            return

        # update stok
        cur.execute("UPDATE stok_darah SET jumlah_kantong = jumlah_kantong - %s WHERE golongan_id=%s", (jumlah, gol))
        db.commit()

        # simpan ke transaksi
        cur.execute("INSERT INTO transaksi_darah (stok_id, jenis_transaksi, jumlah, tanggal, petugas_id) VALUES (%s,'KELUAR',%s,NOW(),NULL)", (gol, jumlah))
        db.commit()
        
        messagebox.showinfo("Sukses", "Permintaan darah berhasil dikirim!")
        db.close()

    tk.Button(win, text="Kirim", command=kirim_permintaan).pack(pady=10)
    tk.Button(win, text="Kembali", command=lambda: menu_rs(win)).pack(pady=10)

    win.mainloop()
