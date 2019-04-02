import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class RectangleManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()     

        self.label1 = QtWidgets.QLabel("Enter two rectangle sides")
        self.label2 = QtWidgets.QLabel("Perimeter: ")
        self.label3 = QtWidgets.QLabel("Square: ")
        self.button = QtWidgets.QPushButton("Calculate")
        self.text1 = QtWidgets.QDoubleSpinBox ()  
        self.text1.setMaximum(1000000000)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)          
        
        self.text2 = QtWidgets.QDoubleSpinBox ()   
        self.text2.setMaximum(1000000000)        
        self.text2.setAlignment(QtCore.Qt.AlignCenter)            

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.mainLayout = QtWidgets.QVBoxLayout()
        
        self.horizontalLayout.addWidget(self.text1)        
        self.horizontalLayout.addWidget(self.text2)        
        
        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.label2)
        self.mainLayout.addWidget(self.label3)
        self.setLayout(self.mainLayout)

        self.button.clicked.connect(self.calculate)

    def calculate(self):      
            
        a = float(self.text1.value())
        b = float(self.text2.value())
        
        p = 2*(a+b)
        s = a * b
            
        self.label2.setText("Perimeter: " + '{0:0.2f}'.format(p))
        self.label3.setText("Square: " + '{0:0.2f}'.format(s))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = RectangleManager()
    widget.setWindowTitle('Square and perimeter of rectangle');
    widget.resize(400, 100)
    widget.show()

    sys.exit(app.exec_())