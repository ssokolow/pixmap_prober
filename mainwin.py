# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImgExperimentDialog(object):
    def setupUi(self, ImgExperimentDialog):
        ImgExperimentDialog.setObjectName("ImgExperimentDialog")
        ImgExperimentDialog.resize(506, 371)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ImgExperimentDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_scroller = QtWidgets.QScrollArea(ImgExperimentDialog)
        self.img_scroller.setWidgetResizable(True)
        self.img_scroller.setObjectName("img_scroller")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 351))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_display = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.img_display.setText("")
        self.img_display.setObjectName("img_display")
        self.verticalLayout.addWidget(self.img_display)
        self.img_scroller.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.img_scroller)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_browse = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_browse.setObjectName("lbl_browse")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_browse)
        self.btn_browse = QtWidgets.QPushButton(ImgExperimentDialog)
        self.btn_browse.setObjectName("btn_browse")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_browse)
        self.lbl_width = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_width.setObjectName("lbl_width")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_width)
        self.spin_width = QtWidgets.QSpinBox(ImgExperimentDialog)
        self.spin_width.setMinimum(1)
        self.spin_width.setObjectName("spin_width")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_width)
        self.lbl_offset = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_offset.setObjectName("lbl_offset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_offset)
        self.spin_offset = QtWidgets.QSpinBox(ImgExperimentDialog)
        self.spin_offset.setObjectName("spin_offset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_offset)
        self.lbl_format = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_format.setObjectName("lbl_format")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_format)
        self.combo_format = QtWidgets.QComboBox(ImgExperimentDialog)
        self.combo_format.setObjectName("combo_format")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.combo_format)
        self.horizontalLayout.addLayout(self.formLayout)
        self.lbl_browse.setBuddy(self.btn_browse)
        self.lbl_width.setBuddy(self.spin_width)
        self.lbl_offset.setBuddy(self.spin_offset)
        self.lbl_format.setBuddy(self.combo_format)

        self.retranslateUi(ImgExperimentDialog)
        QtCore.QMetaObject.connectSlotsByName(ImgExperimentDialog)

    def retranslateUi(self, ImgExperimentDialog):
        _translate = QtCore.QCoreApplication.translate
        ImgExperimentDialog.setWindowTitle(_translate("ImgExperimentDialog", "Explore Data As Image"))
        self.lbl_browse.setText(_translate("ImgExperimentDialog", "&Load File:"))
        self.btn_browse.setText(_translate("ImgExperimentDialog", "&Browse..."))
        self.lbl_width.setText(_translate("ImgExperimentDialog", "Wid&th:"))
        self.lbl_offset.setText(_translate("ImgExperimentDialog", "&Offset:"))
        self.lbl_format.setText(_translate("ImgExperimentDialog", "Pi&xel Format:"))

