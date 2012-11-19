#!/usr/bin/python
# -*- coding: latin-1 *-*
# -*- coding: cp1252 -*-

import ftplib, os,  sys  #import module

                        
class Client(object):
"""Client FTP da linea di comando (Tutt i comandi posso essere scritti in minuscolo)
   Dopo aver avviato servono 'site' 'nick' e 'password' per attivare la 'Connessione'

           Funzioni:               Comandi associati         esempio: 
           -Directory locale         LD                        ld     (si vede dove punta)
           -Directory remota         RD                        rd     (si vede dove punta)
           -Cambio directory locale  CD                        cd l /nome_da_aggiungere_al_path_di_ld
           -Cambio directory remota  CD                        cd r /nome_da_aggiungere_al_path_di_rd
           -Lista File               LIST                      list (serve copiare la libreria ftplib.py in ????)
           -Ricerca File             SEARCH                    search nome_file
           -Rinomina File            REN                       ren nome_file directory nuovo_mome_file
           -Elimina File             DEL                       del nome_file directory
           -Download file            DW                        dw directory_remota filename directory_locale_di_uscita(_che pu� essere omessa)
           -Download all file        DWA                       dwa directory_remota filename directory_locale_di_uscita(_che pu� essere omessa)
           -Invio file               UPL                       upl nome_file directory_remota_di_uscita 
           -
           -Disconnessione           QUIT                      quit

            N.B.: DW e UPL cambiano automaticamente le dir di destinazione
                  se differiscono dal puntamento (ld, rd) di prima del comando
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
                   Compito: Si connette al server alla porta:21 in modalit� passiva"""
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
                print 'Directory locale corrente: %s' %(os.getcwd())
        
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
                """Comando: DW  Parametri: Directory(Directory  remota del file), filename(nome del file remoto), directory_uscita(Directory locale dove verr� salvato il file.
                                                                                                                    il valore predefinito � la directory corrente)
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
                   Compito: Invia un file al server                                          Il valore predefinito � la directory remota corrente).
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
                """Controlla se il  comando � valido"""
                comando = comando.split()
                comando_trovato = False
                for x in comando:
                        if x.upper() in self.comandi:
                                comando_trovato = True
                                cmd = x.upper()
                                self.avvia_cmd(cmd,[y for y in comando if y != x])
                                print "comando trovato. Ho scritto: ", cmd
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
                                print '[!!]Attenzione non � stata specificata la directory di uscita.Il file verr� salvato nelle directory corrente'
                                self.download(argv[0],argv[1])                                
                        else:
                                self.download(argv[0],argv[1],argv[2])
                elif cmd == self.comandi[4]:
                        if numero_parametri < 1:
                                print '[ERROR]Parametri non sufficienti'
                        elif numero_parametri < 2:
                                print '[!!]Attenzione non � stata specificata la directory di uscita.I files verranno salvati nelle directory corrente'
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

if __name__ == '__main__':
        nick = "raga" #raw_input('Nick:')
        pwd = "ragamuz" #raw_input('Password:')
        site = "localhost" #raw_input('Sito:')
        obj = Client(site,nick,pwd)
        while obj.online: #while True
                command = raw_input('pyFTP >>> ')
                obj.controlla_cmd(command)      
        
 
