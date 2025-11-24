# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # === STYLE ===
        MainWindow.setStyleSheet("""
        QMainWindow {
            background-color: #f1f1f1;
            font-family: "Segoe UI";
        }

        QWidget#panel {
            background-color: white;
            border-radius: 15px;
            border: 1px solid #d0d0d0;
        }

        QLabel {
            font-weight: 600;
        }

        QPushButton {
            background-color: #c00000;
            color: white;
            border-radius: 10px;
            font-weight: 600;
            height: 32px;
        }
        QPushButton:hover {
            background-color: #a00000;
        }

        QLineEdit {
            border: 1px solid #c0c0c0;
            border-radius: 8px;
            padding: 4px;
            font-size: 10pt;
        }
        """)

        # === CENTRAL WIDGET ===
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## --- TITLE ---
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 20, 180, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14pt; color: #c00000; font-weight: 700;")

        ## --- TABLE PANEL ---
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 80, 301, 255))
        self.groupBox.setObjectName("panel")

        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(5, 22, 291, 225))

        ## --- REFRESH BUTTON ---
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 350, 121, 32))

        ## --- LABEL PERMINTAAN (CENTER) ---
        self.label_req = QtWidgets.QLabel(self.centralwidget)
        self.label_req.setGeometry(QtCore.QRect(325, 390, 200, 25))
        self.label_req.setAlignment(QtCore.Qt.AlignCenter)   # <-- dibikin center

        ## --- INPUT GOLONGAN ---
        self.lineEditGol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGol.setGeometry(QtCore.QRect(300, 420, 260, 30))
        self.lineEditGol.setPlaceholderText("Masukkan Golongan Darah...")

        ## --- INPUT JUMLAH ---
        self.lineEditJumlah = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditJumlah.setGeometry(QtCore.QRect(300, 455, 260, 30))
        self.lineEditJumlah.setPlaceholderText("Masukkan Jumlah Permintaan...")

        ## --- BUTTON MINTA STOK ---
        self.pushButton_req = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_req.setGeometry(QtCore.QRect(360, 495, 121, 32))

        MainWindow.setCentralWidget(self.centralwidget)

        # === MENUBAR DAN STATUS ===
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # === TEXT SECTION ===
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stok Darah Rumah Sakit"))
        self.label.setText(_translate("MainWindow", "PETUGAS RS"))
        self.groupBox.setTitle(_translate("MainWindow", "Stok Darah Yang Tersedia"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.label_req.setText(_translate("MainWindow", "Permintaan Stok Darah"))
        self.pushButton_req.setText(_translate("MainWindow", "Minta Stok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
