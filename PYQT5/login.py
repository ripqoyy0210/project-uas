# ===================== LOGIN WINDOW AUTO FROM UI =====================

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ==================== L A Y O U T   W I D G E T ====================
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(275, 90, 250, 350))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")

        # ==================== T I T L E ====================
        self.label_title = QtWidgets.QLabel(self.layoutWidget)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)

        # ==================== S U B  T I T L E ====================
        self.label_subtitle = QtWidgets.QLabel(self.layoutWidget)
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout.addWidget(self.label_subtitle)

        # ==================== U S E R N A M E ====================
        self.lineEdit_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_user.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout.addWidget(self.lineEdit_user)

        # ==================== P A S S W O R D ====================
        self.lineEdit_pass = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_pass.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.verticalLayout.addWidget(self.lineEdit_pass)

        # ==================== B U T T O N   L O G I N ====================
        self.pushButton_login = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_login.setMinimumSize(QtCore.QSize(200, 32))
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)

        # ==================== B U T T O N   S I G N U P ====================
        self.pushButton_signup = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_signup.setMinimumSize(QtCore.QSize(200, 32))
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.verticalLayout.addWidget(self.pushButton_signup)

        # ==================== M A I N   W I N D O W ====================
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ======== TEXT UI =========
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # ==================== TEXT FOR UI ====================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_title.setText(_translate("MainWindow", "<html><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">MENU PMI</span></p></body></html>"))
        self.label_subtitle.setText(_translate("MainWindow", "<html><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">LOGIN</span></p></body></html>"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_signup.setText(_translate("MainWindow", "SIGN UP"))
