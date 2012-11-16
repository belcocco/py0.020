#!/usr/bin/python
# -*- coding: latin-1 -*-

# pygtk_studio.py
# Copyright (C) 2012 belcocco <belcocco@gmail.com>
# 
# pygtk-studio is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pygtk-studio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#Creato da: Belcocco
#Data:24-10-2012
#Descrizione: Bottoni per avviare varie attività
#
#import module
import pygtk, gtk
pygtk.require('2.0')
#import gtk.glade
import os, string, subprocess, sys
import ftplib
import gobject
import time
import string
import shutil
import tempfile
from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty

#Importa moduli dell'utente

#Dati fissi
blu = gtk.gdk.color_parse('#7885ff') 
verde = gtk.gdk.color_parse('#0E5023') 
rosso = gtk.gdk.color_parse('#C51111')    
ocra = gtk.gdk.color_parse('#D6D844')
marine = gtk.gdk.color_parse('#0BC7B3')

#Finestra principale con tutti i bottoni delle attività
class MainWin(gtk.Window):
    def __init__(self):
        super(MainWin, self).__init__()
        
        self.set_title("Main")
        self.set_size_request(120, 300)		#dimensione della finestra per 4 button (100,180)
#        self.set_size_request(1000, 480)
        self.set_position(gtk.WIN_POS_MOUSE)
        self.labelpres = gtk.Label("Questa e' un interfaccia che racchiude esempi riassuntivi di oggetti GTK+/pyGTK")
        self.modify_bg(gtk.STATE_NORMAL, verde)    

        self.connect("destroy", self.on_destroy)

        fixed = gtk.Fixed()

        git = gtk.Button("Git")
        git.connect("clicked", self.on_clicked_git)
        git.set_size_request(100, 40)
        fixed.put(git, 10, 10)

        ftp = gtk.Button("FTP")
        ftp.connect("clicked", self.on_clicked_ftp)
        ftp.set_size_request(100, 40)
        fixed.put(ftp, 10, 50)

        hack = gtk.Button("Hack")
        hack.connect("clicked", self.on_clicked_hack)
        hack.set_size_request(100, 40)
        fixed.put(hack, 10, 90)

        lista = gtk.Button("List")
        lista.connect("clicked", self.on_clicked_lista)
        lista.set_size_request(100, 40)
        fixed.put(lista, 10, 130)
        
        foto = gtk.Button("Foto")
        foto.connect("clicked", self.on_clicked_foto)
        foto.set_size_request(100, 40)
        fixed.put(foto, 10, 170)

        comando1 = gtk.Button("Comando1")
        comando1.connect("clicked", self.on_clicked_comando1)
        comando1.set_size_request(100, 40)
        fixed.put(comando1, 10, 210)

        autore = gtk.Button("Autore")
        autore.connect("clicked", self.on_clicked_autore)
        autore.set_size_request(100, 40)
        fixed.put(autore, 10, 250)

        self.add(fixed)
        
    def on_destroy(self, widget):
        gtk.main_quit()
        
    def on_clicked_git(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
        NameFileOut = ""
        GUI_git()						#si apre la finestra dell'applicazione
#       app.show_all()
#       gtk.main_quit()

    def on_clicked_ftp(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del ftp-button
        GUI_ftp()						#si apre la finestra dell'applicazione
#        app.show_all()
#       gtk.main_quit()

    def on_clicked_hack(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del hack-button
        GUI_hack()						#si apre la finestra dell'applicazione
#       gtk.main_quit()
#Da questo punto importa applicazioni fatte da altri
    def on_clicked_lista(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		print "PRIMA di lista"
		import lista
		print "DOPO lista"
#		app = ListaWin()
#		gtk.main_quit()

    def on_clicked_foto(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		print "PRIMA di rinomina_foto"
		GUI_foto()    #import rinomina_foto
		print "DOPO rinomina_foto"

    def on_clicked_comando1(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		import eseguicmd

    def on_clicked_autore(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
        app = Presentazione()						#si apre la finestra dell'applicazione
        app.Presentazione.show_all()
############## FAR DIVENTARE UNA DEF - Visualizza contenuto di un file ###########
#			f = open('clone.out')
#			lines = f.readlines()
#			f.close()
# 			for line in lines:
#				print line,
###################################################################################

#		gtk.main_quit()

class Presentazione:
    def __init__(self):
        self.Presentazione = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.Presentazione.set_title("belcocco")
        self.Presentazione.set_default_size(700,365)
        self.Presentazione.set_size_request(250, 150)
        self.Presentazione.set_position(gtk.WIN_POS_CENTER)
        self.Presentazione.connect("delete_event", self.delete_event)
        self.Presentazione.connect("destroy", self.destroy)

        self.Presentazione.button5 = gtk.Button("Linus")
        self.Presentazione.button5("Clicked", GUI_git)

        hbox = gtk.HBox(False, 0)
        hbox1 = gtk.HBox(False, 0) #<---
        vbox1 = gtk.VBox(False, 0)
        vbox2 = gtk.VBox(False, 0)
        vbox3 = gtk.VBox(False, 0) #<---
        self.img = gtk.Image()
        self.img.set_from_file('auto421x316.png')
        self.immbutton = gtk.Button()
        self.immbutton.add(self.img)
        self.immbutton.connect("clicked", self.immpres)
        self.immbuttonlbl1 = gtk.Label("e-mail: belcocco@gmail.com")
        self.immbuttonlbl2 = gtk.Label("e-mail: ramuff@gmail.com")
        vbox1.pack_start(self.immbutton, 10)
        vbox2.pack_start(self.immbuttonlbl1, 10)
        vbox3.pack_start(self.Presentazione.button5, 10) #<---

        hbox.pack_start(vbox1, False, False, 10)
        hbox.pack_start(vbox2, False, False, 10)
        hbox1.pack_start(vbox3, False, False, 10) #<---
        self.Presentazione.add(hbox)
        self.Presentazione.show_all()
 
    def immpres(self, widget):				#funzione contenente immagine utilizzata dalla presentazione
        self.immpres  = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.immpres.set_title("Linus")
        self.immpres.set_position(gtk.WIN_POS_CENTER)
        img = gtk.Image()
        img.set_from_file('torvalds-linus.jpeg')
        self.immpres.add(img)
        self.immpres.show_all()
    def delete_event(self, widget, event, data=None):
        return gtk.FALSE
    def destroy(self, widget, data=None):
        return #gtk.main_quit()
		
#Window per GitHub.com (Upload e Download Repository)
class GUI_git():
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Git")
#		self.win.set_default_size(200, 80)
		self.win.set_size_request(500, 460)		#dimensione della finestra per 4 button (100,180)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)
		self.win.modify_bg(gtk.STATE_NORMAL, blu)    

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

#		self.vbox = gtk.VBox()

#		self.vbox = gtk.VBox(gtk.TRUE, 3)
		self.vbox = gtk.VBox(gtk.TRUE, 10)
		self.win.add(self.vbox)
		self.vbox.show()

#ToggleButton per l'attività Clone (con il repo remoto)
		self.tog_button_clone = gtk.ToggleButton("CLONE")
		self.tog_button_clone.connect("clicked", self.tog_clone, "Download")
		self.vbox.pack_start(self.tog_button_clone, gtk.TRUE, gtk.TRUE, 5)
#Bottone Add
		self.button_add = gtk.Button("ADD")
		self.button_add.connect("clicked", self.tog_add, "Add")
		self.vbox.pack_start(self.button_add, gtk.TRUE, gtk.TRUE, 0)
#Bottone Log
		self.button_log = gtk.Button("LOG")
		self.button_log.connect("clicked", self.tog_log, "Log")
		self.vbox.pack_start(self.button_log, gtk.TRUE, gtk.TRUE, 0)
#Bottone Commit
		self.button_commit = gtk.Button("COMMIT")
		self.button_commit.connect("clicked", self.tog_commit, "Commit")
		self.vbox.pack_start(self.button_commit, gtk.TRUE, gtk.TRUE, 0)
#ToggleButton per l'attività Push (con il repo remoto)
		self.tog_button_push = gtk.ToggleButton("PUSH")
		self.tog_button_push.connect("clicked", self.tog_push, "Upload")
		self.vbox.pack_start(self.tog_button_push, gtk.TRUE, gtk.TRUE, 5)

#Spazio per controllare l'inserimento del comando (git clone, add, log, commit e push)
		self.entry1 = gtk.Entry(100)
		self.vbox.pack_start(self.entry1, gtk.TRUE, gtk.TRUE, 0)

#Bottone Esegui
		self.button_exec = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button_exec.connect("clicked", self.exec_git_cmd)
		self.vbox.pack_start(self.button_exec, gtk.TRUE, gtk.TRUE, 0)

#Spazio per gestire l'attività scelta (git clone, add, log, commit e push)
		self.entry2 = gtk.Entry(100)
		self.vbox.pack_start(self.entry2, gtk.TRUE, gtk.TRUE, 0)

#Spazio per gestire gli output-errori dell'attività scelta (git clone, add, log, commit e push)
		self.entry3 = gtk.Entry(100)
		self.vbox.pack_start(self.entry3, gtk.TRUE, gtk.TRUE, 0)

		self.win.show_all()

#Gestisce l'attività (clone, add, log, commit e push)
	def exec_git_cmd(self, widget):
		NameFileOut = ""
		CMD_git = self.entry1.get_text()
		print CMD_git
		if CMD_git == "git clone https://github.com/belcocco/py0.020.git &> clone.out":
			NameFileOut = "clone.out"
		if CMD_git == "git push https://github.com/belcocco/py0.020.git &> push.out":
			NameFileOut = "push.out"

		self.entry2.set_text("OK, tutto fatto !")   #Se NON si vede è perchè manca '&' alla fine del comando shell

		#Esegui comando della shell. Ciò che FUNZIONA MEGLIO. 
		proc = subprocess.Popen(CMD_git, shell=True) #, stdin=PIPE, stdout=PIPE, stderr=PIPE)
#		proc = subprocess.check_call(CMD_git, shell=True) #, stdin=PIPE, stdout=PIPE, stderr=PIPE)

		#Controlla se il comando è andato bene. SOLO POPEN !!!
		proc.wait()
		if NameFileOut != "":
			Outwin(NameFileOut)	#Visualizzazione della finestra degli errori
		print proc.returncode

########################### DA CANCELLARE #################
#		k = 0
#		str1 = ""		#non viene eseguito nessun ciclo FOR. Basta guardare se il file è VUOTO.
#		str2 = "Cloning into"
#		str3 = "not found: did you run git"
#		str4 = "fatal: HTTP request failed"
#		str5 = "fatal: Authentication failed"
#		strNR = 0
#		cmdFind = 'find . -name "clone.out" -print'    # Cerca nel file clone.out
###########################################################

		#Guarda se il comando git clone/push .... ha dato errrori
		if proc.returncode != 0:
			self.entry2.set_text("...terminato con ERRORE !")
			#C'E' ERRORE per INTERNET SCONNESSA, ma esiste già la dir del clonaggio?
			#Guarda se il file clone.out è vuoto 
			if os.stat(NameFileOut).st_size == 0:
				#Errore: il path di destinazione esiste già e non è una directory vuota."
				self.entry3.set_text("..terminato con ERRORE e con OUTPUT VUOTO (???)")



#Comando GIT CLONE
	def tog_clone(self, widget, data=None):
		NameFileOut = "clone.out"
		self.entry1.set_text("git clone https://github.com/belcocco/py0.020.git &> clone.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
#Comando GIT ADD
	def tog_add(self, widget, data=None):
		self.entry1.set_text("git add *")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT LOG
	def tog_log(self, widget, data=None):
		self.entry1.set_text("git log | grep studio")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT COMMIT
	def tog_commit(self, widget, data=None):
		self.entry1.set_text("git commit -m -----")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT PUSH
	def tog_push(self, widget, data=None):
		NameFileOut = "push.out"
		self.entry1.set_text("git push https://github.com/belcocco/py0.020.git &> push.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])

	
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()

class GUI_ftp():
	def __init__(self):
		print "----- GUI_ftp -------"
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("FTP")
		self.win.set_default_size(400,95)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.win.show_all()
		
######### FTP Client ############################
#		if __name__ == '__main__':
#		nick = raw_input('Nick:')
#		pwd = raw_input('Password:')
#		site = raw_input('Sito:')
#		obj = ClientFTP(site,nick,pwd)
#		while obj.online: #while True
#			command = raw_input('pyFTP >>> ')
#			obj.controlla_cmd(command)      
#################################################

 	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()
 
class GUI_hack:
	def __init__(self):
		print "----- GUI_hack -------"
		self.hackwin = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.hackwin.set_title("Hack")
		self.hackwin.set_default_size(400,95)
		self.hackwin.set_position(gtk.WIN_POS_CENTER)
		self.hackwin.set_resizable(gtk.TRUE)
		self.hackwin.set_border_width(10)

		self.hackwin.connect("delete_event", self.delete_event)
		self.hackwin.connect("destroy", self.destroy)

#		self.vbox = gtk.VBox()

		self.vbox = gtk.VBox(gtk.TRUE, 3)
		self.hackwin.add(self.vbox)
		self.vbox.show()

#		self.entry = gtk.Entry(100)
#		self.entry.set_text("git clone http://github.com/belcocco/py.git")
#		self.vbox.pack_start(self.entry, gtk.TRUE, gtk.TRUE, 0)
#		self.button = gtk.Button(None, gtk.STOCK_EXECUTE)
#		self.button.connect("clicked", self.changeText)
#		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 0)
#		self.hackwin.add(self.vbox)
#		self.hackwin.show_all()


		self.button_r1 = gtk.RadioButton(None, "primo", gtk.FALSE)
		self.button_r1.connect("toggled", self.tog, "primo")
		self.button_r2 = gtk.RadioButton(self.button_r1, "secondo")
		self.button_r2.connect("toggled", self.tog, "secondo")
		self.button_r3 = gtk.RadioButton(self.button_r1, "terzo")
		self.button_r3.connect("toggled", self.tog, "terzo")

		self.button_t1 = gtk.ToggleButton("primo toggle")
		self.button_t1.connect("toggled", self.tog, "primo toggle")
		self.button_t2 = gtk.ToggleButton("secondo toggle")
		self.button_t2.connect("toggled", self.tog, "secondo toggle")
		self.button_dl = gtk.Button("Download")
		self.button_dl.connect("clicked", self.tog, "Download")
		self.button_ul = gtk.Button("Upload")
		self.button_ul.connect("clicked", self.tog, "Upload")

		self.buttonQuit = gtk.Button(None, gtk.STOCK_QUIT)
		self.buttonQuit.connect("clicked", self.destroy)

		self.vbox.pack_start(self.button_r1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r3, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_dl, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_ul, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.buttonQuit, gtk.TRUE, gtk.TRUE, 5)
		
		self.hackwin.show_all()
	def changeText(self, widget):
		self.entry.set_text("Nuovo testo!")
	def tog(self, widget, data=None):
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()

class GUI_foto:
    def __init__(self):
        print "----- GUI_foto -------"
        self.chmod = True
        self.mov = True
        self.destinazione = os.path.expanduser("~")
        self.origine = self.destinazione
        self.photo_list = []
        self.movie_list = []
        self.fotowin = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.fotowin.set_title("Copia le tue foto")
        self.fotowin.set_position(gtk.WIN_POS_CENTER)
        self.fotowin.connect("delete_event", self.delete_event)
        self.fotowin.connect("destroy", self.destroy)
        self.fotowin.set_border_width(2)
        self.fotowin.show_all()
        self.fotowin.modify_bg(gtk.STATE_NORMAL, ocra)    

        self.tooltips = gtk.Tooltips()
        
        vbox = gtk.VBox(False, 2)
        self.fotowin.add(vbox)
        
        tabella = gtk.Table(3,2, False)
        vbox.pack_start(tabella, True, True, 2)

        label_file = gtk.Label("File di origine")
        tabella.attach(label_file, 0, 1, 0, 1, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        label_file.show()
        
        self.button_file = gtk.Button(self.origine)
        self.button_file.connect("clicked", self.select_files, None)
        self.tooltips.set_tip(self.button_file, "Clicca per selezionare le foto da rinominare")
        tabella.attach(self.button_file, 1, 2, 0, 1, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        self.button_file.show()

        label_file2 = gtk.Label("File di destinazione")
        tabella.attach(label_file2, 0, 1, 1, 2, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        label_file2.show()
        
        self.button_file2 = gtk.Button(self.destinazione)
        self.button_file2.connect("clicked", self.select_dir, None)
        self.tooltips.set_tip(self.button_file2, "Clicca per cambiare la directory di destinazione")
        tabella.attach(self.button_file2, 1, 2, 1, 2, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        self.button_file2.show()
        
        label = gtk.Label("Nome foto")
        tabella.attach(label, 0, 1, 2, 3, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        label.show()
        
        self.entry = gtk.Entry()
        self.entry.set_text("Foto")
        self.entry.select_region(0, len(self.entry.get_text()))
        tabella.attach(self.entry, 1, 2, 2, 3, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL, 2, 2)
        self.entry.show()
        self.tooltips.set_tip(self.entry, "Testo utilizzato per rinominare le foto")
        
        tabella.show()

        check_mod = gtk.CheckButton("Sistema i permessi")
        check_mod.set_active(True)
        check_mod.connect("toggled", self.callback_mod)

        check_mov = gtk.CheckButton("Copia i video")
        check_mov.set_active(True)
        check_mov.connect("toggled", self.callback_mov)
        
        check_box = gtk.HBox(False, 2)
        check_box.pack_start(check_mod, True, True, 2)
        check_box.pack_start(check_mov, True, True, 2)
        check_mod.show()
        check_mov.show()
        vbox.pack_start(check_box, True, True, 2)
        check_box.show()

        button_box = gtk.HBox(False, 2)
        
        self.button = gtk.Button(None, gtk.STOCK_APPLY)
        self.button.connect("released", self.rename_photos, None)
        button_box.pack_start(self.button, True, True, 2)
        self.button.show()
        
        button_quit = gtk.Button(None, gtk.STOCK_CLOSE)
        button_quit.connect_object("clicked", gtk.Widget.destroy, self.fotowin)
        button_box.pack_start(button_quit, True, True, 2)
        button_quit.show()
        
        vbox.pack_start(button_box, True, True, 2)
        button_box.show()
        
        separator = gtk.HSeparator()
        vbox.pack_start(separator, False, False, 2)
        separator.show()

        self.barra = gtk.ProgressBar()
        vbox.pack_start(self.barra, True, True, 2)
        self.barra.show()
        
        vbox.show()
        self.update_labels(self)
        self.entry.grab_focus()
        self.fotowin.show_all()

    def update_labels(self, widget, data=None):
        self.button_file2.set_label(self.destinazione)
        numero = len(self.photo_list)
        if self.mov:
            numero = numero+len(self.movie_list)
        self.button_file.set_label(self.origine + " - " + str(numero) + " file selezionati")
        ntot=0
        self.nfatti=0
        self.barra.set_fraction(0.0)
        self.barra.set_text("Nessuna operazione in esecuzione")

    def rename_photos(self, widget, data=None):
        if len(self.photo_list+self.movie_list) == 0:
            dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_WARNING, gtk.BUTTONS_CLOSE)
            dialog.set_markup("Selezionare dei file di origine prima di eseguire l'operazione")
            response = dialog.run()
            dialog.destroy()
            return 0

        titolo=self.entry.get_text()
        
        ntot=len(self.photo_list + self.movie_list)
        nfatti=0
        
        for i, v in enumerate(self.photo_list):
            stringa = titolo + " - " + str(i) + '.jpg'
            if self.origine == self.destinazione:
                os.rename(v, self.destinazione+"/"+stringa)
            else:
                shutil.copy2(v, self.destinazione+"/"+stringa)
            if self.chmod:
                os.chmod (self.destinazione+"/"+stringa, 0644)
            nfatti = nfatti+1
            self.barra.set_fraction(float(nfatti)/float(ntot))
            self.barra.set_text(str(nfatti) + " su " + str(ntot) + " completati")
            while gtk.events_pending():
                gtk.main_iteration()
        if self.mov:
            for i, v in enumerate(self.movie_list):
                stringa = titolo + " - " + str(i) + '.mov'
                if self.origine == self.destinazione:
                    os.rename(v, self.destinazione+"/"+stringa)
                else:
                    shutil.copy2(v, self.destinazione+"/"+stringa)
                if self.chmod:
                    os.chmod (self.destinazione+"/"+stringa, 0644)
                nfatti = nfatti+1
                self.barra.set_fraction(float(nfatti)/float(ntot))
                self.barra.set_text(str(nfatti) + " su " + str(ntot) + " completati")
                while gtk.events_pending():
                    gtk.main_iteration()

        self.photo_list=[]
        self.movie_list=[]
        self.update_labels(self)
        dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE)
        dialog.set_markup("Operazione terminata, forse con successo")
        response = dialog.run()
        dialog.destroy()
        return 0

    
    def select_dir(self, widget, data=None):
        filesel = gtk.FileChooserDialog("Seleziona directory", None, gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        filesel.set_select_multiple(False)
        filesel.set_current_folder(self.destinazione)
        filesel.set_default_response(gtk.RESPONSE_OK)

        response = filesel.run()
        if response == gtk.RESPONSE_OK:
            self.destinazione = filesel.get_filename()
        self.update_labels(self)
        filesel.destroy()
        self.entry.grab_focus()


    def select_files(self, widget, data=None):
        filesel = gtk.FileChooserDialog("Seleziona foto di origine", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        filesel.set_select_multiple(True)
        filter = gtk.FileFilter()
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.JPG")
        filter.add_pattern("*.mov")
        filter.add_pattern("*.MOV")
        filter.set_name("Immagini Jpeg / Video Mov")
        filesel.set_filter(filter)
        filesel.set_current_folder(self.origine)
        filesel.set_default_response(gtk.RESPONSE_OK)

        response = filesel.run()
        if response == gtk.RESPONSE_OK:
            lista = filesel.get_filenames()
            self.photo_list=[]
            self.movie_list=[]
            for i in lista:
                if i[-4:].lower() == '.jpg':
                    self.photo_list.append(i)
                if i[-4:].lower() == '.mov':
                    self.movie_list.append(i)
            self.photo_list.sort()
            self.movie_list.sort()
            for i in self.photo_list + self.movie_list:
                print i
            self.origine = filesel.get_current_folder()
        self.update_labels(self)
        filesel.destroy()
        self.entry.grab_focus()

    def callback_mod(self, widget, data=None):
        self.chmod = widget.get_active()

    def callback_mov(self, widget, data=None):
        self.mov = widget.get_active()
        self.update_labels(self)

    def delete_event(self, widget, event, data=None):
        print "Delete event occured"
        return False
###############
#    def destroy(self, widget, data=None):
#        print "Esco dal programma"
#        gtk.main_quit()
###############
    def destroy(self, widget, data=None):
        return #gtk.main_quit()

class ClientFTP(object):
        """Client FTP da linea di comando
           Funzioni:               Comandi associati         Parametri: 
              -Connessione              None                      site,nick,password
              -Disconnessione           None                      None
              -Lista File               LIST                      None
              -Ricerca File             SEARCH                    nome_file
              -Rinomina File            REN                       nome_file, directory, nuovoNome
              -Elimina File             DEL                       nome_file, directory
              -Download file            DW                        directory, filename, directory_di_uscita
              -Download all file        DWA                       directory_remota, filename, directory_uscita
              -Invio file               UPL                       nomeFile, directory_uscita 
              -Cambio directory         CD                        place,  nome
              -Informazione sulla
               directory locale/remota   LD->Local Directory      None
                                         RD->Remote Directory
              """
        def __init__(self,site ,nick, pwd):
                self.online = None
                self.comandi = ['RD', 'LD', 'CD', 'DW','DWA','LIST','SEARCH','REN','DEL','UPL','QUIT','HELP','INFO']
                self.site = site
                self.nick = nick
                self.pwd = pwd
                self.user = self.connection(self.site,self.nick,self.pwd)

        def connection(self,site,nick,pwd):
                """Comando: None    Parametri: Site, nick, password
                   Compito: Si connette al server alla porta:21 in modalità passiva"""
                try:
                        user = ftplib.FTP(site,nick,pwd)
                        self.online = True
                        print user.getwelcome()
                        return user 
                except ftplib.all_errors,error:
                        print '[FATAL]Connessione fallita!\n %s' %(error)
                        self.online = False
                        return None  #self.user = None
                        
        
        def disconnect(self):
                """Si disconnette dal server e termina il programma"""
                self.user.quit()
                self.online = False
                sys.exit('Programma terminato')

        def local_directory(self):
                """Comando: LD    Parametri: None
                   Computo: restiruisce informazioni sulla directory locale corrente"""
                print 'Direcory locale corrente: %s' %(os.getcwd())
        
        def remote_directory(self):
                """Comando: RD   Parametri: None
                   Compito: Restituisce informazioni sulla directory remota corrente"""
                print 'Directory remota corrente: %s' %(self.user.pwd())
        
        def change_directory(self,place,path):
                """Comando CD Parametri: place (Valori possibili: R,L.R = remoto,L = locale. path(Nome della nuova directory)
                   Compito: Cambio directory """
                if place.upper() == 'R':
                        try:
                                self.user.cwd(path)
                                print 'Directory remota cambiata in : %s' %(self.user.pwd())
                                return True
                        except ftplib.all_errors ,e:
                                print '[!!]%s' %(e) 
                elif place.upper() == 'L':
                        try:
                                os.chdir(path)
                                print 'Directory locale cambiata in: %s' %(os.getcwd())
                                return True
                        except os.error,e:
                                print '[!!]%s' %(e) 
                else:
                        print 'Error, place non supportato!\nPlace supportati: R,L\nR = remote\nL = local'
                        return False

        def search_file(self,filename,directory):
                """Comando: Search        Parametri: filename, directory
                   Compito: Cerca un file"""
                try:
                        self.change_directory('R',directory)
                        list_file = self.user.mlsd(facts=['type','size'])
                        _file=[x for x in list_file if filename in x]
                        if _file == []:
                                print '[!!]File %s non trovato!' %(filename)
                                return False
                        else:
                                print _file
                                return True
                except ftplib.error_temp,e:
                        print '[ERROR]%s'%(e)
                        print 'Connessione...'
                        self.user.connect(self.site)
                        self.user.login(self.nick,self.pwd)
                        
                        
        
        def download(self,directory,filename,directory_uscita = os.getcwd(),from_all_file = False):
                """Comando: DW  Parametri: Directory(Directory  remota del file), filename(nome del file remoto), directory_uscita(Directory locale dove verrà salvato il file.
                                                                                                                    il valore predefinito è la directory corrente)
                   Compito: Scarica un file dal server"""
                try:
                        if from_all_file:
                                file_remoto = open(filename,'wb')
                                self.user.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
                                file_remoto.close()
                                print 'Scaricato in %s' %(os.getcwd())
                        else:
                                if self.search_file(filename,directory):
                                        file_remoto = open(filename,'wb')
                                        self.user.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
                                        file_remoto.close()
                                        print 'Scaricato in %s' %(os.getcwd())
                                else:
                                        print '[!!]File %s non trovato!' %(filename)
                except ftplib.error_perm as e:
                        file_remoto.close()
                        print '[ERROR] %s' %(e) #Error 500-599
                        os.remove(filename)
                        print 'Download interrotto'
                except IOError as e:
                        print '[ERROR]%s' %(e)
                        print '[!!]Sintassi corretta del comando DW: DW directory_remoto file_remoto directory_uscita esempio: DW / favicon.ico C:\Users\normal_user\Desktop'
                        print 'Per maggiori informazioni usare il comando HELP'
                        
                    
        def download_all_file(self,directory_remota,directory_uscita = os.getcwd()):
                """Comando: DWA Parametri: directory_remota, directory_uscita

                   Compito: prende tutti i nomi di file di directory_remota e li scarica uno ad uno tramite il metodo download nella cartella d'uscita"""
                try:
                        self.change_directory('R',directory_remota)
                        for x in self.user.mlsd(facts = ['type']):
                                if x[1]['type'] == 'file':
                                        self.download(directory_remota, x[0], directory_uscita)
                except ftplib.error_perm as e:
                        print '[ERROR] %s' %(e) #Error 500-599
                except ftplib.error_temp as e:
                        print '[ERROR] %s' %(e) #Error 400-499
                        
                
        def lista_file(self):
                """Comando: LIST    Parametri: //
                   Compito: Stampa la lista di file nella directory remota corrente"""
                try:
                        list_file = self.user.mlsd(facts=['type','size'])
                        files = []
                        for x in list_file:
                                files.append(x.strip('),('))
                        for x in files:
                                print x
                                print
                                
                except ftplib.error_temp,e:
                        print '[ERROR]%s'%(e)
                        print 'Connessione...'
                        self.user.connect(self.site)
                        self.user.login(self.nick,self.pwd)

        
        def rename_file(self,filename,directory,nuovoNome):
                """Comando:REN         Paramentri: filename, directory, nuovoFile
                   Compito:Rinominare un file"""

                if self.search_file(filename,directory):
                        self.user.rename(filename,nuovoName)
                        print 'File: %s cambiato in: %s' %(filename,nuovoNome)
                        return True
                else:
                        print '[!!]Nessuna corrispondenza trovata!'
                        return False

        def delete_file (self,filename,directory):
                if self.search_file(filename,directory):
                        self.user.delete(filename)
                        print 'File %s cancellato!' %(filename)
                else:
                        print '[!!]File non trovato'
                        
                
        def upload(self,filename,directory_uscita):
                """Comando: UPL    Parametri: nameFile(Nome del file con relativo percorso), directory_uscita(Directory remota di uscita.
                   Compito: Invia un file al server                                          Il valore predefinito è la directory remota corrente).
                 """
                try:
                        self.change_directory('R',directory_uscita)
                        file_locale = open(filename,'rb')
                        self.user.storbinary('STOR %s' %(str(filename)), file_locale)
                        print 'File inviato in %s' %(self.user.pwd())
                except ftplib.error_perm,e:
                        print '[ERROR] %s' %(e)
                except IOError,e:
                        print '[ERROR]%s' %(e)
                        print '[!!]Sintassi corretta del comando UPL: UPL  file_remoto directory_uscita esempio: UPL  favicon.ico C:\Users\normal_user\Desktop\Eggs'
        
        def controlla_cmd(self,comando):
                """Controlla se il  comando è valido"""
                comando = comando.split()
                comando_trovato = False
                for x in comando:
                        if x.upper() in self.comandi:
                                comando_trovato = True
                                cmd = x.upper()
                                self.avvia_cmd(cmd,[y for y in comando if y != x])
                                break
                        else:
                                continue
                if not comando_trovato:
                        print 'Usare help per una lista completa dei comandi'

                
        def avvia_cmd(self,cmd, argv):
                """Avvia il comando passato come parametro"""
                argv =  list(argv)
                numero_parametri = len(argv)
                if cmd == self.comandi[0]:
                        self.remote_directory()
                elif cmd == self.comandi[1]:
                        self.local_directory()
                elif cmd == self.comandi[2]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri insufficenti!\nSintassi corretta: CD R NomeDirectory. CD L NomeDirectory.R=remote, L = Local.\nPer maggiori info usare il comando HELP\n'
                                return False
                        else:
                                self.change_directory(argv[0],argv[1])
                elif cmd == self.comandi[3]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                                return False
                        elif numero_parametri < 3:
                                print '[!!]Attenzione non è stata specificata la directory di uscita.Il file verrà salvato nelle directory corrente'
                                self.download(argv[0],argv[1])                                
                        else:
                                self.download(argv[0],argv[1],argv[2])
                elif cmd == self.comandi[4]:
                        if numero_parametri < 1:
                                print '[ERROR]Parametri non sufficienti'
                        elif numero_parametri < 2:
                                print '[!!]Attenzione non è stata specificata la directory di uscita.I files verranno salvati nelle directory corrente'
                                self.download_all_file(argv[0])
                        else:
                                self.download_all_file(argv[0],argv[1])
                elif cmd == self.comandi[5]:
                        self.lista_file()
                elif cmd == self.comandi[6]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.search_file(argv[0],argv[1])
                elif cmd == self.comandi[7]:
                        if numero_parametri < 3:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.rename_file(argv[0],argv[1],argv[2])
                elif cmd ==  self.comandi[8]:
                        if numero_parametri < 2:
                                print'[ERROR]Parametri non sufficienti'
                        else:
                                self.delete_file(argv[0],argv[1])
                elif cmd == self.comandi[9]:                                        
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.upload(argv[0],argv[1])
                elif cmd == self.comandi[10]:
                        self.disconnect()
                elif cmd == self.comandi[11]:
                        help(Client)
                elif cmd == self.comandi[12]:
                        self.info()

class Outwin():
    def __init__(self, NameFileOut):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect("destroy", self.destroy)
        window.set_title("Output dei comandi")
        window.set_border_width(0)
        window.modify_bg(gtk.STATE_NORMAL, rosso)    

        box1 = gtk.VBox(False, 0)
        window.add(box1)
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()

        box2.pack_start(sw)
        # Carica il file generato dal comando git relativo ai messaggi di errore ecc.
#        infile = open("clone.out", "r")
        infile = open(NameFileOut, "r")

        if infile:
            string = infile.read()
            infile.close()
            textbuffer.set_text(string)

        hbox = gtk.HButtonBox()
        box2.pack_start(hbox, False, False, 0)
        hbox.show()

        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        # check button to toggle editable mode
        check = gtk.CheckButton("Editable")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_editable, textview)
        check.set_active(True)
        check.show()
        # check button to toggle cursor visiblity
        check = gtk.CheckButton("Cursor Visible")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_cursor_visible, textview)
        check.set_active(True)
        check.show()
        # check button to toggle left margin
        check = gtk.CheckButton("Left Margin")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_left_margin, textview)
        check.set_active(False)
        check.show()
        # check button to toggle right margin
        check = gtk.CheckButton("Right Margin")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_right_margin, textview)
        check.set_active(False)
        check.show()
        # radio buttons to specify wrap mode
        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        radio = gtk.RadioButton(None, "WRAP__NONE")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_NONE)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__CHAR")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_CHAR)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__WORD")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_WORD)
        radio.show()

        # radio buttons to specify justification
        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        radio = gtk.RadioButton(None, "JUSTIFY__LEFT")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_LEFT)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__RIGHT")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_RIGHT)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__CENTER")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_CENTER)
        radio.show()

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

#        button = gtk.Button("Chiudi")
#        button.connect("clicked", self.destroy)
#        box2.pack_start(button, True, True, 0)
#        button.set_flags(gtk.CAN_DEFAULT)
#        button.grab_default()
#        button.show()
        window.show()

    def toggle_editable(self, checkbutton, textview):
        textview.set_editable(checkbutton.get_active())

    def toggle_cursor_visible(self, checkbutton, textview):
        textview.set_cursor_visible(checkbutton.get_active())

    def toggle_left_margin(self, checkbutton, textview):
        if checkbutton.get_active():
            textview.set_left_margin(50)
        else:
            textview.set_left_margin(0)

    def toggle_right_margin(self, checkbutton, textview):
        if checkbutton.get_active():
            textview.set_right_margin(50)
        else:
            textview.set_right_margin(0)

    def new_wrap_mode(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_wrap_mode(val)

    def new_justification(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_justification(val)

    def destroy(self, widget):
        return #gtk.main_quit()

######## MAIN LOOP ########################
#Questa è la finestra principale con i bottoni per startare le attività.
#Si chiude con la 'X' in alto a destra 
startMainWin = MainWin()
startMainWin.show_all()

######### FTP Client ############################
#if __name__ == '__main__':
#        nick = raw_input('Nick:')
#        pwd = raw_input('Password:')
#        site = raw_input('Sito:')
#        obj = ClientFTP(site,nick,pwd)
#        while obj.online: #while True
#                command = raw_input('pyFTP >>> ')
#                obj.controlla_cmd(command)      
#################################################

gtk.main()
