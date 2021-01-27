import sys


import var
from venEvasor import *
import conexion


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_Proyecto1()
        var.ui.setupUi(self)
        conexion.Conexion.db_connect(var.filebd)

        var.ui.centralwidget.show()
        var.ui.btnIniciar.clicked.connect(conexion.Conexion.cargaJugador)
        var.ui.btnSalir.clicked.connect(sys.exit)
        var.ui.tableJug.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tableJug.clicked.connect(conexion.Conexion.cargarJug)

        conexion.Conexion.mostrarJugadores(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
