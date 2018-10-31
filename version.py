# Just for check that Qt for Python is installed correctly

import PySide2.QtCore

# Prints PySide version
# e.g. 1.0.2
print(PySide2.__version__)

# Gets a tuple with each version component
# e.g. (1, 0, 2, 'final', 1)
print(PySide2.__version_info__)

# Prints the Qt version used to compile PySide
# e.g. "5.11.0"
print(PySide2.QtCore.__version__)

# Gets a tuple with each version components of Qt used to compile PySide
# e.g. (5, 11, 0)
print(PySide2.QtCore.__version_info__)

# Note that the Qt version used to compile Qt for Python may differ from the version used to run Qt for Python. 
#To print the current running Qt version number, you can use:

print(PySide2.QtCore.qVersion())

