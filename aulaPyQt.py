import sys
from PyQt5 import QtGui, QtCore, QtWidgets
#QtGui - definir rotinas da interface , QtCore - Eventos
class Main (QtWidgets):
	def __init__(self):
		QtWidgets.__init__(self,master)
		self.setGeometry(400,300,250,250)
		
app = QtGui.QApplication(sys.argv)
programa = Main()
programa.show()

sys.exit(app.exec_())