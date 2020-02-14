
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QFileInfo

import os
import sys
import subprocess

import menu_conf_type

class MenuGUI(QWidget):

	default_conf = menu_conf_type.tc_menu(
		title = 'Useful commands',
		icon  = 'media-playlist-repeat',
		items = []
	)

	_QFileIconProvider = QFileIconProvider()
	_live_processes = {}

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.trayIcon = QSystemTrayIcon(self)
		self.loadConfig(True)
		# self.trayIcon.activated.connect(callWithAddParams(self.trayClick, ()))
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
					assert y.run_at_startup in [True, False], y
					assert y.wait_for in [None, True, False], y
					assert isinstance(y.name, basestring), y
					assert y.icon is None or isinstance(y.icon, basestring), y
					assert y.cwd is None or isinstance(y.cwd, basestring), y
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
						else:
							icon = None
					elif QIcon.hasThemeIcon(x.icon):
						icon = QIcon.fromTheme(x.icon)
					else:
						icon = QIcon(x.icon)
					if icon is None:
						icon = QIcon.fromTheme("utilities-terminal")
					# wait_for:
					# - True: we wait for it to complete
					# - False: we run in the background without waiting for it
					# - None: we run the command as a daemon
					if x.wait_for:
						action = menu.addAction(icon, x.name)
						action.triggered.connect(callWithAddParams(self.launchCommand, (x.command, x.cwd,)))
						if x.run_at_startup:
							self.launchCommand(x.command, x.cwd)
					elif x.wait_for is not None:
						action = menu.addAction(icon, x.name)
						action.triggered.connect(callWithAddParams(self.launchCommandNoWait, (x.command, x.cwd,)))
						if x.run_at_startup:
							self.launchCommandNoWait(x.command, x.cwd)
					else:
						action = menu.addAction(x.name)
						action.setCheckable(True)
						action.triggered.connect(callWithAddParams(self.controlDaemon, (x.command, x.cwd,)))
						if x.run_at_startup:
							self.controlDaemon(x.command, x.cwd)
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
		action.triggered.connect(callWithAddParams(self.loadConfig, (False,)))
		menu.addAction(QIcon.fromTheme("window-close"), "Quit", self.close)
		return menu

	def trayClick(self, reason):
		if reason == QSystemTrayIcon.Trigger:
			self.trayIcon.contextMenu().popup()
			#self.setVisible(not self.isVisible())

	def launchCommand(self, cmd, cwd):
		print cmd
		if isinstance(cmd, basestring):
			if os.access(cmd, os.X_OK) and os.path.isfile(cmd):
				cmd = [cmd]
			else:
				cmd = ['xdg-open', cmd]
		ret = subprocess.call(cmd, cwd=cwd)
		print ret
		return ret

	def launchCommandNoWait(self, cmd, cwd):
		print cmd
		subprocess.Popen(cmd, close_fds=True, shell=False, env=os.environ, cwd=cwd)

	def controlDaemon(self, cmd, cwd):
		print cmd
		if cmd in self._live_processes:
			self._live_processes[cmd].terminate()
			self._live_processes[cmd].wait()
			del self._live_processes[cmd]
		else:
			self._live_processes[cmd] = subprocess.Popen( [cmd], close_fds=True, shell=False, env=os.environ, cwd=cwd)

	def closeEvent(self, event):
		print("closeEvent", event, event.isAccepted(), event.type(), event.spontaneous())
		self.trayIcon.hide()


def callWithAddParams(f, par):
	def newf(*args, **kwargs):
		print "call", f, par, args, kwargs
		return f(*par)
		# return f(*(par+args), **kwargs)
	return newf


import menu_conf
def load():
	MenuGUI()

def unload():
	pass

