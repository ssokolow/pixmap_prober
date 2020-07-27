# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImgExperimentDialog(object):
    def setupUi(self, ImgExperimentDialog):
        ImgExperimentDialog.setObjectName("ImgExperimentDialog")
        ImgExperimentDialog.resize(483, 324)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ImgExperimentDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_scroller = QtWidgets.QScrollArea(ImgExperimentDialog)
        self.img_scroller.setWidgetResizable(True)
        self.img_scroller.setObjectName("img_scroller")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 228, 304))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
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
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.lbl_browse)
        self.btn_browse = QtWidgets.QPushButton(ImgExperimentDialog)
        self.btn_browse.setObjectName("btn_browse")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.btn_browse)
        self.lbl_stride = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_stride.setObjectName("lbl_stride")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.lbl_stride)
        self.lbl_offset = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_offset.setObjectName("lbl_offset")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.lbl_offset)
        self.spin_offset = QtWidgets.QSpinBox(ImgExperimentDialog)
        self.spin_offset.setObjectName("spin_offset")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.spin_offset)
        self.spin_stride = QtWidgets.QSpinBox(ImgExperimentDialog)
        self.spin_stride.setMinimum(1)
        self.spin_stride.setObjectName("spin_stride")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.spin_stride)
        self.lbl_format = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_format.setObjectName("lbl_format")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.lbl_format)
        self.combo_format = QtWidgets.QComboBox(ImgExperimentDialog)
        self.combo_format.setObjectName("combo_format")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.combo_format)
        self.lbl_width = QtWidgets.QLabel(ImgExperimentDialog)
        self.lbl_width.setObjectName("lbl_width")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lbl_width)
        self.spin_width = QtWidgets.QSpinBox(ImgExperimentDialog)
        self.spin_width.setMinimum(1)
        self.spin_width.setObjectName("spin_width")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.spin_width)
        self.horizontalLayout.addLayout(self.formLayout)
        self.lbl_browse.setBuddy(self.btn_browse)
        self.lbl_stride.setBuddy(self.spin_stride)
        self.lbl_offset.setBuddy(self.spin_offset)
        self.lbl_format.setBuddy(self.combo_format)
        self.lbl_width.setBuddy(self.spin_width)

        self.retranslateUi(ImgExperimentDialog)
        QtCore.QMetaObject.connectSlotsByName(ImgExperimentDialog)

    def retranslateUi(self, ImgExperimentDialog):
        _translate = QtCore.QCoreApplication.translate
        ImgExperimentDialog.setWindowTitle(
            _translate("ImgExperimentDialog", "Explore Data As Image"))
        self.lbl_browse.setText(
            _translate("ImgExperimentDialog", "&Load File:"))
        self.btn_browse.setText(
            _translate("ImgExperimentDialog", "&Browse..."))
        self.lbl_stride.setText(_translate("ImgExperimentDialog", "S&tride:"))
        self.lbl_offset.setText(_translate("ImgExperimentDialog", "&Offset:"))
        self.lbl_format.setText(
            _translate("ImgExperimentDialog", "Pi&xel Format:"))
        self.lbl_width.setText(_translate("ImgExperimentDialog", "&Width:"))

# --- Stuff below this line added manually and must be preserved ---


class MainWin(QtWidgets.QWidget, Ui_ImgExperimentDialog):
    IMG_FORMATS = {
        QtGui.QImage.Format_Mono: ('Mono (MSB)', 1 / 8.0),
        QtGui.QImage.Format_MonoLSB: ('Mono (LSB)', 1 / 8.0),
        QtGui.QImage.Format_Grayscale8: ('8-bit Grayscale', 1),
        QtGui.QImage.Format_Grayscale16: ('16-bit Grayscale', 2),
        # TODO: Indexed8 with some default 256-color palette
        QtGui.QImage.Format_RGB16: ('RGB16', 2),
        QtGui.QImage.Format_RGB444: ('RGB444', 2),
        QtGui.QImage.Format_RGB555: ('RGB555', 2),
        QtGui.QImage.Format_RGB666: ('RGB666', 3),
        QtGui.QImage.Format_RGB888: ('RGB888', 3),
        QtGui.QImage.Format_RGB32: ('RGB32', 4),
        QtGui.QImage.Format_ARGB32: ('ARGB32', 4),
        # TODO: The rest of the formats
    }

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        self.raw_data = b''
        self.pixmap = QtGui.QPixmap()
        self.btn_browse.clicked.connect(self.cb_browse)

        self.spin_width.valueChanged.connect(self.cb_update_img)
        self.spin_stride.valueChanged.connect(self.cb_update_img)
        self.spin_offset.valueChanged.connect(self.cb_update_img)

    def cb_browse(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Open Data File")
        if fname and fname[0]:
            with open(fname[0], 'rb') as fobj:
                self.raw_data = fobj.read()
                self.cb_update_img()

    def cb_resized(self):
        if not self.pixmap.isNull():
            self.img_display.setPixmap(self.pixmap.scaled(
                self.img_display.size(),
                QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def cb_update_img(self):
        offset = self.spin_offset.value()
        data = self.raw_data[offset:]

        self.spin_width.setMaximum(len(data))
        width = self.spin_width.value()

        height = len(data) // width
        stride = width  # TODO

        img = QtGui.QImage(data, width, height, stride,
            QtGui.QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap.fromImage(img)
        self.img_display.setPixmap(self.pixmap)
        self.cb_resized()

    def resizeEvent(self, _event=None):
        self.cb_resized()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainwin = MainWin()
    mainwin.show()
    app.exec_()
