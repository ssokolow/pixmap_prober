#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple tool for experimenting with interpreting raw file data as pixels

Not as flexible as it should be on the pixel formats because this was just me
getting nerd-sniped on something I had no need for myself.
"""

__author__ = "Stephan Sokolow (deitarion/SSokolow)"
__appname__ = "Pixmap Prober"
__version__ = "0.1a1"
__license__ = "MIT"

import math
import sys

# pylint: disable=import-error,no-name-in-module
from PyQt5.QtCore import Qt  # type: ignore
from PyQt5.QtGui import QImage, QPixmap  # type: ignore
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget  # type: ignore

from mainwin import Ui_ImgExperimentDialog


class MainWin(QWidget, Ui_ImgExperimentDialog):
    QT_IMG_FORMATS = [
        ('Mono (MSB)', (QImage.Format_Mono, 1 / 8.0)),
        ('Mono (LSB)', (QImage.Format_MonoLSB, 1 / 8.0)),
        ('8-bit Grayscale', (QImage.Format_Grayscale8, 1)),
        # Qt 5.13+: ('16-bit Grayscale', (QImage.Format_Grayscale16, 2)),
        # TODO: Indexed8 with some default 256-color palette
        ('RGB16', (QImage.Format_RGB16, 2)),
        ('RGB444', (QImage.Format_RGB444, 2)),
        ('RGB555', (QImage.Format_RGB555, 2)),
        ('RGB666', (QImage.Format_RGB666, 3)),
        ('RGB888', (QImage.Format_RGB888, 3)),
        ('RGB32', (QImage.Format_RGB32, 4)),
        ('ARGB4444 (Premultiplied)',
         (QImage.Format_ARGB4444_Premultiplied, 2)),
        ('ARGB6666 (Premultiplied)',
         (QImage.Format_ARGB6666_Premultiplied, 3)),
        ('ARGB8555 (Premultiplied)',
         (QImage.Format_ARGB8555_Premultiplied, 3)),
        ('ARGB8565 (Premultiplied)',
         (QImage.Format_ARGB8565_Premultiplied, 3)),
        ('ARGB32', (QImage.Format_ARGB32, 4)),
        ('ARGB32 (Premultiplied)', (QImage.Format_ARGB32_Premultiplied, 4)),
        ('RGBX8888', (QImage.Format_RGBX8888, 4)),
        ('RGBA8888', (QImage.Format_RGBA8888, 4)),
        ('RGBA8888 (Premultiplied)',
         (QImage.Format_RGBA8888_Premultiplied, 4)),
        # TODO: The rest of the formats
    ]

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        for name, userdata in self.QT_IMG_FORMATS:
            self.combo_format.addItem(name, userdata)

        self.raw_data = b''
        self.pixmap = QPixmap()
        self.btn_browse.clicked.connect(self.cb_browse)

        self.spin_width.valueChanged.connect(self.cb_update_img)
        self.spin_offset.valueChanged.connect(self.cb_update_img)
        self.combo_format.activated.connect(self.cb_update_img)

    def cb_browse(self):
        """Callback for the Browse button"""
        fname = QFileDialog.getOpenFileName(self, "Open Data File")
        if fname and fname[0]:
            self.spin_width.setEnabled(True)
            self.spin_offset.setEnabled(True)
            self.combo_format.setEnabled(True)
            with open(fname[0], 'rb') as fobj:
                self.raw_data = fobj.read()
                self.cb_update_img(reset_width=True)

    def cb_resized(self):
        """Called by anything which requires the image scale to be updated"""
        if not self.pixmap.isNull():
            pix = self.pixmap

            # Start with a Nearest Neighbour upscaling scaling to the closest
            # integer multiple that fits within the target
            for factor in range(32, 1, -2):
                candidate = pix.size() * factor
                target = self.img_display.size()

                if (candidate.width() > target.width() or
                        candidate.height() > target.height()):
                    continue

                pix = pix.scaled(candidate,
                    Qt.KeepAspectRatio, Qt.FastTransformation)

            # Handle downscaling and the final upscale reconciliation using
            # smoothed scaling
            self.img_display.setPixmap(pix.scaled(
                self.img_display.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def cb_update_img(self, event=None, reset_width=False):
        """Called by anything which changes how the bytes get rendered"""
        pixfmt, stride_factor = self.combo_format.currentData()
        offset = self.spin_offset.value()

        # TODO: Override stepBy to do this properly
        if stride_factor < 1:
            self.spin_width.setMinimum(8)
            self.spin_width.setSingleStep(8)
        else:
            self.spin_width.setMinimum(1)
            self.spin_width.setSingleStep(1)

        data = self.raw_data[offset:]

        # The stride factor is the number of pixels per line, so the pixel
        # count is the number of bytes divided by the stride factor.
        # We want the maximum width to be pix_count because that corresponds
        # to a minimum height of 1.
        #
        # For some reason, we have to treat stride_factor as 1 when dealing
        # with formats that pack more than one pixel per byte
        pix_count = len(data) / max(1, stride_factor)
        self.spin_width.setMaximum(round(pix_count / 8) * 8)

        width = self.spin_width.value()
        if reset_width:
            width = int(math.sqrt(pix_count))
            if stride_factor < 1:
                width = round(width / 8) * 8
            self.spin_width.setValue(width)

        # TODO: Pad out the final line so it can be displayed too
        stride = int(width * stride_factor)
        height = int(len(data) // stride)

        img = QImage(data, int(width), height, stride, pixfmt)
        self.pixmap = QPixmap.fromImage(img)
        self.img_display.setPixmap(self.pixmap)
        self.cb_resized()

    def resizeEvent(self, event):
        """Patch Qt's window resize into cb_resized"""
        super(MainWin, self).resizeEvent(event)
        self.cb_resized()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwin = MainWin()
    mainwin.show()
    app.exec_()

# vim: set sw=4 sts=4 expandtab :
