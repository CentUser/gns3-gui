# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dominik/projects/gns3-gui/gns3/ui/edit_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditProjectDialog(object):
    def setupUi(self, EditProjectDialog):
        EditProjectDialog.setObjectName("EditProjectDialog")
        EditProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditProjectDialog.resize(955, 387)
        EditProjectDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(EditProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(EditProjectDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiSceneWidthLabel = QtWidgets.QLabel(self.tab)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.gridLayout_3.addWidget(self.uiSceneWidthLabel, 2, 0, 1, 1)
        self.uiProjectAutoCloseCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiProjectAutoCloseCheckBox.setObjectName("uiProjectAutoCloseCheckBox")
        self.gridLayout_3.addWidget(self.uiProjectAutoCloseCheckBox, 9, 0, 1, 3)
        self.uiProjectNameLabel = QtWidgets.QLabel(self.tab)
        self.uiProjectNameLabel.setObjectName("uiProjectNameLabel")
        self.gridLayout_3.addWidget(self.uiProjectNameLabel, 1, 0, 1, 1)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.gridLayout_3.addWidget(self.uiSceneWidthSpinBox, 2, 1, 1, 1)
        self.uiGridSizeSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiGridSizeSpinBox.setObjectName("uiGridSizeSpinBox")
        self.gridLayout_3.addWidget(self.uiGridSizeSpinBox, 4, 1, 1, 1)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.gridLayout_3.addWidget(self.uiSceneHeightSpinBox, 3, 1, 1, 1)
        self.uiSceneHeightLabel = QtWidgets.QLabel(self.tab)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.gridLayout_3.addWidget(self.uiSceneHeightLabel, 3, 0, 1, 1)
        self.uiProjectNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiProjectNameLineEdit.setObjectName("uiProjectNameLineEdit")
        self.gridLayout_3.addWidget(self.uiProjectNameLineEdit, 1, 1, 1, 1)
        self.uiGridSizeLabel = QtWidgets.QLabel(self.tab)
        self.uiGridSizeLabel.setObjectName("uiGridSizeLabel")
        self.gridLayout_3.addWidget(self.uiGridSizeLabel, 4, 0, 1, 1)
        self.uiProjectAutoOpenCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiProjectAutoOpenCheckBox.setObjectName("uiProjectAutoOpenCheckBox")
        self.gridLayout_3.addWidget(self.uiProjectAutoOpenCheckBox, 7, 0, 1, 3)
        self.uiProjectAutoStartCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiProjectAutoStartCheckBox.setObjectName("uiProjectAutoStartCheckBox")
        self.gridLayout_3.addWidget(self.uiProjectAutoStartCheckBox, 8, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(EditProjectDialog)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 0, 1, 1)

        self.retranslateUi(EditProjectDialog)
        self.tabWidget.setCurrentIndex(0)
        self.uiButtonBox.accepted.connect(EditProjectDialog.accept)
        self.uiButtonBox.rejected.connect(EditProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditProjectDialog)

    def retranslateUi(self, EditProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        EditProjectDialog.setWindowTitle(_translate("EditProjectDialog", "Edit project"))
        self.uiSceneWidthLabel.setText(_translate("EditProjectDialog", "Scene width:"))
        self.uiProjectAutoCloseCheckBox.setText(_translate("EditProjectDialog", "Leave this project running in the background when closing GNS3"))
        self.uiProjectNameLabel.setText(_translate("EditProjectDialog", "Project Name:"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneHeightLabel.setText(_translate("EditProjectDialog", "Scene height:"))
        self.uiGridSizeLabel.setText(_translate("EditProjectDialog", "Grid size:"))
        self.uiProjectAutoOpenCheckBox.setText(_translate("EditProjectDialog", "Open this project in the background when GNS3 server starts"))
        self.uiProjectAutoStartCheckBox.setText(_translate("EditProjectDialog", "Start all nodes when this project is opened"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("EditProjectDialog", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("EditProjectDialog", "Global variables"))

