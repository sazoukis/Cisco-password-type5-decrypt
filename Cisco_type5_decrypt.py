#!/usr/bin/python3
from passlib.hash import md5_crypt
text='$1$pdQG$o8nrSzsGXeaduXrjlvKc91'
salts='pdQG'
pwd_hash='o8nrSzsGXeaduXrjlvKc91'
f=open('/usr/share/wordlists/rockyou.txt','r',encoding='ISO-8859-1')
for lines in f:
    if len(lines)>=12:
        if md5_crypt.hash(lines.rstrip(), salt=salts)==text:
            print(f'[+]Password found {lines}')
            break
