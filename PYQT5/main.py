from PyQt5 import QtWidgets
from login import Ui_MainWindow   # <--- Tambahkan ini
import sys
import mysql.connector
from PyQt5.QtWidgets import QMessageBox

# Import UI untuk setiap role dari subfolder
from petugas_pmi.petugas_pmi import Ui_MainWindow as Ui_MenuPetugas
from pendonor.pendonor import Ui_MainWindow as Ui_Pendonor
from petugas_rs.petugas_rs import Ui_MainWindow as Ui_PetugasRS

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 🔐 Password mode 
        self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)

        # Event Button
        self.ui.pushButton_login.clicked.connect(self.login_action)
        self.ui.pushButton_signup.clicked.connect(self.signup_action)

    def login_action(self):
        username = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_pass.text()

        if username == "" or password == "":
            QMessageBox.warning(self, "Error", "Username dan Password tidak boleh kosong!")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas_pmi"
            )
            cursor = db.cursor()

            query = """
                SELECT user.*, role.nama_role 
                FROM user 
                INNER JOIN role ON user.id_role = role.id_role 
                WHERE username=%s AND password=%s
            """
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                role = result[4]
                QMessageBox.information(self, "Login Berhasil", f"Selamat datang {username}!")
                self.open_menu_by_role(role)
                self.close()
            else:
                QMessageBox.warning(self, "Login Gagal", "Username atau Password salah!")

            cursor.close()
            db.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def open_menu_by_role(self, role):
        if role == "Petugas PMI":
            self.menu_petugas = MenuPetugasWindow()
            self.menu_petugas.show()
        elif role == "Pendonor":
            self.pendonor = PendonorWindow()
            self.pendonor.show()
        elif role == "Petugas RS":
            self.petugas_rs = PetugasRSWindow()
            self.petugas_rs.show()
        else:
            QMessageBox.warning(self, "Error", "Role tidak dikenali!")

    def signup_action(self):
        QMessageBox.information(self, "Sign Up", "Tombol Sign Up ditekan.")


class MenuPetugasWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuPetugasWindow, self).__init__()
        self.ui = Ui_MenuPetugas()
        self.ui.setupUi(self)


class PendonorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PendonorWindow, self).__init__()
        self.ui = Ui_Pendonor()
        self.ui.setupUi(self)


class PetugasRSWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PetugasRSWindow, self).__init__()
        self.ui = Ui_PetugasRS()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
