#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
class SecondWin:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.win.set_resizable(gtk.FALSE)
		self.win.set_border_width(10)
		self.vbox = gtk.VBox(gtk.TRUE, 5)
		self.win.add(self.vbox)
		self.vbox.show()

		self.button_r1 = gtk.RadioButton(None, "primo radio", gtk.FALSE)
		self.button_r1.connect("toggled", self.tog, "primo radio")
		self.button_r2 = gtk.RadioButton(self.button_r1, "secondo radio")
		self.button_r2.connect("toggled", self.tog, "secondo radio")
		self.button_r3 = gtk.RadioButton(self.button_r1, "terzo radio")
		self.button_r3.connect("toggled", self.tog, "terzo radio")

		self.button_t1 = gtk.ToggleButton("primo toggle")
		self.button_t1.connect("toggled", self.tog, "primo toggle")
		self.button_t2 = gtk.ToggleButton("secondo toggle")
		self.button_t2.connect("toggled", self.tog, "secondo toggle")

		self.button = gtk.Button(None, gtk.STOCK_QUIT)
		self.button.connect("clicked", self.destroy)

		self.vbox.pack_start(self.button_r1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r3, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 5)
		
		self.win.show_all()
	def tog(self, widget, data=None):
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return gtk.main_quit()
	def main(self):
		gtk.main()

if __name__ == "__main__":
	second = SecondWin()
	second.main()
