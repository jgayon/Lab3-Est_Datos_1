# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbgame2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 948)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotonAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonAceptar.setGeometry(QtCore.QRect(460, 880, 141, 41))
        self.BotonAceptar.setObjectName("BotonAceptar")
        self.BotonStart = QtWidgets.QPushButton(self.centralwidget)
        self.BotonStart.setGeometry(QtCore.QRect(460, 680, 141, 41))
        self.BotonStart.setObjectName("BotonStart")
        self.spacbackground = QtWidgets.QLabel(self.centralwidget)
        self.spacbackground.setGeometry(QtCore.QRect(0, 0, 1081, 471))
        self.spacbackground.setText("")
        self.spacbackground.setPixmap(QtGui.QPixmap("img/space1.jpg"))
        self.spacbackground.setScaledContents(True)
        self.spacbackground.setObjectName("spacbackground")
        self.ShipIcon = QtWidgets.QLabel(self.centralwidget)
        self.ShipIcon.setGeometry(QtCore.QRect(30, 300, 191, 91))
        self.ShipIcon.setText("")
        self.ShipIcon.setPixmap(QtGui.QPixmap("img/SpShip.png"))
        self.ShipIcon.setScaledContents(True)
        self.ShipIcon.setObjectName("ShipIcon")
        self.EnemyShip = QtWidgets.QLabel(self.centralwidget)
        self.EnemyShip.setGeometry(QtCore.QRect(810, 280, 211, 131))
        self.EnemyShip.setText("")
        self.EnemyShip.setPixmap(QtGui.QPixmap("img/enemy.png"))
        self.EnemyShip.setScaledContents(True)
        self.EnemyShip.setObjectName("EnemyShip")
        self.hearts = QtWidgets.QLabel(self.centralwidget)
        self.hearts.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.hearts.setText("")
        self.hearts.setPixmap(QtGui.QPixmap("img/Heart.png"))
        self.hearts.setScaledContents(True)
        self.hearts.setObjectName("hearts")
        self.liveslabel = QtWidgets.QLabel(self.centralwidget)
        self.liveslabel.setGeometry(QtCore.QRect(80, 20, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.liveslabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.liveslabel.setFont(font)
        self.liveslabel.setScaledContents(False)
        self.liveslabel.setObjectName("liveslabel")
        self.backgroundpregunta = QtWidgets.QLabel(self.centralwidget)
        self.backgroundpregunta.setGeometry(QtCore.QRect(0, 420, 1081, 141))
        self.backgroundpregunta.setText("")
        self.backgroundpregunta.setPixmap(QtGui.QPixmap("img/metalscreen.png"))
        self.backgroundpregunta.setScaledContents(True)
        self.backgroundpregunta.setObjectName("backgroundpregunta")
        self.labelpregunta = QtWidgets.QLabel(self.centralwidget)
        self.labelpregunta.setGeometry(QtCore.QRect(60, 450, 961, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.labelpregunta.setPalette(palette)
        self.labelpregunta.setText("")
        self.labelpregunta.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpregunta.setObjectName("labelpregunta")
        self.RB1 = QtWidgets.QRadioButton(self.centralwidget)
        self.RB1.setGeometry(QtCore.QRect(10, 570, 1061, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RB1.setPalette(palette)
        self.RB1.setObjectName("RB1")
        self.RB2 = QtWidgets.QRadioButton(self.centralwidget)
        self.RB2.setGeometry(QtCore.QRect(10, 650, 1071, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RB2.setPalette(palette)
        self.RB2.setObjectName("RB2")
        self.RB3 = QtWidgets.QRadioButton(self.centralwidget)
        self.RB3.setGeometry(QtCore.QRect(10, 740, 1061, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RB3.setPalette(palette)
        self.RB3.setObjectName("RB3")
        self.RB4 = QtWidgets.QRadioButton(self.centralwidget)
        self.RB4.setGeometry(QtCore.QRect(10, 800, 1061, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RB4.setPalette(palette)
        self.RB4.setObjectName("RB4")
        self.spacbackground.raise_()
        self.ShipIcon.raise_()
        self.EnemyShip.raise_()
        self.hearts.raise_()
        self.liveslabel.raise_()
        self.backgroundpregunta.raise_()
        self.labelpregunta.raise_()
        self.RB3.raise_()
        self.RB4.raise_()
        self.RB2.raise_()
        self.BotonAceptar.raise_()
        self.BotonStart.raise_()
        self.RB1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.BotonAceptar.hide()
        self.RB1.hide()
        self.RB2.hide()
        self.RB3.hide()
        self.RB4.hide()
        self.retranslateUi(MainWindow)
        ui.reset_question()
        self.BotonAceptar.clicked.connect(self.submit_answer)
        self.BotonStart.clicked.connect(self.start)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BotonAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.BotonStart.setText(_translate("MainWindow","Start"))
        self.liveslabel.setText(_translate("MainWindow", "X3"))
        self.RB1.setText(_translate("MainWindow", "A"))
        self.RB2.setText(_translate("MainWindow", "B"))
        self.RB3.setText(_translate("MainWindow", "C"))
        self.RB4.setText(_translate("MainWindow", "D"))
    
    def start(self):
        self.BotonAceptar.show()
        self.RB1.show()
        self.RB2.show()
        self.RB3.show()
        self.RB4.show()
        self.BotonStart.hide()
        self.play()
    def reset_question(self):
        self.RB1.setChecked(False)
        self.RB1.setEnabled(True)
        self.RB2.setChecked(False)
        self.RB2.setEnabled(True)
        self.RB3.setChecked(False)
        self.RB3.setEnabled(True)
        self.RB4.setChecked(False)
        self.RB4.setEnabled(True)

    def submit_answer(self):
        if self.RB1.isChecked():
            answer = "a"
            print("a")
            return answer
        if self.RB2.isChecked():
            answer = "b"
            print("b")
            return answer
        if self.RB3.isChecked():
            answer = "c"
            print("c")
            return answer
        if self.RB4.isChecked():
            answer = "d"
            print("d")
            return answer

    def play(self):
        import numpy as np
        import pandas as pd
        
        archivopreg = 'QyA.xlsx'
        preguntas = pd.read_excel(archivopreg)
        lives = 3
        livestr = str(lives)
        score = 0
        used = []
        self.liveslabel.setText(livestr)
        self.reset_question()
        tam = len(preguntas)
        while lives > 0:
            num = np.random.randint(0,tam)
            
            self.reset_question()
            if (num not in used):
                preg= preguntas['Pregunta'][num]
                self.labelpregunta.setText(preg)
                respa=preguntas['A'][num]
                self.RB1.setText(respa)
                respb=preguntas['B'][num]
                self.RB2.setText(respb)
                respc=preguntas['C'][num]
                self.RB3.setText(respc)
                respd=preguntas['D'][num]
                self.RB4.setText(respd)
                respcorrect= preguntas['Correcta'][num]
                used.append(num)
                print(used)
                answered = False
                while answered == False:
                    if self.BotonAceptar.clicked:
                        answer = self.submit_answer()
                        print(answer)
                        if answer == respcorrect.lower():
                            score += 100
                        else:
                            lives = lives - 1
                            livestr = str(lives)
                            self.liveslabel.setText(livestr)
                        print(score)
                        print("Lives: ",lives)
                        answered = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
