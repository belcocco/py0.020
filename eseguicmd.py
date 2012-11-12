#!/usr/bin/env python
# *-* coding: latin-1 *-*
#Cerca il carattere 'TAB' in tutti i file *.py della dir corrente

import string, os
#cmd = 'find . -name "*.py" -print'         # find is a standard Unix tool
cmd = 'find . -name "lamp.sh" -print'         # find is a standard Unix tool
 
for file in os.popen(cmd).readlines():     # run find command
    num  = 1
    name = file[:-1]                       # strip '\n'
    for line in open(name).readlines():    # scan the file
#        pos = string.find(line, "\t")
#        pos = string.find(line, "gtk")
        pos = string.find(line, "#")
        if  pos >= 0:
            print name, num, pos           # report tab found
            print '....', line[:-1]        # [:-1] strips final \n
            print '....', ' '*pos + '*', '\n'
        num = num+1
