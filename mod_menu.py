
from PyQt4 import QtGui
from PyQt4 import QtCore

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import subprocess


class MenuGUI(QtGui.QWidget):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.trayIcon = QSystemTrayIcon(self)
		self.trayIcon.setToolTip('Useful commands')
		#icon = QIcon.fromTheme("show-menu")
		icon = QIcon.fromTheme("media-playlist-repeat")
		#icon = QIcon.fromTheme("format-justify-fill")
		#icon = QIcon("/mnt/data/Matt/Profiles/canard2.png")
		self.trayIcon.setIcon(icon)
		self.loadConfig(True)
		#self.connect(self.trayIcon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), callWithAddParams(self.trayClick, ()))
		self.trayIcon.show()

	def validateConf(self):
		assert isinstance(menu_conf.config, list)
		for x in menu_conf.config:
			if x is None:
				continue
			assert isinstance(x, tuple), x
			assert len(x) == 4, x
			assert isinstance(x[0], basestring), x[0]
			assert isinstance(x[1], list), x[1]
			for y in x[1]:
				assert isinstance(y, basestring), y
			assert isinstance(x[2], basestring), x[2]
			assert isinstance(x[3], bool), x[3]

	def loadConfig(self, must_load):
		try:
			reload(menu_conf)
			self.validateConf()
			print "Configuration valid & loaded"
		except AssertionError:
			print "invalid configuration"
			menu_conf.config = []
		menu = self.buildMenu()
		if self.trayIcon.contextMenu() is not None:
			self.trayIcon.contextMenu().destroy()
		self.trayIcon.setContextMenu(menu)

	def buildMenu(self):
		menu = QMenu(self)
		print len(menu_conf.config), "items"
		for x in menu_conf.config:
			if x is None:
				menu.addSeparator()
			else:
				(displayname, command, iconname, immediate_exec) = x
				if QIcon.hasThemeIcon(iconname):
					icon = QIcon.fromTheme(iconname)
				else:
					icon = QIcon(iconname)
				action = menu.addAction(icon, displayname)
				self.connect(action, SIGNAL("triggered()"), callWithAddParams(self.launchCommand, (command,)))
				if immediate_exec:
					self.launchCommand(command)
		menu.addSeparator()
		action = menu.addAction(QIcon.fromTheme("view-refresh"), "Reload configuration")
		self.connect(action, SIGNAL("triggered()"), callWithAddParams(self.loadConfig, (False,)))
		menu.addAction(QIcon.fromTheme("window-close"), "Quit", self, SLOT("close()"))
		return menu

	def trayClick(self, reason):
		if reason == QSystemTrayIcon.Trigger:
			self.trayIcon.contextMenu().popup()
			#self.setVisible(not self.isVisible())

	def launchCommand(self, cmd):
		print cmd
		ret = subprocess.call(cmd)
		print ret
		return ret



def callWithAddParams(f, par):
	def newf(*args, **kwargs):
		print "call", f, par, args, kwargs
		return f(*(par+args), **kwargs)
	return newf


import menu_conf
def load():
	MenuGUI()

def unload():
	pass

