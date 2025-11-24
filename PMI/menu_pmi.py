import tkinter as tk
from utils_file import kembali
from transaksi import menu_transaksi
from stok import menu_stok

def buka_menu_pmi(win=None):
    if win is not None:
        win.destroy()

    root = tk.Tk()
    root.title("Menu Utama PMI")
    root.geometry("300x250")

    tk.Label(root, text="MENU PMI", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Kelola Stok Darah", width=25, command=lambda: menu_stok(root)).pack(pady=5)
    tk.Button(root, text="Transaksi Darah", width=25, command=lambda: menu_transaksi(root)).pack(pady=5)

    # Kembali ke login (main.py)
    from main import login_page
    tk.Button(root, text="Logout",
          command=lambda: kembali(root, login_page)).pack(pady=20)

    root.mainloop()
