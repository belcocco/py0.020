#!/usr/bin/env python
import pygtk
#pygtk.require('2.0')
import gtk
class SecondWin:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.label = gtk.Label("Hello (cruel) World....")
		self.win.add(self.label)
		self.win.show_all()
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return gtk.main_quit()
	def main(self):
		gtk.main()
if __name__ == "__main__":
	second = SecondWin()
	second.main()

