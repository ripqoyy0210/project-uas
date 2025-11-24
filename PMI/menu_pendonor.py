import tkinter as tk
from tkinter import messagebox
from utils_file import kembali

# Jadwal Donor Contoh
jadwal_donor = [
    "Senin - PMI Kota",
    "Rabu - RS Umum",
    "Jumat - Kampus X"
]

# Database pendaftaran sementara
data_pendaftaran = []

def menu_pendonor(parent=None):
    if parent:
        parent.destroy()

    win = tk.Tk()
    win.title("Menu Pendonor")
    win.geometry("350x300")

    tk.Label(win, text="Jadwal Donor", font=("Arial", 14)).pack(pady=10)

    # List Jadwal
    for j in jadwal_donor:
        tk.Label(win, text=j).pack()

    tk.Label(win, text="\nDaftar Donor").pack()

    nama = tk.Entry(win)
    nama.insert(0, "Masukkan Nama")
    nama.pack()

    def daftar():
        if nama.get() == "" or nama.get() == "Masukkan Nama":
            messagebox.showerror("Error", "Nama harus diisi!")
            return
        data_pendaftaran.append(nama.get())
        messagebox.showinfo("Sukses", "Pendaftaran berhasil!")
        nama.delete(0, tk.END)

    tk.Button(win, text="Daftar", command=daftar).pack(pady=10)

    tk.Button(win, text="Kembali", command=lambda: kembali(win)).pack(pady=10)
def menu_pendonor():
    win = tk.Tk()
    win.title("Menu Pendonor")
    tk.Label(win, text="Pendonor bisa melihat jadwal & daftar donor").pack(pady=20)
    tk.Button(win, text="Kembali ke Login", command=lambda: kembali(win)).pack(pady=10)
 
    win.mainloop()