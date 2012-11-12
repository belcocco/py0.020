#Rinomina le foto che arrivano dalla fotocamera

class PhotoRename():
    def __init__(self):
        print "----- Foto -------"
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
        button_quit.connect_object("clicked", gtk.Widget.destroy, self.window)
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

    def destroy(self, widget, data=None):
        print "Esco dal programma"
        gtk.main_quit()


#def main():
#    gtk.main()
#    return 0

if __name__ == "__main__":
    PhotoRename()
#    main()
