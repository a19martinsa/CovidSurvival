from PyQt5 import QtWidgets, QtSql

import metodos
import var
from datetime import datetime, date


class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la BBDD', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion Establecida')
        return True

    def cargarFecha(self):
        try:
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            current_date = today.strftime("%d/%m/%Y")
            fecha = current_date + "  " + current_time
            var.fecha = fecha
        except Exception as error:
            print('Error cagar fecha: %s' % str(error))

    def cargaJugador(self):
        try:
            query = QtSql.QSqlQuery()
            var.jugador = var.ui.ltNombre.text()
            b = False
            if var.jugador != '':
                query.prepare('select nombre from jugadores ')
                if query.exec_():
                    while query.next():
                        if query.value(0) == var.jugador:
                            b = True
                else:
                    print("Error comparar jugadores: ", query.lastError().text())
                if not b:
                    Conexion.altaJugador(var.jugador)
                Conexion.cargarPuntmax(var.jugador)
                metodos.evasor(self)
        except Exception as error:
            print('Partida acabada %s' % str(error))
            return None

    def altaJugador(jugador):
        Conexion.cargarFecha(None)
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into jugadores (nombre,puntmax,fecha)'
            'VALUES ( :nombre, :puntmax,:fecha)')
        query.bindValue(':nombre', str(jugador))
        query.bindValue(':puntmax', str(0))
        query.bindValue(':fecha', str(var.fecha))

        if query.exec_():
            print("Inserción Correcta")
        else:
            print("Error: ", query.lastError().text())

        Conexion.mostrarJugadores(None)

    def mostrarJugadores(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select id, nombre ,puntmax ,fecha from jugadores order by puntmax desc')
        if query.exec_():
            while query.next():
                # crea la fila
                var.ui.tableJug.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tableJug.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                var.ui.tableJug.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(1))))
                var.ui.tableJug.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                var.ui.tableJug.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))

                index += 1
            Conexion.limpiarJug(self)
            var.ui.tableJug.selectRow(0)
            var.ui.tableJug.setFocus()
        else:
            print("Error mostrar jugadores: ", query.lastError().text())
        if index == 0:
            var.ui.tableJug.clearContents()

    def limpiarJug(self):
        datosfac = [var.ui.lblPuntMax_2, var.ui.ltNombre]
        for i, data in enumerate(datosfac):
            datosfac[i].setText('')

    def altaPartida(partida):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into partidas (puntuacion,idjugador)'
            'VALUES ( :puntuacion, :idjugador)')
        query.bindValue(':puntuacion', str(partida[0]))
        query.bindValue(':idjugador', str(partida[1]))

        if query.exec_():
            print("Inserción Correcta")
        else:
            print("Error: ", query.lastError().text())

        Conexion.mostrarClientes(None)

    def modifJug(jugador, puntmax):
        Conexion.cargarFecha(None)
        query = QtSql.QSqlQuery()
        query.prepare('update jugadores set puntmax=:puntmax ,fecha=:fecha where nombre =:nombre')
        query.bindValue(':nombre', str(jugador))
        query.bindValue(':puntmax', int(puntmax))
        query.bindValue(':fecha', str(var.fecha))

        if query.exec_():
            print("Update puntuacion Correcta")
        else:
            print("Error en Update puntuacion Correcta: ", query.lastError().text())

    def cargarJug(self):

        try:
            fila = var.ui.tableJug.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            var.ui.ltNombre.setText(str(fila[1]))
            var.ui.lblPuntMax_2.setText(str(fila[2]))
        except Exception as error:
            print('Error cargar Factura: %s ' % str(error))

    def cargarPuntmax(jugador):
        query = QtSql.QSqlQuery()
        query.prepare('select puntmax from jugadores where nombre =:nombre order by puntmax desc')
        query.bindValue(':nombre', str(jugador))
        if query.exec_():
            while query.next():
                var.puntmax = query.value(0)

        else:
            print("Error cargar puntuacion maxima jugador: ", query.lastError().text())
