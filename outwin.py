########### FINESTRA con gli OUTPUT 
class outwin():

    def __init__(self):
        self.outwin = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.outwin.set_resizable(True)  
        self.outwin.connect("destroy", self.close_application)
        self.outwin.set_title("Output da terminale")
        self.outwin.set_border_width(0)

        self.box1 = gtk.VBox(False, 0)
        self.outwin.add(box1)
        self.box1.show()

        self.box2 = gtk.VBox(False, 10)
        self.box2.set_border_width(10)
        self.box1.pack_start(box2, True, True, 0)
        self.box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = self.gtk.TextView()
        textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        self.textview.show()

        box2.pack_start(sw)
        # Load the file textview-basic.py into the text window
        infile = open("clone.out", "r")

        if infile:
            string = infile.read()
            infile.close()
            textbuffer.set_text(string)

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button = gtk.Button("Esci")
        button.connect("clicked", self.close_application)
        box2.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        outwin.show()

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

    def close_application(self, widget):
        gtk.main_quit()

