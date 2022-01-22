from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 440, 51, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 440, 51, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 440, 51, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 380, 51, 51))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 380, 51, 51))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 380, 51, 51))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 320, 51, 51))
        self.pushButton_7.setObjectName("pushButton_9")
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 320, 51, 51))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 320, 51, 51))
        self.pushButton_9.setObjectName("pushButton_10")

        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setGeometry(QtCore.QRect(270, 440, 51, 51))
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.pushButton_Substract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Substract.setGeometry(QtCore.QRect(270, 380, 51, 51))
        self.pushButton_Substract.setObjectName("pushButton_Substract")

        self.pushButton_Mulitply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mulitply.setGeometry(QtCore.QRect(270, 320, 51, 51))
        self.pushButton_Mulitply.setObjectName("pushButton_Mulitply")

        self.pushButton_Divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Divide.setGeometry(QtCore.QRect(270, 260, 51, 51))
        self.pushButton_Divide.setObjectName("pushButton_Divide")

        self.pushButton_perCent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_perCent.setGeometry(QtCore.QRect(210, 260, 51, 51))
        self.pushButton_perCent.setObjectName("pushButton_perCent")

        self.pushButton_rightBracket = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rightBracket.setGeometry(QtCore.QRect(150, 260, 51, 51))
        self.pushButton_rightBracket.setObjectName("pushButton_rightBracket")

        self.pushButton_leftBracket = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_leftBracket.setGeometry(QtCore.QRect(90, 260, 51, 51))
        self.pushButton_leftBracket.setObjectName("pushButton_leftBracket")

        self.pushButton_leftShift = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_leftShift.setGeometry(QtCore.QRect(90, 200, 51, 51))
        self.pushButton_leftShift.setObjectName("pushButton_leftShift")

        self.pushButton_rightShift = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rightShift.setGeometry(QtCore.QRect(150, 200, 51, 51))
        self.pushButton_rightShift.setObjectName("pushButton_rightShift")

        self.pushButton_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(210, 200, 51, 51))
        self.pushButton_Clear.setObjectName("pushButton_Clear")

        self.pushButton_Del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Del.setGeometry(QtCore.QRect(270, 200, 51, 51))
        self.pushButton_Del.setObjectName("pushButton_Del")

        self.pushButton_A = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_A.setGeometry(QtCore.QRect(30, 200, 51, 51))
        self.pushButton_A.setObjectName("pushButton_A")
        
        self.pushButton_B = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_B.setGeometry(QtCore.QRect(30, 260, 51, 51))
        self.pushButton_B.setObjectName("pushButton_B")

        self.pushButton_C = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_C.setGeometry(QtCore.QRect(30, 320, 51, 51))
        self.pushButton_C.setObjectName("pushButton_C")

        self.pushButton_D = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D.setGeometry(QtCore.QRect(30, 380, 51, 51))
        self.pushButton_D.setObjectName("pushButton_D")

        self.pushButton_E = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_E.setGeometry(QtCore.QRect(30, 440, 51, 51))
        self.pushButton_E.setObjectName("pushButton_E")

        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(270, 500, 51, 51))
        self.pushButton_equal.setObjectName("pushButton_equal")

        self.pushButton_comma = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_comma.setGeometry(QtCore.QRect(210, 500, 51, 51))
        self.pushButton_comma.setObjectName("pushButton_comma")

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(150, 500, 51, 51))
        self.pushButton_0.setObjectName("pushButton_0")

        self.pushButton_sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sign.setGeometry(QtCore.QRect(90, 500, 51, 51))
        self.pushButton_sign.setObjectName("pushButton_sign")

        self.pushButton_F = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_F.setGeometry(QtCore.QRect(30, 500, 51, 51))
        self.pushButton_F.setObjectName("pushButton_F")
        
        self.checkBox_BIN = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_BIN.setGeometry(QtCore.QRect(10, 170, 70, 17))
        self.checkBox_BIN.setObjectName("checkBox_BIN")
        #self.checkBox_BIN.stateChanged.connect(self.uncheck)

        self.checkBox_OCT = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_OCT.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.checkBox_OCT.setObjectName("checkBox_OCT")
        #self.checkBox_OCT.stateChanged.connect(self.uncheck)

        self.checkBox_DEC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_DEC.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.checkBox_DEC.setObjectName("checkBox_DEC")
        self.checkBox_DEC.setChecked(True)
        #self.checkBox_DEC.stateChanged.connect(self.uncheck)

        self.checkBox_HEX = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_HEX.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_HEX.setObjectName("checkBox_HEX")
        #self.checkBox_HEX.stateChanged.connect(self.uncheck)

        self.Display = QtWidgets.QLabel(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(80, 30, 241, 91))
        self.Display.setObjectName("Display")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.set_calc_for_dec()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def set_calc_for_dec(self):
        self.pushButton_A.setEnabled(False)
        self.pushButton_B.setEnabled(False)
        self.pushButton_C.setEnabled(False)
        self.pushButton_D.setEnabled(False)
        self.pushButton_E.setEnabled(False)
        self.pushButton_F.setEnabled(False)

    
    


    # def uncheck(self, state):
  
    #     # checking if state is checked
    #     if state == Qt.Checked:
  
    #         # if first check box is selected
    #         if self.sender() == self.self.checkBox_BIN:
  
    #             # making other check box to uncheck
    #             self.checkBox_OCT.setChecked(False)
    #             self.checkBox_DEC.setChecked(False)
    #             self.checkBox_HEX.setChecked(True)
  
    #         # if second check box is selected
    #         elif self.sender() == self.checkBox_DEC:
  
    #             # making other check box to uncheck
    #             self.checkBox_OCT.setChecked(False)
    #             self.checkBox_BIN.setChecked(False)
    #             self.checkBox_HEX.setChecked(True)
  
  
    #         # if third check box is selected
    #         elif self.sender() == self.checkBox_OCT:
  
    #             # making other check box to uncheck
    #             self.checkBox_DEC.setChecked(False)
    #             self.checkBox_BIN.setChecked(False)
    #             self.checkBox_HEX.setChecked(True)
    #         elif self.sender() == self.checkBox_HEX:
  
    #             # making other check box to uncheck
    #             self.checkBox_DEC.setChecked(False)
    #             self.checkBox_BIN.setChecked(False)
    #             self.checkBox_OCT.setChecked(True)



    def retranslateUi(self,MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))

        self.pushButton_2.setText(_translate("MainWindow", "2"))

        self.pushButton_3.setText(_translate("MainWindow", "3"))

        self.pushButton_4.setText(_translate("MainWindow", "4"))

        self.pushButton_5.setText(_translate("MainWindow", "5"))

        self.pushButton_6.setText(_translate("MainWindow", "6"))

        self.pushButton_9.setText(_translate("MainWindow", "9"))

        self.pushButton_8.setText(_translate("MainWindow", "8"))

        self.pushButton_7.setText(_translate("MainWindow", "7"))

        self.pushButton_Add.setText(_translate("MainWindow", "+"))

        self.pushButton_Substract.setText(_translate("MainWindow", "-"))

        self.pushButton_Mulitply.setText(_translate("MainWindow", "X"))

        self.pushButton_Divide.setText(_translate("MainWindow", "/"))

        self.pushButton_perCent.setText(_translate("MainWindow", "%"))

        self.pushButton_rightBracket.setText(_translate("MainWindow", ")"))

        self.pushButton_leftBracket.setText(_translate("MainWindow", "("))

        self.pushButton_leftShift.setText(_translate("MainWindow", "<<"))

        self.pushButton_rightShift.setText(_translate("MainWindow", ">>"))

        self.pushButton_Clear.setText(_translate("MainWindow", "C"))

        self.pushButton_Del.setText(_translate("MainWindow", "del"))

        self.pushButton_A.setText(_translate("MainWindow", "A"))

        self.pushButton_B.setText(_translate("MainWindow", "B"))

        self.pushButton_C.setText(_translate("MainWindow", "C"))

        self.pushButton_D.setText(_translate("MainWindow", "D"))

        self.pushButton_E.setText(_translate("MainWindow", "E"))

        self.pushButton_equal.setText(_translate("MainWindow", "="))

        self.pushButton_comma.setText(_translate("MainWindow", ","))

        self.pushButton_0.setText(_translate("MainWindow", "0"))

        self.pushButton_sign.setText(_translate("MainWindow", "sign"))

        self.pushButton_F.setText(_translate("MainWindow", "F"))

        self.checkBox_BIN.setText(_translate("MainWindow", "BIN"))

        self.checkBox_OCT.setText(_translate("MainWindow", "OCT"))

        self.checkBox_DEC.setText(_translate("MainWindow", "DEC"))

        self.checkBox_HEX.setText(_translate("MainWindow", "HEX"))

        self.Display.setText(_translate("MainWindow", "0"))

                # first decorate the getter method
    def get_display_value(self): # This getter method name is *the* name
        return self.Display.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    
    window = QtWidgets.QMainWindow()
    ex.setupUi(window)
    window.show()
    sys.exit(app.exec_())