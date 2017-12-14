#Fazer o Formulario no PyQt
#Transformar em py
#Criar outro arquivo py para chamar o Formulario
#Importar o formulário
#Criar uma Classe herdando o formulário conforme abaixo:
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pessoa import Ui_MainWindow #Nome da caixa de dialogo

class Main(QtGui.QWindow):# Herda as propriedades do formulário criado
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

app=QtWidgets.QApplication(sys.argv)
programa=Main()
programa.show()
sys.exit(app.exec_())