# -*- coding: utf-8 -*-



# Created by: PyQt5 UI code generator 5.13.2
#



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pytube

___autore___ == ("AbdelmounaimOmri aka tpx1scS")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 479)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CampoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoInput.setGeometry(QtCore.QRect(60, 130, 421, 91))
        self.CampoInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CampoInput.setObjectName("CampoInput")

        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(120, 230, 291, 71))
        self.DownloadButton.setObjectName("DownloadButton")

        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(60, 12, 421, 111))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Logo-Resized.bmp"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionInformazione = QtWidgets.QAction(MainWindow)
        self.actionInformazione.setObjectName("actionInformazione")

        self.actionVersione = QtWidgets.QAction(MainWindow)
        self.actionVersione.setObjectName("actionVersione")

        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")

        self.menu.addAction(self.actionInformazione)
        self.menu.addSeparator()
        self.menu.addAction(self.actionVersione)
        self.menu.addAction(self.actionEsci)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.DownloadButton.clicked.connect(self.retrieve_link)
        self.actionInformazione.triggered.connect(self.show_Info)

    def show_Info(self):
        msg1 = QMessageBox()
        msg1.setWindowTitle("Informazioni")
        msg1.setText("YTDownlader, creato da AbdelmounaimOmri aka tpx1sc, permette di scaricare la maggiorparte dei video YouTube inserendo l'url nel campo input.")
        msg1.setIcon(QMessageBox.Information)
        info = msg1.exec_()

    def show_Versione():
        msg2 = QMessageBox()
        msg2.setWindowTitle('Versione')
        msg2.setText("YTDownlader 1.0")
        msg2.setIcon(QMessageBox.Information)
        Info = msg1.exec_()

    def retrieve_link(self):
        msg = QMessageBox()
        msg.setWindowTitle("Scaricamento In corso...")
        msg.setText("Il video sta venendo scaricato, attendere...")
        msg.setIcon(QMessageBox.Information)
        y = msg.exec_()
        try:
            self.url = self.CampoInput.text()
            self.yt = pytube.YouTube(self.url)
            self.yt.streams.first().download("../../../Video Scaricati")

            msg = QMessageBox()
            msg.setWindowTitle("Scaricamento Completo")
            msg.setText("Il video é stato scaricato nella cartella 'Video scaricati' nel Desktop")
            msg.setIcon(QMessageBox.Information)
            #msg.setDetailedText(str(e))
            y = msg.exec_()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Scaricamento Fallito")
            msg.setText("Riscontrato un errore durante lo scaricamento del video, riprovare")
            msg.setIcon(QMessageBox.Critical)
            y = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CampoInput.setText(_translate("MainWindow", "Link del video YouTube:"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionInformazione.setText(_translate("MainWindow", "Informazioni"))
        self.actionVersione.setText(_translate("MainWindow", "Versione"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
