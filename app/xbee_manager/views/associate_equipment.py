# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'associate_equipment.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AssociateEquipment(object):
    def setupUi(self, AssociateEquipment):
        AssociateEquipment.setObjectName("AssociateEquipment")
        AssociateEquipment.resize(961, 285)
        AssociateEquipment.setMinimumSize(QtCore.QSize(961, 285))
        AssociateEquipment.setMaximumSize(QtCore.QSize(961, 285))
        self.centralwidget = QtWidgets.QWidget(AssociateEquipment)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cbx_xbees = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_xbees.sizePolicy().hasHeightForWidth())
        self.cbx_xbees.setSizePolicy(sizePolicy)
        self.cbx_xbees.setObjectName("cbx_xbees")
        self.horizontalLayout_4.addWidget(self.cbx_xbees)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.list_xbees = QtWidgets.QListWidget(self.groupBox)
        self.list_xbees.setObjectName("list_xbees")
        self.verticalLayout_4.addWidget(self.list_xbees)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.ledit_descritpion = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_descritpion.sizePolicy().hasHeightForWidth())
        self.ledit_descritpion.setSizePolicy(sizePolicy)
        self.ledit_descritpion.setBaseSize(QtCore.QSize(0, 0))
        self.ledit_descritpion.setObjectName("ledit_descritpion")
        self.horizontalLayout_9.addWidget(self.ledit_descritpion)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.ledit_nserie = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_nserie.sizePolicy().hasHeightForWidth())
        self.ledit_nserie.setSizePolicy(sizePolicy)
        self.ledit_nserie.setBaseSize(QtCore.QSize(5, 0))
        self.ledit_nserie.setObjectName("ledit_nserie")
        self.horizontalLayout_12.addWidget(self.ledit_nserie)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.ledit_function = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_function.sizePolicy().hasHeightForWidth())
        self.ledit_function.setSizePolicy(sizePolicy)
        self.ledit_function.setBaseSize(QtCore.QSize(5, 0))
        self.ledit_function.setObjectName("ledit_function")
        self.horizontalLayout_10.addWidget(self.ledit_function)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.ledit_primary_place = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_primary_place.sizePolicy().hasHeightForWidth())
        self.ledit_primary_place.setSizePolicy(sizePolicy)
        self.ledit_primary_place.setObjectName("ledit_primary_place")
        self.horizontalLayout_11.addWidget(self.ledit_primary_place)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_associate_equipment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_associate_equipment.sizePolicy().hasHeightForWidth())
        self.btn_associate_equipment.setSizePolicy(sizePolicy)
        self.btn_associate_equipment.setMinimumSize(QtCore.QSize(400, 0))
        self.btn_associate_equipment.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btn_associate_equipment.setObjectName("btn_associate_equipment")
        self.verticalLayout_3.addWidget(self.btn_associate_equipment, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        AssociateEquipment.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AssociateEquipment)
        self.statusbar.setObjectName("statusbar")
        AssociateEquipment.setStatusBar(self.statusbar)

        self.retranslateUi(AssociateEquipment)
        QtCore.QMetaObject.connectSlotsByName(AssociateEquipment)

    def retranslateUi(self, AssociateEquipment):
        _translate = QtCore.QCoreApplication.translate
        AssociateEquipment.setWindowTitle(_translate("AssociateEquipment", "Associar Equipamento"))
        self.groupBox.setTitle(_translate("AssociateEquipment", "Informações do dispositivo"))
        self.label.setText(_translate("AssociateEquipment", "XBee"))
        self.groupBox_2.setTitle(_translate("AssociateEquipment", "Informações do equipamento"))
        self.label_2.setText(_translate("AssociateEquipment", "Descrição"))
        self.label_3.setText(_translate("AssociateEquipment", "Nº Série"))
        self.label_4.setText(_translate("AssociateEquipment", "Função"))
        self.label_5.setText(_translate("AssociateEquipment", "Local Primário"))
        self.btn_associate_equipment.setText(_translate("AssociateEquipment", "Associar equipamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssociateEquipment = QtWidgets.QMainWindow()
    ui = Ui_AssociateEquipment()
    ui.setupUi(AssociateEquipment)
    AssociateEquipment.show()
    sys.exit(app.exec_())

