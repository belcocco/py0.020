#!/usr/bin/python
# -*- coding: utf-8 -*-

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
import pango
from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty

#Importa moduli dell'utente

#Dati fissi
blu = gtk.gdk.color_parse('#413EDC') 
verde = gtk.gdk.color_parse('#1FCC3F') 
rosso = gtk.gdk.color_parse('#C51111')    
ocra = gtk.gdk.color_parse('#D6D944')
marine = gtk.gdk.color_parse('#0BC7B3')
giallo = gtk.gdk.color_parse('#FFFF00')
carota = gtk.gdk.color_parse('#FC9060')
marine = gtk.gdk.color_parse('#2BC4E3')
	#Pango
fg_color = pango.AttrForeground(65565, 0, 0, 0, 6)
underline = pango.AttrUnderline(pango.UNDERLINE_DOUBLE, 7, 11)
bg_color = pango.AttrBackground(40000, 40000, 40000, 12, 19)
strike = pango.AttrStrikethrough(True, 20, 29)
size = pango.AttrSize(20000, 0, -1)
	#Testi vari
txt_clone = "CLONE"
txt_push = "PUSH"
testtext = "Ti sì che te se un hom, minga tò surela!"
clonetext = "git clone https://github.com/belcocco/py0.020.git &> clone.out" 
pushtext = "git push https://github.com/belcocco/py0.020.git master &> push.out"
txt_site_default = "localhost"
txt_uname_default = "raga"
txt_pswd_default = "ragamuz"
#txt_site_default = "na.mirror.garr.it"
#txt_uname_default = "anonymous"
#txt_pswd_default = ""

#
#site = "localhost"
#nick = "raga"
#pswd = "ragamuz"
#site = "na.mirror.garr.it"
#nick = "anonymous"
#pswd = ""

