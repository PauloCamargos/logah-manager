# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_equipment1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditEquipment(object):
    def setupUi(self, EditEquipment):
        EditEquipment.setObjectName("EditEquipment")
        EditEquipment.resize(927, 286)
        EditEquipment.setMinimumSize(QtCore.QSize(927, 286))
        EditEquipment.setMaximumSize(QtCore.QSize(927, 286))
        self.centralwidget = QtWidgets.QWidget(EditEquipment)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbx_equipments = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_equipments.sizePolicy().hasHeightForWidth())
        self.cbx_equipments.setSizePolicy(sizePolicy)
        self.cbx_equipments.setObjectName("cbx_equipments")
        self.horizontalLayout_2.addWidget(self.cbx_equipments)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_search_equipment = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search_equipment.setAutoDefault(False)
        self.btn_search_equipment.setObjectName("btn_search_equipment")
        self.horizontalLayout.addWidget(self.btn_search_equipment)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.ledit_description = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_description.sizePolicy().hasHeightForWidth())
        self.ledit_description.setSizePolicy(sizePolicy)
        self.ledit_description.setObjectName("ledit_description")
        self.horizontalLayout_4.addWidget(self.ledit_description)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.ledit_nserie = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_nserie.sizePolicy().hasHeightForWidth())
        self.ledit_nserie.setSizePolicy(sizePolicy)
        self.ledit_nserie.setObjectName("ledit_nserie")
        self.horizontalLayout_5.addWidget(self.ledit_nserie)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.ledit_function = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_function.sizePolicy().hasHeightForWidth())
        self.ledit_function.setSizePolicy(sizePolicy)
        self.ledit_function.setObjectName("ledit_function")
        self.horizontalLayout_6.addWidget(self.ledit_function)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.ledit_primary_place = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_primary_place.sizePolicy().hasHeightForWidth())
        self.ledit_primary_place.setSizePolicy(sizePolicy)
        self.ledit_primary_place.setObjectName("ledit_primary_place")
        self.horizontalLayout_7.addWidget(self.ledit_primary_place)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_update_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update_data.setObjectName("btn_update_data")
        self.horizontalLayout_9.addWidget(self.btn_update_data)
        self.btn_remove_equipment = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remove_equipment.setObjectName("btn_remove_equipment")
        self.horizontalLayout_9.addWidget(self.btn_remove_equipment)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        EditEquipment.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditEquipment)
        self.statusbar.setObjectName("statusbar")
        EditEquipment.setStatusBar(self.statusbar)

        self.retranslateUi(EditEquipment)
        QtCore.QMetaObject.connectSlotsByName(EditEquipment)

    def retranslateUi(self, EditEquipment):
        _translate = QtCore.QCoreApplication.translate
        EditEquipment.setWindowTitle(_translate("EditEquipment", "Editar equipmento"))
        self.label.setText(_translate("EditEquipment", "Equipamento"))
        self.btn_search_equipment.setText(_translate("EditEquipment", "Buscar dados"))
        self.groupBox.setTitle(_translate("EditEquipment", "Informações do equipamento"))
        self.label_2.setText(_translate("EditEquipment", "Descrição"))
        self.label_3.setText(_translate("EditEquipment", "Nº Série"))
        self.label_4.setText(_translate("EditEquipment", "Função"))
        self.label_5.setText(_translate("EditEquipment", "Local Primário"))
        self.btn_update_data.setText(_translate("EditEquipment", "Atualizar dados"))
        self.btn_remove_equipment.setText(_translate("EditEquipment", "Remover equipamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditEquipment = QtWidgets.QMainWindow()
    ui = Ui_EditEquipment()
    ui.setupUi(EditEquipment)
    EditEquipment.show()
    sys.exit(app.exec_())

