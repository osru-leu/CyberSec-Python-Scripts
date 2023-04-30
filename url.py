#!/usr/bin/python3
#Author: Sam Urso
#Date: 6.6.2022
#version: 1.0

'''Find hyperlink in html text
if link (href) is there print the entire line'''

import urllib.request

page = urllib.request.urlopen('http://example.org/')
page = page.read().decode('utf8')
html_str = page.split("\n")

for line in html_str: 
    if 'href' in line:
        print(line)
