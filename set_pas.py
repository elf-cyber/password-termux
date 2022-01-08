# -*- coding: utf-8 -*-
import os
os.chdir('/data/data/com.termux//files/home')
file = open('run.sh' , 'a+')
file.write('python password-termux/password.py')
file.close()
try:
    file2 = open('.bashrc' , 'a')
    file2.write('bash run.sh')
except:
    try:
        os.system('> .bashrc')
    except:
        pass
    file2 = open('.bashrc', 'a')
    file2.write('bash run.sh')
