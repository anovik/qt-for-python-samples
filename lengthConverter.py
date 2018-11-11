import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class LengthConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()                
      

        self.button = QtWidgets.QPushButton("Convert")
        self.text1 = QtWidgets.QDoubleSpinBox ()  
        self.text1.setMaximum(1000000000)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)            
        
        self.combo1 = QtWidgets.QComboBox()        
        self.combo1.addItem("m")
        self.combo1.addItem("cm")
        self.combo1.addItem("ft")
        
        self.text2 = QtWidgets.QDoubleSpinBox ()   
        self.text2.setMaximum(1000000000)        
        self.text2.setAlignment(QtCore.Qt.AlignCenter)     
        
        self.combo2 = QtWidgets.QComboBox()       
        self.combo2.addItem("m")
        self.combo2.addItem("cm")
        self.combo2.addItem("ft")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.mainLayout = QtWidgets.QVBoxLayout()
        
        self.horizontalLayout.addWidget(self.text1)
        self.horizontalLayout.addWidget(self.combo1)
        self.horizontalLayout.addWidget(self.text2)
        self.horizontalLayout.addWidget(self.combo2)
        
        self.mainLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addWidget(self.button)
        self.setLayout(self.mainLayout)

        self.button.clicked.connect(self.convert)

    def convert(self):
        meters = float(self.text1.value())
        if self.combo1.currentIndex() == 1:
            meters = meters / 100
        if self.combo1.currentIndex() == 2:
            meters = meters * 0.3048    
            
        output = meters
        if self.combo2.currentIndex() == 1:
            output = output * 100
        if self.combo2.currentIndex() == 2:
            output = output / 0.3048    
            
        self.text2.setValue(output)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = LengthConverter()
    widget.setWindowTitle('Length Converter');
    widget.resize(400, 100)
    widget.show()

    sys.exit(app.exec_())