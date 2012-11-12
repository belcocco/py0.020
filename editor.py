

#import gtk				#moduli per pygtk	
import gtk.glade
import pygtk
#from os import path		#altri moduli

#click del tasto 'X'
#window1
def on_window1_destroy(widget, data=None):
	gtk.main_quit()
	print "Exit"
#window2
def on_window2_destroy(widget, data=None):
	window2.destroy()
	print "Exit"

#funzioni riguardanti il click dei bottoni della finestra principale
def on_btnSave_clicked(widget, data=None):
	global content
	buffer = txvEditor.get_buffer()
	start, end = buffer.get_bounds()	
	content = buffer.get_text(start, end)
	window2.show()

def on_btnNew_clicked(widget, data=None):
	buffer = txvEditor.get_buffer()
	buffer.set_text("")
	print "Nuova editazione"
	
def on_btnQuit_clicked(widget, data=None):	
	gtk.main_quit()
	print "Quit"

#funzioni riguardanti il click dei bottoni della finestra di imput del nome file da salvare
def on_btnCancel_clicked(widget, data=None):
	window2.destroy()
	print "Cancel"
	
def on_btnSave2_clicked(widget, data=None):
	fname = entFile.get_text()
	if path.exists(fname):
		print "File already exsist"
	else:
		try:
			f1 = open(fname, "w")
			f1.write(content)
			f1.close()
			print "File saved succeffully"
		except:
			print "Cannot save the file"
	entFile.set_text(fname)
	window2.destroy()

#segnali
signals = {
	"on_window1_destroy":on_window1_destroy,		#window1
	"on_btnSave_clicked":on_btnSave_clicked,
	"on_btnNew_clicked":on_btnNew_clicked,
	"on_btnQuit_clicked":on_btnQuit_clicked,
	"on_window2_destroy":on_window2_destroy,		#window2
	"on_btnCancel_clicked":on_btnCancel_clicked,	
	"on_btnSave2_clicked":on_btnSave2_clicked	
}


#carica e mostra finestra
MainGlade = gtk.glade.XML("editor.glade")			#file glade
window1 = MainGlade.get_widget("window1")			#window1 e widget contenuti in essa
txvEditor = MainGlade.get_widget("txvEditor")
window2 = MainGlade.get_widget("window2")			#window2 ...
entFile = MainGlade.get_widget("entFile")

MainGlade.signal_autoconnect(signals)				#funzione che controlla gli eventi




if window1:
	window1.show()
	gtk.main()
