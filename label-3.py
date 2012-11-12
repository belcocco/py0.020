#!/usr/bin/env python
import pygtk
#pygtk.require('2.0')
import gtk
class SecondWin:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.vbox = gtk.VBox(gtk.TRUE, 0)
		self.win.add(self.vbox)
		self.label = gtk.Label("Hello (cruel) World....")
		self.button = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button.connect("clicked", self.change_text)
		self.vbox.pack_start(self.label)
		self.vbox.pack_start(self.button)
		self.win.show_all()
#	def change_text(self, widget, data=None):
#		self.label.set_text("Hello (better) World....")
	def change_text(self, widget, data=None):
		self.label.set_text("_Hello (better) World....")
		self.label.set_use_underline(gtk.TRUE)
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return gtk.main_quit()
	def main(self):
		gtk.main()
if __name__ == "__main__":
	second = SecondWin()
	second.main()

