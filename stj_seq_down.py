#!/usr/bin/env python3

import requests
import re
from sys import argv
from bs4 import BeautifulSoup

def get_page(url):
    print('trying to fetch page: ', url)
    r = requests.get(url)
    if re.search('(Ocorreu um erro ao buscar o documento\. Tente novamente)|(O documento não foi liberado para publicação)', r.text):
        print('No document available.')
    else:
        text = BeautifulSoup(r.text, 'html5lib').text
        text_list = text.splitlines()
        text_list = [i for i in text_list if i]
        try:
            with open('html_data/' + str(i) + '.html', 'wb') as f:
                f.write(r.content)
        except IndexError as e:
            print(e)
        except UnicodeError as e:
            print(e)



for i in range(int(argv[1]), int(argv[2])):
    url = 'https://ww2.stj.jus.br/websecstj/cgi/revista/REJ.cgi/MON?seq=%d&formato=HTML' % i
    get_page(url)
