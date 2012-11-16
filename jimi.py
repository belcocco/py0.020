#!/usr/bin/python
# *-* coding: latin-1 *-*

#------------tofy.py----------
#Creato da: total
#Data:14-8-2006
#Descrizione: Semplice Riassunto che include degli esempi di utilizzo delle pygtk.
#Revisioni:
#5-11-2006 riordino codice
#------------------------------------------


import pygtk		
import gtk
import sys

#includo le librerie necessarie 

class Window:		#la classe principale contenete tutte le funzoni
    def __init__(self):		#la funzione princuipale della classe
        self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)		#la finestra contenitore
        self.win.set_title("Riassunto funzioni")		#setta il titolo della finestra
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
	self.labelcent = gtk.Label("Questa e' un interfaccia che racchiude esempi riassuntivi di oggetti GTK+/pyGTK")
#	self.labelcent = gtk.Label("Questa GTK+/pyGTK")
	
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
	self.frame = gtk.Frame("Introduzione")
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
	self.entry2.set_invisible_char('@')
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
if __name__ == "__main__":					#metodo esterno alla classe per esegure il modulo 
    win = Window()
    win.main()
