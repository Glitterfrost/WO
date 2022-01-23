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
        
        self.assertEqual(test_gui.get_display_value(),'')

    def test_default_numerical_system(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        self.assertEqual(test_gui.checkBox_DEC.isChecked(),True)

    
    def test_input_digits_decimal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_dec()
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
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_dec()
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
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_dec()
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
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_bin()
        self.assertEqual(test_gui.pushButton_0.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_1.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_2.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_3.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_4.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_5.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_6.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_7.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_8.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_9.isEnabled(), False)

    def test_input_letters_binary(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_bin()
        self.assertEqual(test_gui.pushButton_A.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_B.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_C.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_D.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_E.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_F.isEnabled(), False)


        
    def test_input_operations_binary(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_bin()
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

    def test_input_digits_octagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_oct()
        self.assertEqual(test_gui.pushButton_0.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_1.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_2.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_3.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_4.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_5.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_6.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_7.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_8.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_9.isEnabled(), False)
        
    def test_input_letters_octagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_oct()
        self.assertEqual(test_gui.pushButton_A.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_B.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_C.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_D.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_E.isEnabled(), False)
        self.assertEqual(test_gui.pushButton_F.isEnabled(), False)
        
    def test_input_operations_octagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_bin_dec_oct()
        test_gui.set_calc_digits_oct()
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

    def test_input_digits_hexagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_hex()
        test_gui.set_calc_digits_dec()
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
        
    def test_input_letters_hexagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_hex()
        test_gui.set_calc_digits_dec()
        self.assertEqual(test_gui.pushButton_A.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_B.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_C.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_D.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_E.isEnabled(), True)
        self.assertEqual(test_gui.pushButton_F.isEnabled(), True)

    def test_input_operations_hexagonal(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.set_calc_letters_hex()
        test_gui.set_calc_digits_dec()
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

    def test_input_0(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_0()
        self.assertEqual(test_gui.get_display_value()[-1],'0')

    def test_input_1(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_1()
        self.assertEqual(test_gui.get_display_value()[-1],'1')

    def test_input_2(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_2()
        self.assertEqual(test_gui.get_display_value()[-1],'2')

    def test_input_3(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_3()
        self.assertEqual(test_gui.get_display_value()[-1],'3')

    def test_input_4(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_4()
        self.assertEqual(test_gui.get_display_value()[-1],'4')

    def test_input_5(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_5()
        self.assertEqual(test_gui.get_display_value()[-1],'5')

    def test_input_6(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_6()
        self.assertEqual(test_gui.get_display_value()[-1],'6')

    def test_input_7(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_7()
        self.assertEqual(test_gui.get_display_value()[-1],'7')

    def test_input_8(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_8()
        self.assertEqual(test_gui.get_display_value()[-1],'8')

    def test_input_9(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_9()
        self.assertEqual(test_gui.get_display_value()[-1],'9')


    def test_input_Clear(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        test_gui.clicked_Clear()
        self.assertEqual(test_gui.get_display_value(),'')

    def test_input_Del(self):
        test_gui  = calc_gui.Ui_MainWindow()
        window = calc_gui.QtWidgets.QMainWindow()
        test_gui.setupUi(window)
        prev_string = test_gui.get_display_value()
        test_gui.clicked_Del()
        self.assertEqual(test_gui.get_display_value(),prev_string[:-1])






if __name__=='__main__':
    unittest.main()
    test_gui  = calc_gui.Ui_MainWindow()
    window = calc_gui.QtWidgets.QMainWindow()
    test_gui.setupUi(window)
    window.show()
