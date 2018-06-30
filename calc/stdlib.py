#!/usr/bin/env python
# coding=utf-8

# 标准库
# Operating System Interface
import os
os.getcwd()      # Return the current working directory
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

import shutil
shutil.copyfile('a.txt', 'b.txt')
shutil.move('c.txt', 'd.txt')

# File Wildcards
import glob
glob.glob('*.py')

# Command Line Arguments
import sys
print(sys.argv)

# Error Output Redirection and Program Termination
sys.stderr.write('Warning, log file not found starting a new one\n')

# String Pattern Matching
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'tea for too'.replace('too', 'two')

# Mathematics
import math
math.cos(math.pi / 4)
math.log(1024, 2)

import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# Internet Access
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()

# Datas and Times
# dates are easily constructed and formatted
from datetime import date
now = date.today()
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday

# Data Compression
import zlib
s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
zlib.decompress(t)
zlib.crc32(s)

# Performace Measurement
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

Timer('a,b = b,a', 'a=1; b=2').timeit()

# Quality Control

# Batteries Included

# Output Formatting

# Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village = 'Hottingham', cause = 'the ditch fund')

# Working with Binary Data Record Layouts

# Multi-threading

# Logging

# Weak Reference

# Tools for Working with Lists

# Decimal Floating Point Arithmetic
