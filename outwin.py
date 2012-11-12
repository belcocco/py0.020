#import gtk.glade
#import pygtk
#Outwin.py finestre di appoggio per tutti gli input/output del terminale

#outwin1
def on_outwin1_destroy(widget, data=None):
	gtk.main_quit()
	print "Exit"
#outwin2
def on_outwin2_destroy(widget, data=None):
	outwin2.destroy()
	print "Exit"

#funzioni riguardanti il click dei bottoni della finestra principale
def on_btnSave_clicked(widget, data=None):
	global content
	buffer = txvEditor.get_buffer()
	start, end = buffer.get_bounds()	
	content = buffer.get_text(start, end)
	outwin2.show()

def on_btnNew_clicked(widget, data=None):
	buffer = txvEditor.get_buffer()
	buffer.set_text("")
	print "Nuova editazione"
	
def on_btnQuit_clicked(widget, data=None):	
	gtk.main_quit()
	print "Quit"

#funzioni riguardanti il click dei bottoni della finestra di imput del nome file da salvare
def on_btnCancel_clicked(widget, data=None):
	outwin2.destroy()
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
	outwin2.destroy()

#segnali
signals = {
	"on_outwin1_destroy":on_outwin1_destroy,		#outwin1
	"on_btnSave_clicked":on_btnSave_clicked,
	"on_btnNew_clicked":on_btnNew_clicked,
	"on_btnQuit_clicked":on_btnQuit_clicked,
	"on_outwin2_destroy":on_outwin2_destroy,		#outwin2
	"on_btnCancel_clicked":on_btnCancel_clicked,	
	"on_btnSave2_clicked":on_btnSave2_clicked	
}

