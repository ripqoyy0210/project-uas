from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter.ttk import Combobox  # <-- Tambahan

# =================== KONEKSI DATABASE ===================
def koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uas_pmi"
    )

# =================== SIGN UP / REGISTER ===================
def signup_page():
    reg = tk.Tk()
    reg.title("Registrasi Akun")
    reg.geometry("350x400")

    tk.Label(reg, text="REGISTRASI AKUN", font=("Arial", 16)).pack(pady=15)

    tk.Label(reg, text="Nama Lengkap").pack()
    nama = tk.Entry(reg)
    nama.pack()

    tk.Label(reg, text="Username").pack()
    user = tk.Entry(reg)
    user.pack()

    tk.Label(reg, text="Password").pack()
    pw = tk.Entry(reg, show="*")
    pw.pack()

    tk.Label(reg, text="Role").pack()

    role = Combobox(reg, values=["pmi", "pendonor", "rs"], state="readonly")  # <-- COMBOBOX
    role.pack()
    role.set("pilih role")  # placeholder

    tk.Label(reg, text="Alamat").pack()
    alamat = tk.Entry(reg)
    alamat.pack()

    def daftar():
        n = nama.get()
        u = user.get()
        p = pw.get()
        r = role.get().lower()
        a = alamat.get()

        if r not in ["pmi", "pendonor", "rs"]:
            messagebox.showerror("Error", "Silahkan pilih role yang valid!")
            return

        if n == "" or u == "" or p == "" or a == "":
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        db = koneksi()
        cur = db.cursor()
        cur.execute("SELECT * FROM user WHERE username=%s", (u,))
        cek = cur.fetchone()

        if cek:
            messagebox.showerror("Error", "Username sudah digunakan!")
            db.close()
            return

        cur.execute("INSERT INTO user (nama_lengkap, username, password, role, alamat) VALUES (%s,%s,%s,%s,%s)",
                    (n, u, p, r, a))
        db.commit()
        db.close()

        messagebox.showinfo("Sukses", "Registrasi Berhasil! Silahkan Login.")
        reg.destroy()
        login_page()

    tk.Button(reg, text="Daftar", width=20, command=daftar).pack(pady=20)
    tk.Button(reg, text="Kembali", width=20, command=lambda: [reg.destroy(), login_page()]).pack()

    reg.mainloop()

# =================== LOGIN PAGE ===================
def login_page():
    win = tk.Tk()
    win.title("Halaman Login")
    win.geometry("350x320")

    tk.Label(win, text="LOGIN SISTEM PMI", font=("Arial", 16)).pack(pady=15)

    tk.Label(win, text="Username").pack()
    username = tk.Entry(win)
    username.pack()

    tk.Label(win, text="Password").pack()
    password = tk.Entry(win, show="*")
    password.pack()

    tk.Label(win, text="Role/User").pack()

    role = Combobox(win, values=["pmi", "pendonor", "rs"], state="readonly")  # <-- COMBOBOX
    role.pack()
    role.set("pilih role")

    def cek_login():
        user = username.get()
        pw = password.get()
        r = role.get().lower()

        db = koneksi()
        cur = db.cursor()
        cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND role=%s", (user, pw, r))
        data = cur.fetchone()
        db.close()

        if data:
            messagebox.showinfo("Sukses", f"Login Berhasil sebagai {r.upper()}!")
            win.destroy()

            if r == "pmi":
                from menu_pmi import buka_menu_pmi
                buka_menu_pmi(None)

            elif r == "pendonor":
                from menu_pendonor import menu_pendonor
                menu_pendonor(None)

            elif r == "rs":
                from menu_rs import menu_rs
                menu_rs(None)

        else:
            messagebox.showerror("Gagal", "Login salah, coba ulang!")

    tk.Button(win, text="Login", width=20, command=cek_login).pack(pady=10)
    tk.Button(win, text="Belum Punya Akun? Sign Up", width=25, command=lambda: [win.destroy(), signup_page()]).pack()

    win.mainloop()

# =================== START APP ===================
if __name__ == "__main__":
    login_page()
