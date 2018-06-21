#!/usr/bin/env python3

import re
from sys import argv
from bs4 import BeautifulSoup

def get_text(file_name):
    with open(file_name) as f:
        t = f.read()
    bs = BeautifulSoup(t, "html5lib")
    return bs.text

def get_header(datalist):
    titlere = re.compile('(\d\d)|(\d{4})⁄\d{7,8}-\d')
    for i, data in enumerate(datalist):
        match = titlere.search(data)
        if match:
            title = match.group()
            end_title = i
    actorsre = re.compile('.+:.+')
    actors = list()
    for data in datalist[end_title:]:
        actor = actorsre.search(data)
        if actor:
            actors.append(actor.group())
        else:
            break
    return {'title': title,
            'actors': actors
            }

def get_body(datalist):
    headtitlere = re.compile('EMENTA|DECISÃO|DESPACHO|ACÓRDÃO')
    head_titles = list()
    content_list = list()
    titlevalue = False
    contentvalue = False
    acc_text = ""
    for i in datalist:
        line = i.strip()
        isheadtitle = headtitlere.match(line)
        if isheadtitle:
            head_titles.append(isheadtitle.group())
            if contentvalue:
                content_list.append(acc_text)
                contentvalue = False
            titlevalue = True
        elif titlevalue:
            acc_text += line
            contentvalue = True
    body = dict(zip(head_titles, content_list))
    return body

def struct_info(text):
    textlist = [i for i in text.splitlines() if i]
    header, pos = get_header(textlist)
    

if __name__ == '__main__':
    text = get_text(argv[1]).splitlines()
    head = get_header(text)
    body = get_body(text)
    print(head)
    print("--------")
    print(body)