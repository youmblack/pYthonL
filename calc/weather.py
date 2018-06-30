#!/usr/bin/env python
# coding=utf-8

from pip._vendor import requests
import re

def getHtml():
    response = requests.get('https://docs.python.org/')
    
def getTemperature():
    response = requests.get('https://docs.python.org/')
    pattern = re.compile(r'https://www.python.org/psf/donations/')
    match = pattern.findall(response.text)
    print(match)

    with open(r'C:\Users\admin\Desktop\netWorkProgram\bkgd\temp\temp\1.url.txt', 'a') as file:
        file.write(response.text)
    file.closed


