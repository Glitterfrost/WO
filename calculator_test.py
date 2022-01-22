import unittest
import calc_gui
#Testy inicjalizacji klasy


app = calc_gui.QApplication(calc_gui.sys.argv)

class TestCalculator(unittest.TestCase):
    #Testy inicjalizacji klasy
    def test_create_calculator_object(self):
        self.assertEqual(isinstance(calc_gui.Ui_MainWindow(),calc_gui.Ui_MainWindow),True)

    def test_default_display_value(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        
        self.assertEqual(test_gui.get_display_value(),'0')

    def test_default_numerical_system(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        self.assertEqual(test_gui.checkBox_DEC.isChecked(),True)

    # def test_default_data_type(self):
    #     self.assertEqual(Calculator().get_data_type,'qword')
    #Testy wprowadzania znakow w systemie dziesiętny
    def test_input_digits_decimal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        self.assertEqual(test_gui.pushButton_0.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_1.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_2.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_3.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_4.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_5.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_6.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_7.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_8.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_9.isEnabled(), True)

    def test_input_letters_decimal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        self.assertEqual(test_gui.pushButton_A.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_B.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_C.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_D.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_E.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_F.isEnabled(), False)

    def test_input_operations_decimal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
       
        self.assertEqual(test_gui.pushButton_Add.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_Substract.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_Mulitply.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_Divide.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_perCent.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_rightBracket.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_leftBracket.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_leftShift.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_rightShift.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_Clear.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_Del.isEnabled(), True)


    #Testy wprowadzania znakow w systemie binarnym
    def test_input_digits_binary(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_system('BIN')
        self.assertEqual(calc.get_available_digits(), [0,1])

    def test_input_operations_binary(self):
        calc = Calculator()
        calc.set_current_system('bin')
        self.assertEqual(calc.get_available_operations(), ['+','-','*','/','(',')','<<','>>','%'])





    # #Testy wprowadzania znakow w systemie ósemkowym
    # def test_input_digits_octagonal(self):
    #     calc = Calculator()
    #     calc.set_current_system('oct')
    #     self.assertEqual(calc.get_available_digits(), [0,1,2,3,4,5,6,7])

    # def test_input_operations_octagonal(self):
    #     calc = Calculator()
    #     calc.set_current_system('oct')
    #     self.assertEqual(calc.get_available_operations(), ['+','-','*','/','(',')','<<','>>','%'])





    # #Testy wprowadzania znakow w systemie dziesiętny
    # def test_input_digits_decimal(self):
    #     calc = Calculator()
    #     calc.set_current_system('dec')
    #     self.assertEqual(calc.get_available_digits(), [0,1,2,3,4,5,6,7,8,9])

    # def test_input_operations_decimal(self):
    #     calc = Calculator()
    #     calc.set_current_system('dec')
    #     self.assertEqual(calc.get_available_operations(), ['+','-','*','/','(',')','<<','>>','%'])






    # #Testy wprowadzania znakow w systemie szesnastkowym
    # def test_input_digits_hexagonal(self):
    #     calc = Calculator()
    #     calc.set_current_system('hex')
    #     self.assertEqual(calc.get_available_digits(), [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'])

    # def test_input_operations_hexagonal(self):
    #     calc = Calculator()
    #     calc.set_current_system('hex')
    #     self.assertEqual(calc.get_available_operations(), ['+','-','*','/','(',')','<<','>>','%'])
  

    
    # def test_conversion_decimal_binary(self):
    #     calc = Calculator()
    #     self.assertEqual(calc.convert('dec','bin',1874), '11100110111')
        

 
    




    






if __name__=='__main__':
    unittest.main()
    test_gui  = calc_gui.Ui_MainWindow()
    window = calc_gui.QtWidgets.QMainWindow()
    test_gui.setupUi(window)
    window.show()
