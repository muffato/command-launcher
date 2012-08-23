#!/usr/bin/env python

from PyQt4 import QtGui

import sys

import mod_menu

app = QtGui.QApplication(sys.argv)

mod_menu.load()

app.exec_()

mod_menu.unload()


