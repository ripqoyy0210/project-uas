import tkinter as tk
from tkinter import messagebox
from utils_file import koneksi
from menu_pmi import buka_menu_pmi

def menu_transaksi(win):
    if win is not None:
        win.destroy()

    root = tk.Tk()
    root.title("Transaksi Darah PMI")
    root.geometry("360x340")

    tk.Label(root, text="Transaksi PMI ke Rumah Sakit", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(root, text="Golongan Darah (A+, O-, AB+)").pack()
    gol = tk.Entry(root)
    gol.pack()

    tk.Label(root, text="Jumlah Kantong").pack()
    jumlah = tk.Entry(root)
    jumlah.pack()

    def kirim():
        g = gol.get().upper()
        try:
            j = int(jumlah.get())
        except:
            messagebox.showerror("Error", "Jumlah harus angka!")
            return

        db = koneksi()
        cur = db.cursor()

        # Ambil golongan_id
        cur.execute("SELECT golongan_id FROM golongan_darah WHERE nama_golongan=%s", (g,))
        gol_id = cur.fetchone()

        if gol_id is None:
            messagebox.showerror("Error", "Golongan darah tidak terdaftar!")
            db.close()
            return

        # Ambil stok_id dan stok saat ini
        cur.execute("SELECT stok_id, jumlah_kantong FROM stok_darah WHERE golongan_id=%s", (gol_id[0],))
        stok = cur.fetchone()

        if stok is None:
            messagebox.showerror("Error", "Data stok tidak ditemukan!")
            db.close()
            return

        stok_id, jumlah_stok = stok

        if jumlah_stok < j:
            messagebox.showerror("Error", "Stok darah tidak mencukupi!")
            db.close()
            return

        # Kurangi stok
        cur.execute("""
            UPDATE stok_darah 
            SET jumlah_kantong = jumlah_kantong - %s, updated_at = NOW()
            WHERE stok_id = %s
        """, (j, stok_id))

        # Masukkan ke tabel transaksi_darah
        cur.execute("""
            INSERT INTO transaksi_darah (stok_id, jenis_transaksi, jumlah, tanggal)
            VALUES (%s, 'keluar', %s, CURDATE())
        """, (stok_id, j))

        db.commit()
        db.close()

        messagebox.showinfo("Sukses", "Transaksi berhasil dicatat!")
        gol.delete(0, tk.END)
        jumlah.delete(0, tk.END)

    tk.Button(root, text="Kirim", command=kirim).pack(pady=10)
    tk.Button(root, text="Kembali ke Menu PMI", command=lambda: buka_menu_pmi(root)).pack()

    root.mainloop()
