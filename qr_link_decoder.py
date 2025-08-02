#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QR Link Decrypter (Cross-Platform GUI)

A simple tool to decode QR codes from clipboard or drag-and-drop images.
Useful for scanning links and short text embedded in QR codes.

Created on: 2025-08-02
Version: 1.0
Author: Ian Michael Bollinger (iPsychonaut)
Contact: ian.michael.bollinger@gmail.com
License: MIT

Dependencies:
- PyQt5
- NumPy
- Pillow (PIL)
- OpenCV (cv2)
"""

import sys
import os

import numpy as np
import cv2
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QLineEdit, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage


class QRDecoder(QWidget):
    """Main application window for QR code decoding."""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setAcceptDrops(True)

    def init_ui(self):
        """Initialize the GUI layout and elements."""
        self.setWindowTitle('QR Code Decoder (Cross-Platform)')
        self.setGeometry(100, 100, 400, 300)

        # Buttons
        self.paste_button = QPushButton('Paste QR Image from Clipboard', self)
        self.paste_button.clicked.connect(self.paste_image)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clear_fields)

        # Result field
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)

        # Drag & drop label
        self.label = QLabel('Drag and drop a QR image here', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")

        # Layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.paste_button)
        button_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result)
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)

    def paste_image(self):
        """Decode QR code from clipboard image."""
        clipboard = QApplication.clipboard()
        qt_image = clipboard.image()

        if qt_image.isNull():
            self.result.setText("No image in clipboard.")
            return

        qt_image = qt_image.convertToFormat(QImage.Format.Format_RGB32)
        width, height = qt_image.width(), qt_image.height()
        ptr = qt_image.bits()
        ptr.setsize(qt_image.byteCount())
        arr = np.array(ptr).reshape((height, width, 4))[:, :, :3]

        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(arr)

        if data:
            self.result.setText(data)
        else:
            self.result.setText("No QR code found.")

    def decode_image(self, pil_img):
        """Decode QR code from a given PIL image."""
        try:
            img = np.array(pil_img.convert('RGB'))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(img)

            if data:
                self.result.setText(data)
            else:
                self.result.setText("No QR code found.")
        except Exception as e:
            self.result.setText(f"Error decoding: {str(e)}")

    def dragEnterEvent(self, event):
        """Handle drag enter event."""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Handle drop event and try to decode QR code."""
        for url in event.mimeData().urls():
            filepath = url.toLocalFile()
            if os.path.isfile(filepath):
                try:
                    img = Image.open(filepath)
                    self.decode_image(img)
                except Exception as e:
                    self.result.setText(f"Error reading file: {str(e)}")
                break

    def clear_fields(self):
        """Clear all fields and reset drag-and-drop message."""
        self.result.clear()
        self.label.setText('Drag and drop a QR image here')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    decoder = QRDecoder()
    decoder.show()
    sys.exit(app.exec_())
