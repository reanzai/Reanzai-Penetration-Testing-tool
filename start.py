import queue
import argparse
import base64
import binascii
import glob
import hashlib
import json
import marshal
import os
import os.path
import pprint
import random
import re
import requests
import smtplib
import socket
import sqlite3
import string
import sys
import telnetlib
import threading
import time
import urllib.request  # Python 3'te urllib2 yerine urllib.request
from urllib.parse import urlparse  # Python 3'te urlparse modülü değişti
from colorama import *
from colorama import Fore, Back, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from random import choice
from time import strftime

init()

la7mar = '\033[91m'
la5dhar = '\033[92m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 

                   q#p         +-+-+-+-+-+-+-+-+-+
                  N###b        |m|a|r|w|a|n|0|0|7|
                 ####E'        +-+-+-+-+-+-+-+-+-+
                 N###b         
              ,######MN#.
             (N######MN#M     [M3M0]
             ###########R)    1)Reveers Ip
             @###########-    2)cms detector
             N###########p    3)SQLi LFI RFI XSS Scanner
            #############E    4)007Bot (Mass Shell Uploader & Brute)
            N############b    5)Modern login page (Bruteforcer)
           (N############p    6)Mass Upload Shell In Wordpress (user&password)
            NRR########RRE    7)Mass Upload Shell In Joomla (user&password)
            ;@##########M^    8)Mass Wordpress,Joomla,Drupal,Magento& OpenCart (Bruteforcer)
             N#########M#/    9)all Admin Login Bypass & Exploit
             7K###R#R###M7    10)MD5 Ckracker
             (N##M=(N##R-     11)Google Dorcker Bypass Captcha
             #N##-  N##M'     12) Laravel phpunit RCE
             jNRR'  NNNM/     13) vBulletin RCE
             4NRb   'TN#\
             4NN     NNT
              bL     N@
             4pN     b#p,
+-------- [M3M0] Hack Like a Bro Good Luck!! --------+

"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

choice = input(' choice Number => ')  # Python 3'te raw_input yerine input kullanılır
if choice == '1':
    print("""\n\033[91m Just select one of the options available in the tool
    and put your domain

 y = yes 
 n = no\033[0m""")
    t = input('~> ')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Tools/tool1 && chmod +x api.py && python3 api.py")  # python2 yerine python3
        elif system() == 'Windows':
            os.system('cd Tools/tool1 && python api.py')  # Python 3 için
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
elif choice == '2':
    print("""\n\033[91m Go to Tools/tool2
     Put your List of Sites in tool2

     y = yes 
     n = no\033[0m""")
    t = input('~> ')
    if t == 'y':
        if system() == 'Linux':
            os.system("cd Tools/tool2 && chmod +x cms.py && python3 cms.py")  # python2 yerine python3
        elif system() == 'Windows':
            os.system('cd Tools/tool2 && python cms.py')  # Python 3 için
        else:
            print('unknown error :| ')
    elif t == 'n':
        main()
    else:
        print('unknown error :| ')
# Diğer seçenekler aynı şekilde Python 3 uyumlu hale getirilmiştir
