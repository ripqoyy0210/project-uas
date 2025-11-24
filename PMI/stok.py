import tkinter as tk
from tkinter import messagebox
from utils_file import koneksi
from menu_pmi import buka_menu_pmi

def refresh_list(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    db = koneksi()
    cur = db.cursor()
    cur.execute("""
        SELECT g.nama_golongan, s.jumlah_kantong 
        FROM stok_darah s
        JOIN golongan_darah g ON g.golongan_id = s.golongan_id
    """)
    data = cur.fetchall()
    db.close()

    for gol, jml in data:
        tk.Label(frame, text=f"{gol} : {jml} kantong", font=("Arial", 11)).pack(anchor="w")

def menu_stok(win):
    if win is not None:
        win.destroy()

    root = tk.Tk()
    root.title("Kelola Stok Darah")
    root.geometry("350x400")

    tk.Label(root, text="Stok Darah", font=("Arial", 14, "bold")).pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=5)

    refresh_list(frame)

    # Input Update
    tk.Label(root, text="\nUpdate Stok Darah").pack()

    tk.Label(root, text="Golongan (contoh: A+, O-, AB+)").pack()
    gol = tk.Entry(root)
    gol.pack()

    tk.Label(root, text="Jumlah (+/-)").pack()
    jml = tk.Entry(root)
    jml.pack()

    def update():
        g = gol.get().upper()
        try:
            angka = int(jml.get())
        except:
            messagebox.showerror("Error", "Jumlah harus angka")
            return

        db = koneksi()
        cur = db.cursor()

        # Cek golongan_id
        cur.execute("SELECT golongan_id FROM golongan_darah WHERE nama_golongan=%s", (g,))
        gol_id = cur.fetchone()

        if gol_id is None:
            messagebox.showerror("Error", "Golongan tidak ada di database!")
            db.close()
            return

        # Cek stok existing
        cur.execute("SELECT jumlah_kantong FROM stok_darah WHERE golongan_id=%s", (gol_id[0],))
        stok = cur.fetchone()

        if stok is None:
            messagebox.showerror("Error", "Stok untuk golongan ini belum dibuat!")
            db.close()
            return

        if stok[0] + angka < 0:
            messagebox.showerror("Error", "Stok tidak boleh minus!")
            db.close()
            return

        # Update stok
        cur.execute("""
            UPDATE stok_darah 
            SET jumlah_kantong = jumlah_kantong + %s, updated_at = NOW() 
            WHERE golongan_id = %s
        """, (angka, gol_id[0]))

        db.commit()
        db.close()

        messagebox.showinfo("Sukses", "Stok berhasil diperbarui!")
        refresh_list(frame)
        gol.delete(0, tk.END)
        jml.delete(0, tk.END)

    tk.Button(root, text="Simpan Perubahan", command=update).pack(pady=10)
    tk.Button(root, text="Kembali ke Menu PMI", command=lambda: buka_menu_pmi(root)).pack(pady=10)

    root.mainloop()
