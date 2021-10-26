#! /usr/bin/env python3

import psutil
import pgrep
import os
import re
import time
import logging
import datetime

logging.basicConfig(filename='/var/log/ProcessKiller/ProcessKiller.log', level=logging.INFO)
logging.info(str(datetime.datetime.today()) + ' : ProcessKiller START')

os.chdir('/home/userbot/ProcessKiller/')

def findProcessIdByName(regex):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time', 'cmdline'])
            if len(pinfo['cmdline']) > 1:
                for i in range(len(pinfo['cmdline'])):
                    if re.search(regex, pinfo['cmdline'][i]):
                        listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            logging.error(str(datetime.datetime.today()) + ' : !! ERROR  function - \'findProcessIdByName\' !!')
    return listOfProcessObjects

try:
    listOfProcess_aA = findProcessIdByName(r'.*edt_asurA.py')
    listOfProcess_aB = findProcessIdByName(r'.*edt_asurB.py')
    listOfProcess_cyber = findProcessIdByName(r'.*edt_cyber.py')
    listOfProcess_gen = findProcessIdByName(r'.*edt_gen.py')
    listOfProcess_getpdf = findProcessIdByName(r'.*getpdf.py')

    if len(listOfProcess_aA) == 0 and len(listOfProcess_aB) == 0 and len(listOfProcess_cyber) == 0 and len(listOfProcess_gen) == 0 and len(listOfProcess_getpdf) == 0:
        process = r".*chrome.*"
        listOfProcesschrome = findProcessIdByName(process)
        nb_process = len(listOfProcesschrome)
        if nb_process > 0 :
            for elem in listOfProcesschrome:
                processID = elem['pid']
                os.kill(processID,9)
            logging.info(str(datetime.datetime.today()) + ' : ' + str(nb_process) + ' processus chrome fermés')
        else :
            logging.info(str(datetime.datetime.today()) + ' : Il n\'y a aucun processus chrome')
    else:
        logging.info(str(datetime.datetime.today()) + ' : Un programme python utilise chrome !')
except:
    logging.error(str(datetime.datetime.today()) + ' : !! ERROR !!')

logging.info(str(datetime.datetime.today()) + ' : ProcessKiller END')
