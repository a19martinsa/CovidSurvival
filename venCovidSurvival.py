# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venCovidSurvival.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Proyecto1(object):
    def setupUi(self, Proyecto1):
        Proyecto1.setObjectName("Proyecto1")
        Proyecto1.setWindowModality(QtCore.Qt.NonModal)
        Proyecto1.resize(1173, 907)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Proyecto1.sizePolicy().hasHeightForWidth())
        Proyecto1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        Proyecto1.setFont(font)
        Proyecto1.setAutoFillBackground(False)
        Proyecto1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Proyecto1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 160, 511, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblNombre = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setStyleSheet("\n"
"color: rgba( 255, 255, 255);")
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout.addWidget(self.lblNombre, 0, 0, 1, 1)
        self.lblPuntMax = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblPuntMax.setFont(font)
        self.lblPuntMax.setStyleSheet("\n"
"color: rgba( 255, 255, 255);")
        self.lblPuntMax.setObjectName("lblPuntMax")
        self.gridLayout.addWidget(self.lblPuntMax, 1, 0, 1, 1)
        self.ltNombre = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ltNombre.sizePolicy().hasHeightForWidth())
        self.ltNombre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.ltNombre.setFont(font)
        self.ltNombre.setTabletTracking(False)
        self.ltNombre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ltNombre.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.ltNombre.setObjectName("ltNombre")
        self.gridLayout.addWidget(self.ltNombre, 0, 1, 1, 3)
        self.lblPuntMax_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPuntMax_2.sizePolicy().hasHeightForWidth())
        self.lblPuntMax_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblPuntMax_2.setFont(font)
        self.lblPuntMax_2.setStyleSheet("background-color: rgb( 255, 255, 255);\n"
"")
        self.lblPuntMax_2.setText("")
        self.lblPuntMax_2.setObjectName("lblPuntMax_2")
        self.gridLayout.addWidget(self.lblPuntMax_2, 1, 1, 1, 3)
        self.tableJug = QtWidgets.QTableWidget(self.centralwidget)
        self.tableJug.setGeometry(QtCore.QRect(170, 410, 771, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableJug.sizePolicy().hasHeightForWidth())
        self.tableJug.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tableJug.setFont(font)
        self.tableJug.setTabletTracking(False)
        self.tableJug.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableJug.setAutoFillBackground(False)
        self.tableJug.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"gridline-color:rgb(0, 0, 0);\n"
"boder-color:rgb(0, 0, 0);")
        self.tableJug.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableJug.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableJug.setAlternatingRowColors(True)
        self.tableJug.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableJug.setShowGrid(True)
        self.tableJug.setObjectName("tableJug")
        self.tableJug.setColumnCount(4)
        self.tableJug.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableJug.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableJug.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableJug.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableJug.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableJug.setHorizontalHeaderItem(3, item)
        self.tableJug.horizontalHeader().setVisible(True)
        self.tableJug.horizontalHeader().setCascadingSectionResizes(False)
        self.tableJug.horizontalHeader().setDefaultSectionSize(180)
        self.tableJug.horizontalHeader().setHighlightSections(True)
        self.tableJug.horizontalHeader().setMinimumSectionSize(35)
        self.tableJug.horizontalHeader().setSortIndicatorShown(False)
        self.tableJug.horizontalHeader().setStretchLastSection(True)
        self.tableJug.verticalHeader().setVisible(False)
        self.tableJug.verticalHeader().setCascadingSectionResizes(True)
        self.tableJug.verticalHeader().setDefaultSectionSize(40)
        self.tableJug.verticalHeader().setSortIndicatorShown(False)
        self.tableJug.verticalHeader().setStretchLastSection(False)
        self.lblTitulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo_2.setGeometry(QtCore.QRect(170, 340, 771, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblTitulo_2.setFont(font)
        self.lblTitulo_2.setStyleSheet("background-color: rgba( 255, 255, 255);\n"
"text-decoration: underline ;")
        self.lblTitulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo_2.setObjectName("lblTitulo_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(410, 290, 321, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnIniciar_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.btnIniciar_2.setFont(font)
        self.btnIniciar_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btnIniciar_2.setObjectName("btnIniciar_2")
        self.gridLayout_2.addWidget(self.btnIniciar_2, 0, 0, 1, 1)
        self.btnIniciar = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btnIniciar.setObjectName("btnIniciar")
        self.gridLayout_2.addWidget(self.btnIniciar, 0, 1, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout_2.addWidget(self.btnSalir, 0, 2, 1, 1)
        Proyecto1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Proyecto1)
        QtCore.QMetaObject.connectSlotsByName(Proyecto1)

    def retranslateUi(self, Proyecto1):
        _translate = QtCore.QCoreApplication.translate
        Proyecto1.setWindowTitle(_translate("Proyecto1", "Esquiva al bicho"))
        self.lblNombre.setText(_translate("Proyecto1", "Nombre jugador"))
        self.lblPuntMax.setText(_translate("Proyecto1", "Puntuación máxima"))
        item = self.tableJug.verticalHeaderItem(0)
        item.setText(_translate("Proyecto1", "1"))
        item = self.tableJug.verticalHeaderItem(1)
        item.setText(_translate("Proyecto1", "2"))
        item = self.tableJug.verticalHeaderItem(2)
        item.setText(_translate("Proyecto1", "3"))
        item = self.tableJug.verticalHeaderItem(3)
        item.setText(_translate("Proyecto1", "4"))
        item = self.tableJug.verticalHeaderItem(4)
        item.setText(_translate("Proyecto1", "5"))
        item = self.tableJug.verticalHeaderItem(5)
        item.setText(_translate("Proyecto1", "6"))
        item = self.tableJug.verticalHeaderItem(6)
        item.setText(_translate("Proyecto1", "8"))
        item = self.tableJug.horizontalHeaderItem(0)
        item.setText(_translate("Proyecto1", "ID"))
        item = self.tableJug.horizontalHeaderItem(1)
        item.setText(_translate("Proyecto1", "NOMBRE"))
        item = self.tableJug.horizontalHeaderItem(2)
        item.setText(_translate("Proyecto1", "PUNT.MAX"))
        item = self.tableJug.horizontalHeaderItem(3)
        item.setText(_translate("Proyecto1", "FECHA"))
        self.lblTitulo_2.setText(_translate("Proyecto1", "LISTA JUGADORES"))
        self.btnIniciar_2.setText(_translate("Proyecto1", "Nuevo Jug."))
        self.btnIniciar.setText(_translate("Proyecto1", "Iniciar"))
        self.btnSalir.setText(_translate("Proyecto1", "Salir"))
