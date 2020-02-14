#!/usr/bin/env python2

from PyQt5.QtWidgets import QApplication

import sys

import mod_menu

app = QApplication(sys.argv)

mod_menu.load()

app.exec_()

mod_menu.unload()


