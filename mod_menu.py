
from PyQt4 import QtGui
from PyQt4 import QtCore

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os
import sys
import subprocess

import menu_conf_type

class MenuGUI(QtGui.QWidget):

	default_conf = menu_conf_type.tc_menu(
		title = 'Useful commands',
		icon  = 'media-playlist-repeat',
		items = []
	)

	_QFileIconProvider = QFileIconProvider()
	_live_processes = {}

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.trayIcon = QSystemTrayIcon(self)
		self.loadConfig(True)
		#self.connect(self.trayIcon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), callWithAddParams(self.trayClick, ()))
		self.trayIcon.show()

	def validateConf(self):
		def validate_tc_menu(x):
			assert isinstance(x, menu_conf_type.tc_menu), x
			assert isinstance(x.icon, basestring), x
			assert isinstance(x.title, basestring), x
			assert isinstance(x.items, list), x
			for y in x.items:
				if y is None:
					continue
				if isinstance(y, menu_conf_type.tc_item):
					assert y.do_exec in [True, False, 'tickbox'], y
					assert isinstance(y.name, basestring), y
					assert y.icon is None or isinstance(y.icon, basestring), y
					assert isinstance(y.command, basestring) or isinstance(y.command, list), y
					if isinstance(y.command, list):
						for z in y:
							assert isinstance(z, basestring), z
				elif isinstance(y, menu_conf_type.tc_menu):
					validate_tc_menu(y)
				else:
					assert False, y

		#validate_tc_menu(menu_conf.config)

	def loadConfig(self, must_load):
		try:
			reload(menu_conf)
			self.validateConf()
			print "Menu configuration valid & loaded"
		except AssertionError:
			print "invalid configuration"
			menu_conf.config = self.default_conf
		menu = self.buildMenu()
		if self.trayIcon.contextMenu() is not None:
			self.trayIcon.contextMenu().destroy()
		self.trayIcon.setToolTip(menu_conf.config.title)
		icon = QIcon.fromTheme(menu_conf.config.icon)
		self.trayIcon.setIcon(icon)
		self.trayIcon.setContextMenu(menu)

	def buildMenu(self):
		def addMenuItems(menu, items):
			print len(items), "items"
			for x in items:
				if x is None:
					menu.addSeparator()
				elif isinstance(x, menu_conf_type.tc_item):
					if x.icon is None:
						if isinstance(x.command, basestring):
							info = QFileInfo(x.command)
							icon = self._QFileIconProvider.icon(info)
					elif QIcon.hasThemeIcon(x.icon):
						icon = QIcon.fromTheme(x.icon)
					else:
						icon = QIcon(x.icon)
					if isinstance(x.do_exec, bool):
						action = menu.addAction(icon, x.name)
						self.connect(action, SIGNAL("triggered()"), callWithAddParams(self.launchCommand, (x.command,)))
						if x.do_exec:
							self.launchCommand(x.command)
					else:
						action = menu.addAction(x.name)
						action.setCheckable(True)
						self.connect(action, SIGNAL("triggered()"), callWithAddParams(self.launchSubCommand, (x.command,)))
				elif len(x) == 3:
					if QIcon.hasThemeIcon(x.icon):
						icon = QIcon.fromTheme(x.icon)
					else:
						icon = QIcon(x.icon)
					submenu = menu.addMenu(icon, x.title)
					addMenuItems(submenu, x.items)

		menu = QMenu(self)
		addMenuItems(menu, menu_conf.config.items)
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
		if isinstance(cmd, basestring):
			if os.access(cmd, os.X_OK) and os.path.isfile(cmd):
				cmd = [cmd]
			else:
				cmd = ['xdg-open', cmd]
		ret = subprocess.call(cmd)
		print ret
		return ret

	def launchSubCommand(self, cmd):
		print cmd
		if cmd in self._live_processes:
			self._live_processes[cmd].terminate()
			self._live_processes[cmd].wait()
			del self._live_processes[cmd]
		else:
			self._live_processes[cmd] = subprocess.Popen( [cmd], close_fds=True, shell=False, env=os.environ)



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

