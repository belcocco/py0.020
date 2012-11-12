#!/usr/bin/env python
import pygtk
#pygtk.require('2.0')
import gtk
class SecondWin:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_border_width(10)
		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.hbox = gtk.HBox(gtk.TRUE, 10)
		self.win.add(self.hbox)
		self.label = gtk.Label("_Switch me on")
		self.label.set_use_underline(gtk.TRUE)
		self.button = gtk.CheckButton(None, None)
		self.label.set_mnemonic_widget(self.button)
		self.button.connect("toggled", self.switch)
		self.hbox.pack_start(self.label)
		self.hbox.pack_start(self.button)
		self.win.show_all()
	def switch(self, widget, data=None):
		(data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return gtk.main_quit()
	def main(self):
		gtk.main()
if __name__ == "__main__":
	second = SecondWin()
	second.main()

