from PyQt5.QtWidgets import *
from view_project import Ui_MainWindow
from project1_functions import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self):
        #circle
        if self.radioButton_circle.isChecked():
            radius = self.lineEdit_radius.text()
            radius_int = int(radius)
            area = radius_int * radius_int
            self.label_area_output.setText(f'The area of the circle is {area}')
            self.lineEdit_radius.setText('')

        #rectangle
        elif self.radioButton_rectangle.isChecked():
            lenght = self.lineEdit_lenght.text()
            width =  self.lineEdit_width.text()
            lenght_int = int(lenght)
            width_int = int(width)
            area = rectangle_area(lenght_int, width_int)
            self.label_area_output.setText(f'The area of the rectangle is {area}')
            self.lineEdit_lenght.setText('')
            self.lineEdit_width.setText('')

        #square
        elif self.radioButton_square.isChecked():
            side_lenght = self.lineEdit_side_lenght.text()
            side_lenght_int = int(side_lenght)
            area = square_area(side_lenght_int)
            self.label_area_output.setText(f'The area of the square is {area}')
            self.lineEdit_side_lenght.setText('')

        #triangle
        elif self.radioButton_triangle.isChecked():
            base = self.lineEdit_base.text()
            height = self.lineEdit_height.text()
            base_int = int(base)
            height_int = int(height)
            area = triangle_area(base_int, height_int)
            self.label_area_output.setText(f'The area of the triangle is {area}')
            self.lineEdit_height.setText('')
            self.lineEdit_base.setText('')









