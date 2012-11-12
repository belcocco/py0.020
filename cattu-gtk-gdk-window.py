#!/usr/bin/env python

# example per catturare una gtk.gdk.Window

import pygtk
pygtk.require('2.0')
import gtk

class FirstWin(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
		self.connect("destroy", lambda w: gtk.main_quit())
		self.show()
		gdkwin = self.window
		print gdkwin
	def main(self):
		gtk.main()
if __name__ == "__main__":
	first = FirstWin()
	first.main