objru = unicode(u'''Фёдор Михайлович Достоевский родился 30 октября (11 ноября)
1821 года в Москве. Был вторым из 7 детей. Отец, Михаил Андреевич, 
работал вгоспитале для бедных. Мать, Мария Фёдоровна 
(в девичестве Нечаева), происходила из купеческого рода.''')
ftp_help = unicode(u"""Client FTP da linea di comando (Tutti i comandi posso essere scritti in minuscolo)
           Dopo aver avviato servono 'site' 'nick' e 'password' per attivare la 'Connessione'
           Funzioni:               Comandi associati         esempio: 

           -Directory locale         LD                        ld     (si vede dove punta)
           -Directory remota         RD                        rd     (si vede dove punta)
           -Cambio directory locale  CD                        cd l /nome_da_aggiungere_al_path_di_ld
           -Cambio directory remota  CD                        cd r /nome_da_aggiungere_al_path_di_rd
           -Lista File               LIST                      list
           -Ricerca File             SEARCH                    search nome_file
           -Rinomina File            REN                       ren nome_file dir nuovo_mome_file
           -Elimina File             DEL                       del nome_file dir
           -Download file            DW                        dw dir_remota filename dir_locale_di_uscita(_che può essere omessa)
           -Download all file        DWA                       dwa dir_remota filename dir_locale_di_uscita(_che può essere omessa)
           -Invio file               UPL                       upl nome_file dir_remota_di_uscita 
                 -
           -Disconnessione           QUIT                      quit

            N.B.: DW e UPL cambiano automaticamente le dir di destinazione
                  se differiscono dal puntamento (ld, rd) di prima del comando.""")
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

        attvarwin = gtk.Button("Attività Varie")
        attvarwin.connect("clicked", self.on_clicked_attvarwin)
        attvarwin.set_size_request(100, 40)
        fixed.put(attvarwin, 10, 130)
        
        foto = gtk.Button("Foto")
        foto.connect("clicked", self.on_clicked_foto)
        foto.set_size_request(100, 40)
        fixed.put(foto, 10, 170)

        comando1 = gtk.Button("Pango")
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

    def on_clicked_attvarwin(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		print "PRIMA di Attività varie"
		Attvarwin()
		print "DOPO Attività varie"
#		gtk.main_quit()

    def on_clicked_foto(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		print "PRIMA di rinomina_foto"
		GUI_foto()    #import rinomina_foto
		print "DOPO rinomina_foto"

    def on_clicked_comando1(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		PangoApp1()
		PangoApp2()
#		import eseguicmd

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


        hbox = gtk.HBox(False, 0)
        vbox1 = gtk.VBox(False, 0)
        vbox2 = gtk.VBox(False, 0)
        self.img = gtk.Image()
        self.img.set_from_file('auto421x316.png')
        self.immbutton = gtk.Button()
        self.immbutton.add(self.img)
        self.immbutton.connect("clicked", self.immpres)
        self.immbuttonlbl1 = gtk.Label("e-mail: belcocco@gmail.com")
        self.immbuttonlbl2 = gtk.Label("e-mail: ramuff@gmail.com")
        vbox1.pack_start(self.immbutton, 10)
        vbox2.pack_start(self.immbuttonlbl1, 10)

        hbox.pack_start(vbox1, False, False, 10)
        hbox.pack_start(vbox2, False, False, 10)
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
		self.tog_button_clone = gtk.ToggleButton(txt_clone)
		self.tog_button_clone.connect("clicked", self.tog_clone, "Download")
		self.vbox.pack_start(self.tog_button_clone, gtk.TRUE, gtk.TRUE, 5)
#Bottone Add
		self.button_add = gtk.Button("ADD")
		self.button_add.connect("clicked", self.tog_add, "Add")
		self.vbox.pack_start(self.button_add, gtk.TRUE, gtk.TRUE, 0)
#Bottone Status
		self.button_status = gtk.Button("STATUS")
		self.button_status.connect("clicked", self.tog_status, "Status")
		self.vbox.pack_start(self.button_status, gtk.TRUE, gtk.TRUE, 0)
#Bottone Log
		self.button_log = gtk.Button("LOG")
		self.button_log.connect("clicked", self.tog_log, "Log")
		self.vbox.pack_start(self.button_log, gtk.TRUE, gtk.TRUE, 0)
#Bottone Commit
		self.button_commit = gtk.Button("COMMIT")
		self.button_commit.connect("clicked", self.tog_commit, "Commit")
		self.vbox.pack_start(self.button_commit, gtk.TRUE, gtk.TRUE, 0)
#ToggleButton per l'attività Push (con il repo remoto)
		self.tog_button_push = gtk.ToggleButton(txt_push)
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
		self.entry2.set_text(" ")
		self.entry3.set_text(" ")
		CMD_git = self.entry1.get_text()
		print CMD_git
		if CMD_git == clonetext: #"git clone https://github.com/belcocco/py0.020.git &> clone.out":
			NameFileOut = "clone.out"
		elif CMD_git == pushtext: #"git push https://github.com/belcocco/py0.020.git master &> push.out":
			NameFileOut = "push.out"
		elif NameFileOut != "clone.out" or NameFileOut != "push.out":
			NameFileOut = "git.out"
		self.entry2.set_text("OK, tutto fatto !")   #Se NON si vede è perchè manca '&' alla fine del comando shell

		#Esegui comando della shell. Ciò che FUNZIONA MEGLIO. 
#		proc = subprocess.check_call(CMD_git, shell=True) #, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		proc = subprocess.Popen(CMD_git, shell=True) #, stdin=PIPE, stdout=PIPE, stderr=PIPE)

		#Aspetta la fine del comando. SOLO POPEN !!!
		proc.wait()

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
		print NameFileOut
		if proc.returncode != 0:
			self.entry2.set_text("...terminato con ERRORE !")
			#C'E' ERRORE per INTERNET SCONNESSA, ma esiste già la dir del clonaggio?
			#Guarda se il file clone.out è vuoto 
			if os.stat(NameFileOut).st_size == 0:
				#Errore: il path di destinazione esiste già e non è una directory vuota."
				self.entry3.set_text("..terminato con ERRORE e con OUTPUT VUOTO (???)")
		elif CMD_git == clonetext:
			self.entry3.set_text("Clone eseguito con SUCCESSO in LOCALE")
		elif CMD_git == pushtext:
			self.entry3.set_text("Push eseguito con SUCCESSO sul repository di GITHUB")
#		if NameFileOut != "":
		Outwin(NameFileOut)	#Visualizzazione della finestra degli output del comando git
		print proc.returncode
		
#Comando GIT CLONE
	def tog_clone(self, widget, data=None):
#		NameFileOut = "clone.out"
		self.entry1.set_text(clonetext) #"git clone https://github.com/belcocco/py0.020.git &> clone.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
#Comando GIT ADD
	def tog_add(self, widget, data=None):
#		NameFileOut = "git.out"
		self.entry1.set_text("git add * &> git.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT STATUS
	def tog_status(self, widget, data=None):
#		NameFileOut = "git.out"
		self.entry1.set_text("git status &> git.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
##Comando GIT LOG
	def tog_log(self, widget, data=None):
#		NameFileOut = "git.out"
		self.entry1.set_text("git log | grep studio &> git.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT COMMIT
	def tog_commit(self, widget, data=None):
#		NameFileOut = "git.out"
		self.entry1.set_text("git commit -m ----- &> git.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
#Comando GIT PUSH
	def tog_push(self, widget, data=None):
#		NameFileOut = "push.out"
		self.entry1.set_text(pushtext) #"git push https://github.com/belcocco/py0.020.git &> push.out")
		self.entry2.set_text("")
		self.entry3.set_text("")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])

	
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()

class GUI_ftp():
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("FTP")
		self.win.set_default_size(400,295)
		self.win.set_position(gtk.WIN_POS_CENTER_ALWAYS)   #CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)
		self.win.modify_bg(gtk.STATE_NORMAL, carota)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)
		self.win.show_all()

############## Inserire gli pggetti
		self.vbox = gtk.VBox(gtk.TRUE, 10)
		self.win.add(self.vbox)
		self.vbox.show()


#Label e spazio per controllare l'inserimento del comando indirizzo server
		self.frame1 = gtk.Frame("")
		self.labelcent1 = gtk.Label("Sito Server FTP")
#		fg_color_Att = pango.AttrForeground(65535, 0, 0, 0, 1000)
#		size_Att = pango.AttrSize(20000, 0, -1)
		attr = pango.AttrList()
		attr.insert(fg_color)
		attr.insert(size)
		self.labelcent1.set_attributes(attr)
		self.vbox.pack_start(self.frame1, gtk.TRUE, gtk.TRUE, 0)
		self.frame1.add(self.labelcent1)

		self.entry1 = gtk.Entry(100)
		self.vbox.pack_start(self.entry1, gtk.TRUE, gtk.TRUE, 0)
#Label e spazio per per controllare l'inserimento del comando username
		self.frame2 = gtk.Frame("")
		self.labelcent2 = gtk.Label("Nome Utente")
#		fg_color_Att = pango.AttrForeground(65535, 0, 0, 0, 1000)
#		size_Att = pango.AttrSize(20000, 0, -1)
		attr = pango.AttrList()
		attr.insert(fg_color)
		attr.insert(size)
		self.labelcent2.set_attributes(attr)
		self.vbox.pack_start(self.frame2, gtk.TRUE, gtk.TRUE, 0)
		self.frame2.add(self.labelcent2)
		self.entry2 = gtk.Entry(100)
		self.vbox.pack_start(self.entry2, gtk.TRUE, gtk.TRUE, 0)
#Label e spazio per per controllare l'inserimento del comando password
		self.frame3 = gtk.Frame("")
		self.labelcent3 = gtk.Label("Password")
#		fg_color_Att = pango.AttrForeground(65535, 0, 0, 0, 1000)
#		size_Att = pango.AttrSize(20000, 0, -1)
		attr = pango.AttrList()
		attr.insert(fg_color)
		attr.insert(size)
		self.labelcent3.set_attributes(attr)
		self.vbox.pack_start(self.frame3, gtk.TRUE, gtk.TRUE, 0)
		self.frame3.add(self.labelcent3)
		self.entry3 = gtk.Entry(100)
		self.vbox.pack_start(self.entry3, gtk.TRUE, gtk.TRUE, 0)
#Bottone Esegui
		self.button_exec = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button_exec.connect("clicked", self.prova_connessione)
		self.vbox.pack_start(self.button_exec, gtk.TRUE, gtk.TRUE, 0)

#Visualizza le varie stringe per la connessione
		self.entry1.set_text(txt_site_default)
		self.entry2.set_text(txt_uname_default)
		self.entry3.set_visibility(False)
		self.entry3.set_invisible_char('*')
		self.entry3.set_text(txt_pswd_default)
		
		self.win.show_all()

	def prova_connessione(self, widget):
		self.online = None
#		self.comandi = ['RD', 'LD', 'CD', 'DW','DWA','LIST','SEARCH','REN','DEL','UPL','QUIT','HELP','INFO']
		self.site = self.entry1.get_text()
		self.nick = self.entry2.get_text()
		self.pswd = self.entry3.get_text()
		self.ftp = self.connessione(self.site,self.nick,self.pswd)
#		self.online = None
#		self.comandi = ['RD', 'LD', 'CD', 'DW','DWA','LIST','SEARCH','REN','DEL','UPL','QUIT','HELP','INFO']
#		while self.online:
#			Comandi_FTP(Welcome_site) # Su questa classe c'è TUTTO il peso del ClientFTL
#			print "CICCIA"
			
	def connessione(self,site,nick,pswd):
		"""Comando: None    Parametri: Site, nick, password
		Compito: Si connette al server alla porta:21 in modalità passiva"""
		try:
			ftp = ftplib.FTP(site,nick,pswd)
			Errore_connessione = False 
			self.online = True
			print ftp.getwelcome()
			Stato_server = ftp.getwelcome()
			Comandi_FTP(Stato_server, Errore_connessione)

			return ftp 
		except ftplib.all_errors,error:
			Errore_connessione = True
			Stato_server = "[FATAL ERROR]Connessione fallita!"
			Comandi_FTP(Stato_server, Errore_connessione)
			print '[FATAL ERROR]Connessione fallita!\n %s ' %(error)
			self.online = False
			return None  #self.ftp = None

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

class Outwin():
    def __init__(self, NameFileOut):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect("destroy", self.destroy)
        window.set_title("Output dei comandi")
        window.set_size_request(600, 460)		#dimensione della finestra per 4 button (100,180)
        window.set_border_width(0)
        window.modify_bg(gtk.STATE_NORMAL, giallo)    

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

class Comandi_FTP(): 
	#Stato_server = stringa di welcome oppure stringa d'errore
	#Errore_connessione = TRUE (se c'è errore) oppure FALSE (se non c'è)
	def __init__(self, Stato_server, Errore_connessione):  
#Label e spazio per controllare l'inserimento del comando indirizzo server
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Connessione FTP")
#		self.win.set_default_size(200, 80)
		self.win.set_size_request(500, 460)		#dimensione della finestra per 4 button (100,180)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)
		self.win.modify_bg(gtk.STATE_NORMAL, marine)    

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

#		self.vbox = gtk.VBox()

#		self.vbox = gtk.VBox(gtk.TRUE, 3)
		self.vbox = gtk.VBox(gtk.TRUE, 10)
		self.win.add(self.vbox)
		self.vbox.show()

#Frame con la risposta del server a connessione avvenuta
		if Errore_connessione == False:
			self.frame1 = gtk.Frame("Il Server è collegato ed ha risposto:")
		else:
			self.frame1 = gtk.Frame("Il Server NON risponde")
		
		self.labelcent1 = gtk.Label(Stato_server)
#		fg_color_Att = pango.AttrForeground(65535, 0, 0, 0, 1000)
#		size_Att = pango.AttrSize(20000, 0, -1)
		attr = pango.AttrList()
		attr.insert(fg_color)
		attr.insert(size)
		self.labelcent1.set_attributes(attr)
		self.vbox.pack_start(self.frame1, gtk.TRUE, gtk.TRUE, 0)
		self.frame1.add(self.labelcent1)

#Spazio entry0 di riserva
#		self.entry0 = gtk.Entry(100)
#		self.vbox.pack_start(self.entry0, gtk.TRUE, gtk.TRUE, 0)


#Spazio per controllare l'inserimento del comando 
		self.entry1 = gtk.Entry(100)
		self.vbox.pack_start(self.entry1, gtk.TRUE, gtk.TRUE, 0)

#Bottone Esegui
		self.button_exec_ftp_cmd = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button_exec_ftp_cmd.connect("clicked", self.exec_ftp_cmd)
		self.vbox.pack_start(self.button_exec_ftp_cmd, gtk.TRUE, gtk.TRUE, 0)

#Spazio per gestire una attività (RISERVA)
		self.entry2 = gtk.Entry(100)
		self.vbox.pack_start(self.entry2, gtk.TRUE, gtk.TRUE, 0)

#Spazio per gestire una attività (RISERVA)
		self.entry3 = gtk.Entry(100)
		self.vbox.pack_start(self.entry3, gtk.TRUE, gtk.TRUE, 0)

#Visualizza prompt: ClientFTP>>>
		self.entry1.set_text("ClientFTP>>>")
		self.win.show_all()


#Gestisce i comandi 
	def exec_ftp_cmd(self, widget):
		self.online = True
		self.comandi = ['RD', 'LD', 'CD', 'DW','DWA','LIST','SEARCH','REN','DEL','UPL','QUIT','HELP','INFO']
		print "BoH"
		while self.online:
#			command = raw_input('ClientFTP >>> ')
			command = self.entry1.get_text()
			print "PAPERA"
			self.controlla_cmd(command)
			


############################################################################
#		NameFileOut = ""
#		self.entry2.set_text(" ")
#		self.entry3.set_text(" ")
############################################################################                        
        
	def disconnect(self):
		"""Si disconnette dal server e termina il programma"""
		self.ftp.quit()
		self.online = False
		sys.exit('Programma terminato')

	def local_directory(self):
 		"""Comando: LD    Parametri: None
		Computo: restiruisce informazioni sulla directory locale corrente"""
		print 'Direcory locale corrente: %s' %(os.getcwd())
        
	def remote_directory(self):
		"""Comando: RD   Parametri: None
		Compito: Restituisce informazioni sulla directory remota corrente"""
		print 'Directory remota corrente: %s' %(self.ftp.pwd())
        
	def change_directory(self,place,path):
		"""Comando CD Parametri: place (Valori possibili: R,L.R = remoto,L = locale. path(Nome della nuova directory)
		Compito: Cambio directory """
		if place.upper() == 'R':
			try:
				self.ftp.cwd(path)
				print 'Directory remota cambiata in : %s' %(self.ftp.pswd())
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
			list_file = self.ftp.mlsd(facts=['type','size'])
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
				self.ftp.connect(self.site)
				self.ftp.login(self.nick,self.pswd)
                        
                        
        
	def download(self,directory,filename,directory_uscita = os.getcwd(),from_all_file = False):
		"""Comando: DW  Parametri: Directory(Directory  remota del file), filename(nome del file remoto), directory_uscita(Directory locale dove verrà salvato il file.
		il valore predefinito è la directory corrente)
		Compito: Scarica un file dal server"""
		try:
			if from_all_file:
				file_remoto = open(filename,'wb')
				self.ftp.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
				file_remoto.close()
				print 'Scaricato in %s' %(os.getcwd())
			else:
				if self.search_file(filename,directory):
					file_remoto = open(filename,'wb')
					self.ftp.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
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
			for x in self.ftp.mlsd(facts = ['type']):
				if x[1]['type'] == 'file':
					self.download(directory_remota, x[0], directory_uscita)
		except ftplib.error_perm as e:
			print '[ERROR] %s' %(e) #Error 500-599
		except ftplib.error_temp as e:
			print '[ERROR] %s' %(e) #Error 400-499
                        
                
	def lista_file(self):
		"""Comando: LIST    Parametri: //
		Compito: Stampa la lista di file nella directory remota corrente
		try:
			list_file = self.ftp.mlsd(facts=['type','size'])
			files = []
			for x in list_file:
				files.append(x.strip('),('))
			for x in files:
				print x
				print
                                
		except ftplib.error_temp,e:
			print '[ERROR]%s'%(e)
			print 'Connessione...'
			self.ftp.connect(self.site)
 			self.ftp.login(self.nick,self.pswd)"""
		self.ftp.retrlines('LIST')
        
	def rename_file(self,filename,directory,nuovoNome):
		"""Comando:REN         Paramentri: filename, directory, nuovoFile
		Compito:Rinominare un file"""

		if self.search_file(filename,directory):
			self.ftp.rename(filename,nuovoName)
			print 'File: %s cambiato in: %s' %(filename,nuovoNome)
			return True
		else:
			print '[!!]Nessuna corrispondenza trovata!'
			return False

	def delete_file (self,filename,directory):
		if self.search_file(filename,directory):
 			self.ftp.delete(filename)
			print 'File %s cancellato!' %(filename)
		else:
			print '[!!]File non trovato'
                        
                
	def upload(self,filename,directory_uscita):
		"""Comando: UPL    Parametri: nameFile(Nome del file con relativo percorso), directory_uscita(Directory remota di uscita.
		Compito: Invia un file al server  (Il valore predefinito è la directory remota corrente).
		"""
		try:
			self.change_directory('R',directory_uscita)
			file_locale = open(filename,'rb')
			self.ftp.storbinary('STOR %s' %(str(filename)), file_locale)
			print 'File inviato in %s' %(self.ftp.pswd())
		except ftplib.error_perm,e:
			print '[ERROR] %s' %(e)
		except IOError,e:
			print '[ERROR]%s' %(e)
			print '[!!]Sintassi corretta del comando UPL: UPL  file_remoto directory_uscita esempio: UPL  favicon.ico C:\Users\normal_user\Desktop\Eggs'
        
	def controlla_cmd(self,comando):
		"""Controlla se il  comando è valido"""
		comando_VERO = comando[12:]
#		print comando_VERO
		comando_VERO = comando_VERO.split()
#		print comando_VERO
		comando_trovato = False
		for x in comando_VERO:
			if x.upper() in self.comandi:
				comando_trovato = True
				cmd = x.upper()
				self.avvia_cmd(cmd,[y for y in comando_VERO if y != x])
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
			help(ftp_help)
		elif cmd == self.comandi[12]:
			self.info()
			
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()

class Attvarwin:		#la classe principale contenete tutte le funzioni
    def __init__(self):		#la funzione principale della classe
        self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)		#la finestra contenitore
        self.win.set_title("Attività Varie")		#setta il titolo della finestra
#---------------------------------------------------------------
	#definisco tutte le variabili dei box
#----------------------------------------------------------------
	vboxer = gtk.VBox(False)		
	hbox = gtk.HBox(False)
	hbox1 = gtk.HBox(False)
	hbox2 = gtk.HBox(False)
	vbox = gtk.VBox(False)
	vbox1 = gtk.VBox(False)
	vbox2 = gtk.VBox(False)
	vbox3 = gtk.VBox(False)
	vbox4 = gtk.VBox(False)
	vbox5 = gtk.VBox(False)
	
#-------------------------------------------------------------
	
	self.win.connect("destroy", self.exit)		#assegno al pulsante destroy 
	self.labelcent = gtk.Label("yum update, ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc. ecc.")
	fg_color_Att = pango.AttrForeground(65535, 0, 0, 0, 1000)
	size_Att = pango.AttrSize(20000, 0, -1)
	attr = pango.AttrList()
	attr.insert(fg_color_Att)
	attr.insert(size_Att)
	self.labelcent.set_attributes(attr)
	
#--------------------------------------------------------------
	#DEFINISCO TUTTI  I BOTTONI DELLA FINESTRA
#--------------------------------------------------------------
	
	self.button = gtk.Button(None, gtk.STOCK_QUIT)		#definisce il bottone contenete uno stock item
        self.button.connect("clicked", self.exit)		#assegna al bottone la funzione di uscita dal programma
	gtk.stock_add([(gtk.STOCK_DIALOG_INFO, "Info", 0, 0, "")])   
	self.but = gtk.Button(None, gtk.STOCK_DIALOG_INFO, True)
        self.but.connect("clicked", self.info)
	self.button1 = gtk.Button("button...")		#definisce un altro bottone
        self.button1.connect("clicked", self.win1)		#assegna al bottone una funzione
	self.button2 = gtk.Button("toggle,...")		#definisce un altro bottone
        self.button2.connect("clicked", self.win2)		#assegna al bottone una funzione cosi per tutti i bottone fino al segno di commento
	self.button3 = gtk.Button("label...")
        self.button3.connect("clicked", self.win3)
	self.button4 = gtk.Button("entry...")
        self.button4.connect("clicked", self.win4)
	self.button5 = gtk.Button("dialog...")
        self.button5.connect("clicked", self.win5)
	self.button6 = gtk.Button("tool...")
        self.button6.connect("clicked", self.win6)
	self.button7 = gtk.Button("image...")
        self.button7.connect("clicked", self.win7)
	self.button8 = gtk.Button("look...")
        self.button8.connect("clicked", self.win8)
	self.button9 = gtk.Button("Text...")
        self.button9.connect("clicked", self.win9)

#------------------------------------------------------------------
	
	#questo frame contiene  la label :"labelcent"
	self.frame = gtk.Frame("Elenco delle attività")
	self.frame.add(self.labelcent)
	
#-------------------------------------------------------------------
	#assegno ai box gli oggetti che devono contenere
	vbox.pack_start(self.button1, False, False, 5)
	vbox.pack_start(self.button4, False, False, 5)
	vbox.pack_start(self.button7, False, False, 5)
	vbox1.pack_start(self.button2, False, False, 5)
	vbox1.pack_start(self.button5, False, False, 5)
	vbox1.pack_start(self.button8, False, False, 5)
	vbox2.pack_start(self.button3, False, False, 5)
	vbox2.pack_start(self.button6, False, False, 5)
	vbox2.pack_start(self.button9, False, False, 5)

	vbox3.pack_start(self.frame, False, False, 10)

	vbox4.pack_start(self.button, False, 1, 10)
	vbox5.pack_start(self.but, False, 1, 10)

	hbox.pack_start(vbox3, False, False)
	hbox1.pack_start(vbox, True, True, 5)
	hbox1.pack_start(vbox1, True, True, 5)
	hbox1.pack_start(vbox2, 1, 1, 5)
	hbox2.pack_start(vbox4, 1,1)
	hbox2.pack_start(vbox5, 1,1)
	vboxer.pack_start(hbox, True, False)
	vboxer.pack_start(hbox1, True,False )
	vboxer.pack_start(hbox2, True, False)
	
	#-----------------------------------------------------------------------
	
	#aggiungo a win la variabile che contiene tutte le box(vboxer)
	self.win.add(vboxer)
        self.win.show_all()

    def win1(self, widget):		#funzione contenete la finestra win1
	self.win1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win1.set_position(gtk.WIN_POS_CENTER)
	self.win1.set_title("Button()")
	self.win1.set_border_width(15)
	hbox1 = gtk.HBox(True, 0)
	hbox2 = gtk.HBox(True, 0)
	hbox3 = gtk.HBox(True, 0)
	hbox4 = gtk.HBox(True, 0)
	vbox = gtk.VBox(True, 0)
	self.button1 = gtk.Button("normal")
	self.button2 = gtk.Button(None, gtk.STOCK_DIALOG_INFO)
	self.button3 = gtk.Button("_underline", use_underline=True)
	self.label1 = gtk.Label("Normale bottone: gtk.Button(label)")
	self.label2 = gtk.Label("Bottone con stock item: gtk.Button(None, gtk.STOCK_ITEM)")
	self.label3 = gtk.Label("Bottone con mnemonic accellerator: gtk.Button('_label', True)")
	self.label4 = gtk.Label("Ricorda: 'clicked' per il clik, 'enter' per attivare quando il puntatore entra nell'bottone.")
	hbox1.pack_start(self.button1, True, True, 5)
	hbox1.pack_start(self.label1, True, True, 5)
	hbox2.pack_start(self.button2, True, True, 5)
	hbox2.pack_start(self.label2, True, True, 5)
	hbox3.pack_start(self.button3, True, True, 5)
	hbox3.pack_start(self.label3, True, True, 5)
	hbox4.pack_start(self.label4, True, True, 5)
	vbox.pack_start(hbox1, True, False, 5)
	vbox.pack_start(hbox2, True, False, 5)
	vbox.pack_start(hbox3, True, False, 5)
	vbox.pack_start(hbox4, True, False,  10)

	self.win1.add(vbox)
	self.win1.show_all()
	gtk.main()

    def win2(self, widget):		#funzione contenete la finestra win1
        self.win2 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win2.set_position(gtk.WIN_POS_CENTER)
	self.win2.set_title("toggle,check,radio button")
	vbox = gtk.VBox(False, 0)
	hbox1 = gtk.HBox(False, 0)
	hbox2 = gtk.HBox(False, 0)
	hbox3 = gtk.HBox(False, 0)
	vbox1 = gtk.VBox(False, 0)
	vbox2 = gtk.VBox(False, 0)
	vbox3 = gtk.VBox(False, 0)
	vbox4 = gtk.VBox(False, 0)
	vbox5 = gtk.VBox(False, 0)
	vbox6 = gtk.VBox(False, 0)
	self.button_t1 = gtk.ToggleButton("primo toggle")
	self.button_t1.connect("toggled", self.tog1, "primo toggle")
	self.button_t2 = gtk.ToggleButton("secondo toggle")
	self.button_t2.connect("toggled", self.tog2, "secondo toggle")
	self.label_t1 = gtk.Label("I Toggle Button si creano con la sintassi gtk.ToggleButton e \nhanno il vantaggio di avere 2 stadi grafici normale e attivo in modo da richiamare\n una funzione tipo: self.button.connect('toggled', widget, 'label')\n nel widget va inserita la funzione con widget.get_active()\n tipo: if widget.get_active(): funzione else:    funzione")
	self.button_c1 = gtk.CheckButton("primo check")
	self.button_c1.connect("toggled", self.check1, "primo check")
	self.button_c2 = gtk.CheckButton("secondo check")
	self.button_c2.connect("toggled", self.check2, "secondo check")
	self.label_c1 = gtk.Label("I checkbutton funzionano esattamente come i togglebutton vengono\n richiamati dalla funzione gtk.CheckButton")
	self.button_r1 = gtk.RadioButton(None, "nessuna finestra")
	self.button_r2 = gtk.RadioButton(self.button_r1, "finestra 1")
	self.button_r2.connect("toggled", self.rad2, "secondo radio")
	self.button_r3 = gtk.RadioButton(self.button_r1, "finestra 2")
	self.button_r3.connect("toggled", self.rad3, "terzo radio")
	self.label_r1 = gtk.Label("I radio button sono utili perche permettono all'utente di fare una scelta sola\n tra due o piu possibilita la sintassi per richiamarli e gtk.RadioButton() e funzionano come i togglebutton") 
	vbox1.pack_start(self.button_t1, True, False, 5)
	vbox1.pack_start(self.button_t2, True, False, 5)
	vbox2.pack_start(self.label_t1, False, False, 5)
	vbox3.pack_start(self.button_c1, False, False, 5)
	vbox3.pack_start(self.button_c2, False, False, 5)
	vbox4.pack_start(self.label_c1, False, False)
	vbox5.pack_start(self.button_r1, False, False)
	vbox5.pack_start(self.button_r2, False, False)
	vbox5.pack_start(self.button_r3, False, False)
	vbox6.pack_start(self.label_r1, False, False)
	hbox1.pack_start(vbox1, False, False, 5)
	hbox1.pack_start(vbox2, False, False, 5)
	hbox2.pack_start(vbox3, False, False, 5)
	hbox2.pack_start(vbox4, False, False, 5)
	hbox3.pack_start(vbox5, False, False)
	hbox3.pack_start(vbox6, False, False)
	vbox.pack_start(hbox1, False, False, 10)
	vbox.pack_start(hbox2, False, False, 10)
	vbox.pack_start(hbox3, False, False, 10)
	self.win2.add(vbox)
	self.win2.show_all()
   

    def rad2(self, widget, data=None):		#funzione utilizzata dal primo secondo radio button 
	if widget.get_active():
		self.windtg = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windtg.set_default_size(200, 200)
		self.lab = gtk.Label("finestra aperta\n con il secondo radio")
		self.windtg.add(self.lab)
		self.windtg.show_all()
	else:
		self.windtg.destroy()

    def rad3(self, widget, data=None):		#funzione utilizzata dal terzo radio button
	if widget.get_active():
		self.windtg = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windtg.set_default_size(200, 200)
		self.lab = gtk.Label("finestra aperta\n con il terzo radio")
		self.windtg.add(self.lab)
		self.windtg.show_all()
	else:
		self.windtg.destroy()
   
    def tog1(self, widget, data=None): 		#funzione utilizzata dal primo toggle button

	if widget.get_active():
		self.windtg = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windtg.set_default_size(200, 200)
		self.lab = gtk.Label("finestra di toggle 1")
		self.windtg.add(self.lab)
		self.windtg.show_all()
	else:
		self.windtg.destroy()
    
    def tog2(self, widget, data=None): 		#funzione utilizzata dal secondo toggle button

	if widget.get_active():
		self.winddtg = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.winddtg.set_default_size(200, 200)
		self.labb = gtk.Label("finesra di toggle 2")
		self.winddtg.add(self.labb)
		self.winddtg.show_all()
	else:
		self.winddtg.destroy()	

    def check1(self, widget, data=None): 	#funzione utilizzata dal primo check button

	if widget.get_active():
		self.windch = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windch.set_default_size(200, 200)
		self.lab = gtk.Label("finestra di check 1")
		self.windch.add(self.lab)
		self.windch.show_all()
	else:
		self.windch.destroy()

    def check2(self, widget, data=None): 	#funzione utilizzata dal secondo check button

	if widget.get_active():
		self.winddch = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.winddch.set_default_size(200, 200)
		self.lab = gtk.Label("finestra di check 2")
		self.winddch.add(self.lab)
		self.winddch.show_all()
	else:
		self.winddch.destroy()		

    def win3(self, widget):					#funzione che apre la 3a finestra
        self.win3 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win3.set_title("Label")
	vbox = gtk.VBox(False, 0)
	hbox1 = gtk.HBox(True, 0)
	hbox2 = gtk.HBox(True, 0)
	hbox3 = gtk.HBox(True, 0)
	hbox4 = gtk.HBox(True, 0)
	hbox5 = gtk.HBox(True, 0)
	hbox6 = gtk.HBox(True, 0)
	vbox11 = gtk.VBox(True, 0)
	vbox12 = gtk.VBox(True, 0)
	vbox21 = gtk.VBox(True, 0)
	vbox22 = gtk.VBox(True, 0)
	vbox31 = gtk.VBox(True, 0)
	vbox32 = gtk.VBox(True, 0)
	vbox41 = gtk.VBox(True, 0)
	vbox42 = gtk.VBox(True, 0)
	vbox51 = gtk.VBox(True, 0)
	vbox52 = gtk.VBox(True, 0)
	vbox61 = gtk.VBox(False, 0)
	vbox62 = gtk.VBox(False, 0)
	self.label1 = gtk.Label("Normale label contenente testo")
	self.label1lab = gtk.Label("le label si richiamno con la funzione gtk.Label\n per andare a capo inserire nel testo /n con la \nslash al contratrio pero ovvi motivi")
	self.label2 = gtk.Label("label dinamica cambia con l'esecuzione")
        self.buttonlab2 = gtk.Button(None, gtk.STOCK_EXECUTE)
        self.buttonlab2.connect("clicked", self.change_text)
	self.label2lab = gtk.Label("label dinamica la label cambia testo con il comando\n self.nomelabel.set_text('testo')")
	self.label3 = gtk.Label("label contenete<b><big> testo evidenziato</big></b>")
	self.label3lab = gtk.Label("nelle label e possibile evidenziare del testo inserendo i tag\n <b><big>testo</big></b> bisogna inoltre\n inserire la funzione self.nomelabel.set_use_markup(True)")
    	self.label3.set_use_markup(True)
	self.label4 = gtk.Label("Il contenuto di questa label e selezionabile!")
	self.label4.set_selectable(True)
	self.label4lab = gtk.Label("Di default il  contenuto delle label non e selezionabile mentre \ninserendo l'opzione self.nomelabele.set_selectable(True)\n la si rende selzionabile, si puo rendere selezionabile anche solo una parte\ncon il comando gtk.Label.select_region(start, end) \n dove start e end si riferiscono al numero del carattere di inizio e di fine") 
	self.chechkk5 = gtk.CheckButton("check associato al label sovrastante!")
	self.chechkk5.connect("toggled", self.checkk5win, False)
	self.label5 = gtk.Label("_clicckami!  premi alt+c per attivare il Mnemonic accelerator")
	self.label5.set_mnemonic_widget(self.chechkk5)
	self.label5.set_use_underline(True)
	self.label5lab = gtk.Label("Label con mnemonic accelerator associato ad un widget  per attivare e disattivare\n il widget e necessario o clicckare o usare il  Mn.acc associato per associare\n un widget ad un label con MnAcc.  self.nomelabel.set_mnemonic_widget(widget)")
	self.label6 = gtk.Label("Label contenuta in un frame")
	self.framelab6 = gtk.Frame("frame")
	self.framelab6.add(self.label6)
	self.label6lab =gtk.Label("I frame sono contenitori che possono contenere oggetti per crare un frame \n bisogna creare la varibile con la funzione gtk.Frame('intestazione') e poi aggiungere \n al frame l'ogrtto come se fosse un windows")
	vbox11.pack_start(self.label1, True, False, 10)
	vbox12.pack_start(self.label1lab, True, False, 10)
	vbox21.pack_start(self.label2, True, False)
	vbox21.pack_start(self.buttonlab2, True, False)
	vbox22.pack_start(self.label2lab, True, False, 10)
	vbox31.pack_start(self.label3, True, False, 10)
	vbox32.pack_start(self.label3lab, True, False, 10)
	vbox41.pack_start(self.label4, True, False, 10)
	vbox42.pack_start(self.label4lab, True,  False, 10)
	vbox51.pack_start(self.label5, True, True)
	vbox51.pack_start(self.chechkk5, True, True)
	vbox52.pack_start(self.label5lab, True, False, 10)
	vbox61.pack_start(self.framelab6, True, True, 10)
	vbox62.pack_start(self.label6lab, True, True, 10)
	hbox1.pack_start(vbox11, True, True, 10)
	hbox1.pack_start(vbox12, True, True, 10)
	hbox2.pack_start(vbox21, True, True, 10)
	hbox2.pack_start(vbox22, True, True, 10)
	hbox3.pack_start(vbox31, True, True, 10)
	hbox3.pack_start(vbox32, True, True, 10)
	hbox4.pack_start(vbox41, True, True, 10)
	hbox4.pack_start(vbox42, True, True, 10)
	hbox5.pack_start(vbox51, True, True, 10)
	hbox5.pack_start(vbox52, True, True, 10)
	hbox6.pack_start(vbox61, True, True, 10)
	hbox6.pack_start(vbox62, True, True, 10)
	vbox.pack_start(hbox1, False, False)
	vbox.pack_start(hbox2, False, False)
	vbox.pack_start(hbox3, False, False)
	vbox.pack_start(hbox4, False, False)
	vbox.pack_start(hbox5, False, False)
	vbox.pack_start(hbox6, False, False)
	self.win3.add(vbox)
	self.win3.show_all()
	
    def checkk5win(self, widget, data=None):	#funzione utilizzata da un check button contenuto in win3 che apre una finestra
	if widget.get_active():
		self.checkk5win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.checkk5winlab = gtk.Label("questa finestra e stata aperta con un \ncheck associato al'mnemonic accelerator della label")
		self.checkk5win.add(self.checkk5winlab)
		self.checkk5win.show_all()
	else: 
		self.checkk5win.destroy()

    def change_text(self, widget, data=None):	#funzione che cambia il testo quando si preme il pulsante in win3
        self.label2.set_text("Frase cambiata grazie al comando set_text")

    def win4(self, widget):					#funzione contenete la finestra win4
        self.win4 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win4.set_title("Entry")
	vbox = gtk.VBox(False, 0)
	vbox1 = gtk.VBox(False, 0)
	vbox2 = gtk.VBox(False, 0)
	hbox1 = gtk.HBox(False, 0)	
	hbox2 = gtk.HBox(False, 0)
	hbox3 = gtk.HBox(False, 0)
	hbox4 = gtk.HBox(False, 0)
	hbox5 = gtk.HBox(False, 0)	
	hbox6 = gtk.HBox(False, 0)
	hbox7 = gtk.HBox(False, 0)
	hbox8 = gtk.HBox(False, 0)
	hbox9 = gtk.HBox(False, 0)
	hbox10 = gtk.HBox(False, 0)
	self.entry1 = gtk.Entry()
	self.entry1lab = gtk.Label("le entry vengono utilizzate per inserire stringhe si richiamo con la funzione gtk.Entry()")
	self.entry2 = gtk.Entry()
	self.entry2.set_visibility(False)
	self.entry2.set_invisible_char('*')
	self.entry2lab = gtk.Label("questa entry e uguale a quella sopra solo che non vengono visualizzati i caratteri grazie a gtk.set_invisible_char(char)")
	self.entry3 = gtk.Entry()
	self.entry3.set_visibility(False)
	self.entry3lab = gtk.Label("questa entry e uguale alla precendente solo che non e stato importato nessun carattere e rimane invisibile \ncon il carattere di default ossia * ")
	self.entry4 = gtk.Entry()
	self.entry4.set_text("testo di default")
	self.entry4.set_property("editable", False)
	self.entry4lab = gtk.Label("a questa entry ho applicato 2 funzioni la prima gtk.set_text() inserisce un testo di default la seconda\nset_propety('editable', False rende al entry visibile ma non modificabile")
	self.framentry1 = gtk.Frame("Commenti")
	self.labelentry1 = gtk.Label("Ci sono numerose funzioni non citate ma e bene ricordare che esistono delle EntryCompletition() che permettono di avere una menu a tendina \nper scegliere un opzione tra altre inserite in una lista, e si puo cambiare la posizione del testo nell'entry, inoltre l'imput dell'entry per assegnarlo\n ad una variabile si utilizza la funzione gtk.entry.get_text()")
	self.framentry1.add(self.labelentry1)
	hbox3.pack_start(self.entry1, True, False, 10)
	hbox4.pack_start(self.entry2, True, False, 10)
	hbox5.pack_start(self.entry3, True, False, 10)
	hbox6.pack_start(self.entry4, True, False, 10)
	hbox7.pack_start(self.entry1lab, True, False, 10)
	hbox8.pack_start(self.entry2lab, True, False, 10)
	hbox9.pack_start(self.entry3lab, True, False, 10)
	hbox10.pack_start(self.entry4lab, True, False, 10)

	vbox1.pack_start(hbox3, True, True, 10)
	vbox1.pack_start(hbox4, True, True, 10)
	vbox1.pack_start(hbox5, True, True, 10)
	vbox1.pack_start(hbox6, True, True, 10)
	vbox2.pack_start(hbox7, True, True, 10)
	vbox2.pack_start(hbox8, True, True, 10)
	vbox2.pack_start(hbox9, True, True, 10)
	vbox2.pack_start(hbox10, True, True, 10)

	hbox1.pack_start(vbox1, True, True)
	hbox1.pack_start(vbox2, True, True)
	hbox2.pack_start(self.framentry1, False, False)

	vbox.pack_start(hbox1, False, False)
	vbox.pack_start(hbox2, False, False)

	self.win4.add(vbox)
	self.win4.show_all()
 
    def win5(self, widget):					#funzione contenete la 5a finestra
        self.win5 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win5.set_title("dialog()")
	hbox= gtk.HBox(False, 0)
	vbox1 = gtk.VBox(False, 0)
	vbox2 = gtk.VBox(False, 0)
	self.labeldial1 = gtk.Label("prosegui per vedere l'esempio di dialog")
	self.dialbutton1 =gtk.Button("Quit")
	self.dialbutton1.connect("clicked", self.dialogRun)
	self.labeldial2 = gtk.Label("prosegui per vedere l'esempio di dialog")
	self.dialbutton2 =gtk.Button("Info")
	self.dialbutton2.connect("clicked", self.showMessage)
	vbox1.pack_start(self.labeldial1, True, False, 10)
	vbox1.pack_start(self.dialbutton1, True, False, 10)
	vbox2.pack_start(self.labeldial2, True, False, 10)
	vbox2.pack_start(self.dialbutton2, True, False, 10)
	hbox.pack_start(vbox1, True, True, 10)
	hbox.pack_start(vbox2, True, True, 10)
	self.win5.add(hbox)
        self.win5.show_all()

    def dialogRun(self, widget): 			#funzione contenete un dialog
        self.dialog = gtk.Dialog('Sure?', self.win5, 
                    gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT, 
                    (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
        self.dialog.vbox.pack_start(gtk.Label("Vuoi davvero uscire??"))
        self.dialog.show_all()
        response = self.dialog.run()
        if response == gtk.RESPONSE_ACCEPT: 
		self.win5.destroy()
		self.dialog.destroy()
        elif response == gtk.RESPONSE_REJECT: 
		self.dialog.destroy()
	self.dialog.destroy()

    def showMessage(self, widget, data=None):		#funzione contenete un dialogo di info
        message = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, 
                                    gtk.BUTTONS_CLOSE, "Programma creato da Total")    
        message.show()
        resp = message.run()
        if resp == gtk.RESPONSE_CLOSE:    
            message.destroy()

    def win6(self, widget):					#funzione contenete la 6a finestra
        self.win6 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	vbox = gtk.VBox(False, 0)
	hbox1 = gtk.HBox(False, 0)
	hbox2 = gtk.HBox(False, 0)
	vbox1 = gtk.VBox(True, 0)
	vbox2 = gtk.VBox(True, 0)
	vbox3 = gtk.VBox(True, 0)
	vbox4 = gtk.VBox(True, 0)
	self.toolbut =gtk.Button("toolbar")
	self.toolbut.connect("clicked", self.tool)
	self.toolbutlab =gtk.Label("Questo button apre una windows cntenete una toolbar utilissima per numerose applicazioni\n si richiam con la funzione gtk.Toolbar() mentre i button si richiamano con gtk.ToolButton() si inseriscono nella label con\n gtk.toolbar.insert(nomebutton,posizione")
	self.tootbut = gtk.Button("tooltips")
	self.tootbut.connect("clicked", self.tooll)
	self.tootbutlab =gtk.Label("Questo button apre una finestra contente un button a cui e associato un tooltips molto comodo\n per indicare brevemente cosa succede dopo aver premutio que bottone si richiama con gtk.Tooltips() e si assegna \n con gtk.tooltip.set_tip(widget, 'messaggio', 'private')")
	vbox1.pack_start(self.toolbut, True, False, 5)
	vbox2.pack_start(self.toolbutlab, True, False, 5)
	vbox3.pack_start(self.tootbut, True, False, 5)
	vbox4.pack_start(self.tootbutlab, True, False, 5)
	hbox1.pack_start(vbox1, True, False, 5)
	hbox1.pack_start(vbox2, True, False, 5)
	hbox2.pack_start(vbox3, True, False, 5)
	hbox2.pack_start(vbox4, True, False, 5)
	vbox.pack_start(hbox1, True, False, 5)
	vbox.pack_start(hbox2, True, False, 5)
	self.win6.add(vbox)
	self.win6.show_all()

    def tool(self, widget):					#funzione contentente una toolbar
	self.wintool =gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.toolbar = gtk.Toolbar()
	self.wintool.set_default_size(120, 50)
	self.toolbutton = gtk.ToolButton(gtk.STOCK_QUIT)
	self.toolbutton.connect("clicked", self.wintoolexit)
	self.toolbutton1 =gtk.ToolButton(gtk.STOCK_NEW)
	self.toolbutton1.connect("clicked", self.wintoolexit)
	self.toolbar.insert(self.toolbutton, -1)
	self.toolbar.insert(self.toolbutton1, 0)
	self.wintool.add(self.toolbar)
	self.wintool.show_all()
    
    def tooll(self, widget):				#funzione contente un tooltips che permette di far apparire un messaggio quando sipassa con il mouse sopra ad un bottone
	self.wintooll =gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.wintooll.set_border_width(30)
	self.wintooll.set_default_size(100, 100)
	self.tobutton = gtk.Button(None, gtk.STOCK_QUIT)
	self.tobutton.connect("clicked", self.wintolexit)
	self.tooltips =gtk. Tooltips()
	self.tooltips.set_tip(self.tobutton, "con questo bottone esci..")
	self.wintooll.add(self.tobutton)
	self.wintooll.show_all()

    def wintoolexit(self, widget):			#definisce l'uscita da tool
	self.wintool.destroy()

    def wintolexit(self, widget):			#definisce l'uscita da wintooll
	self.wintooll.destroy()

    def win7(self, widget):					#funzione che definisce la finestra win7
        self.win7 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	hbox = gtk.HBox(False, 0)
	vbox1 = gtk.VBox(False, 0)
	vbox2 = gtk.VBox(False, 0)
	self.img = gtk.Image()
	self.img.set_from_file('024_2.jpg')
	self.immbutton = gtk.Button()
	self.immbutton.add(self.img)
	self.immbutton.connect("clicked", self.immwinn)
	self.immbuttonlab = gtk.Label("con questo bottone si apre una finestra contenete un immagine la funzione immagine si richiama con gtk.Image()\n e si specifica il perrcoso del file in gtk.image.set_from_file() specificando cosi il percorso")
	vbox1.pack_start(self.immbutton, 10)
	vbox2.pack_start(self.immbuttonlab, 10)
	hbox.pack_start(vbox1, False, False, 10)
	hbox.pack_start(vbox2, False, False, 10)
	self.win7.add(hbox)
	self.win7.show_all()

    def immwinn(self, widget):				#funzione contenente la finestra con immagine utilizzata usata in win7 e
	self.immwin  = gtk.Window(gtk.WINDOW_TOPLEVEL)
        img = gtk.Image()
        img.set_from_file('024_1.jpg')
        self.immwin.add(img)
        self.immwin.show_all()

    def win8(self, widget):					#funzione contenente l'8ava finestra
        self.win8 = gtk.Window(gtk.WINDOW_TOPLEVEL)
        vbox = gtk.VBox(False, 0)
	hbox1 = gtk.HBox(False, 0)
	hbox2 = gtk.HBox(False, 0)
	hbox3 = gtk.HBox(False, 0)
	hbox4 = gtk.HBox(False, 0)
	vbox1 = gtk.VBox(False, 0)
	vbox2 = gtk.VBox(False, 0)
	vbox3 = gtk.VBox(False, 0)
	vbox4 = gtk.VBox(False, 0)
	vbox5 = gtk.VBox(False, 0)
	vbox6 = gtk.VBox(False, 0)
	self.lookbutton =gtk.Button("background")
	self.lookbutton.connect("clicked", self.lookwin)
	self.lookbuttonlab =gtk.Label("questo bottone apre una finestra a cui e stato modificato il background di un colore a mia scelta\n con la funzione gtk.window.modify_bg(stato, colore)")
	self.looklabel = gtk.Label("Questa label ha un colore diverso grazie alla funzione gtk.label.modify_fg(state, color) il colore si imposta cosi come in tutti gli altri casi con gtk.gdk.color_parse('#000000')\n in questo caso ho messo #000000 pero sono colori in esadecimale ci sono numerose liste e numerosi programmi che li elencano!")
	color1 = gtk.gdk.color_parse('#7885ff')    
        self.looklabel.modify_fg(gtk.STATE_NORMAL, color1) 
	self.lookradbutton = gtk.RadioButton(None, "colore del radiobutton attivo")    
        color2 = gtk.gdk.color_parse('#7885ff')
        self.lookradbutton.modify_text(gtk.STATE_NORMAL, color2)   
	self.lookradbuttonlab = gtk.Label("questo radio button ha il colore diverso grazie alla funzione gtk.button.modify_text(state, color) applicatagli")
	gtk.stock_add([(gtk.STOCK_QUIT, " Con questo bottone si esce dal programma", 0, 0, "")])    
        self.lookbutbutton = gtk.Button(None, gtk.STOCK_QUIT)
        self.lookbutbutton.connect("clicked", self.exit)
	self.lookbutbuttonlab = gtk.Label("abbiamo modificato lo stock con  gtk.stock_add([stock, label, modifier, keyval, translation_domain]) \n in questo caso gtk.stock_add([(gtk.STOCK_QUIT, ' Con questo bottone si esce dal programma', 0, 0, '')])") 

	vbox1.pack_start(self.lookbutton, False, False, 10)
	vbox2.pack_start(self.lookbuttonlab, False, False, 10)
	vbox3.pack_start(self.lookradbutton, False, False, 10)
	vbox4.pack_start(self.lookradbuttonlab, False, False, 10)
	vbox5.pack_start(self.lookbutbutton, False, False)
	vbox6.pack_start(self.lookbutbuttonlab, False, False)
	hbox1.pack_start(vbox1 ,True, True, 10)
	hbox1.pack_start(vbox2 ,True, True, 10)
	hbox2.pack_start(self.looklabel ,True, True, 10)
	hbox3.pack_start(vbox3 ,True, True, 10)
	hbox3.pack_start(vbox4 ,True, True, 10)
	hbox4.pack_start(vbox5 ,True, True, 10)
	hbox4.pack_start(vbox6 ,True, False, 10)

	vbox.pack_start(hbox1 ,False, False, 10)
	vbox.pack_start(hbox2 ,False, False, 10)
	vbox.pack_start(hbox3 ,False, False, 10)	
	vbox.pack_start(hbox4 ,False, False)

 	self.win8.add(vbox)
	self.win8.show_all()


    def lookwin(self, widget):				#funzione contenetela finestra aperta con il bottone in win8 
	self.winlook = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.winlook.set_title('background')
        color = gtk.gdk.color_parse('#7885ff')    
        self.winlook.modify_bg(gtk.STATE_NORMAL, color)    
        self.winlook.show()

    def win9(self, widget):					#funzione contenete la nona finestra
	self.win9 = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.win9.set_default_size(500,500)
	self.win9.set_title("Testview")
	self.vbox1 = gtk.VBox(0,0)
	self.text = gtk.TextView()
	self.tool = gtk.Toolbar()
	self.toolbutton1 = gtk.ToolButton(gtk.STOCK_QUIT)
	self.toolbutton1.connect("clicked", self.exit)
	self.toolbutton2 =gtk.ToolButton(gtk.STOCK_NEW)
	self.toolbutton2.connect("clicked", self.exit)
	self.tool.insert(self.toolbutton1, -1)
	self.tool.insert(self.toolbutton2, 0)
		
	self.vbox1.pack_start(self.tool,0,0)
	self.vbox1.pack_start(self.text,1,1)
		
	self.win9.add(self.vbox1)
		
	self.win9.show_all()
		
    def exit(self, *args):					#funzione che determina l'uscita dal programma
	gtk.main_quit()
	sys.exit()
	
    def info(self, widget, data=None):	
        self.mex = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Programma creato da Total\n link:\n www.parafrenalia.org\pygtk\n www.python.it\n www.pygtk.org\n www.dak.netsons.org\n www.python.org")    
        self.mex.show()
        resp = self.mex.run()
        if resp == gtk.RESPONSE_CLOSE:    
            self.mex.destroy()
	    
    def destroy(self, *args):					#funzione che determina l'uscita dal programma
	gtk.main_quit()

 
    def main(self):							#esegue il tutto
        gtk.main()





class PangoApp1(gtk.Window): 
    def __init__(self):
        super(PangoApp1, self).__init__()
        
#        self.connect("destroy", gtk.main_quit)
        self.set_title("Unicode")
        
        label = gtk.Label(objru.encode('utf-8'))

        fontdesc = pango.FontDescription("Georgia 10")
        label.modify_font(fontdesc)

        fix = gtk.Fixed()

        fix.put(label, 5, 5)
        
        self.add(fix)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show_all()

class PangoApp2(gtk.Window): 
    def __init__(self):
        super(PangoApp2, self).__init__()
        
#        self.connect("destroy", gtk.main_quit)
        self.set_title("Attributes")
        label = gtk.Label(testtext)

        attr = pango.AttrList()

        attr.insert(fg_color)
        attr.insert(underline)
        attr.insert(bg_color)
        attr.insert(size)
        attr.insert(strike)

        label.set_attributes(attr)
        color = pango.Color('#FFFF00')
        print color
        fix = gtk.Fixed()

        fix.put(label, 5, 5)
        
        self.add(fix)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show_all()


######## MAIN LOOP ########################
#Questa è la finestra principale con i bottoni per startare le attività.
#Si chiude con la 'X' in alto a destra 
startMainWin = MainWin()
startMainWin.show_all()

######### FTP Client ############################
#if __name__ == '__main__':
#        nick = raw_input('Nick:')
#        pswd = raw_input('Password:')
#        site = raw_input('Sito:')
#        obj = ClientFTP(site,nick,pswd)
#        while obj.online: #while True
#                command = raw_input('pyFTP >>> ')
#                obj.controlla_cmd(command)      
#################################################

gtk.main()
