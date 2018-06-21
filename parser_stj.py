#!/usr/bin/env python3

import re
from sys import argv
from bs4 import BeautifulSoup

def get_text(file_name):
    with open(file_name) as f:
        t = f.read()
    bs = BeautifulSoup(t, "html5lib")
    return bs.text

def get_header(text):
    idre = re.compile('.+(\d\d)|(\d{4})⁄\d{7,8}-\d')
    headre = re.compile('\n[A-Z]+?\n?:\n?.+?\n')
    try:
        title = idre.search(text).group()
    except AttributeError as e:
        print(e)
        title = None
    try:
        head = [i.split(':')
                for i in [j.replace('\n', '')
                          for j in headre.findall(text)]]
    except AttributeError as e:
        print(e)
        head = None
    return {
        'title': title,
        'head': head
    }

def get_body(text):
    ementare = re.compile('(E M E N T A|EMENTA) +\n')
    afterementare = re.compile('(?<=(E M E N T A|EMENTA)) .+(?=(ACÓRDÃO|A C Ó R D Ã O|DECISÃO|D E C I S Ã O)), flags=re.DOTALL')
        
def get_