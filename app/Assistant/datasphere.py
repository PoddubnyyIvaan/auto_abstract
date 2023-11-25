#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:09:49 2023

@author: ivan
"""

import yadisk
import time

def preprocessing(file_path):
    with open(file_path,'rb') as in_f:
        print('ok')
    
    text = 'aaa\nfijw'
    
    
    
    
    with open('out.txt', 'w') as out_f:
        out_f.write(text)
    
    return 'out.txt'
    

token = 'y0_AgAAAAAzSxLyAArg1wAAAADy4fApYeNMFE5WS0aalIrIJ00O2B_X2KI'
y = yadisk.YaDisk(token=token)
while True:
    print('Слушаю')
    files = list(map(lambda x: x.name,y.listdir("app:/")))
    if 'input.mp3' in files:
        print('Начинаю обработку')

        y.download("app:/input.mp3","input.mp3")
        y.remove("app:/input.mp3", permanently=True)
        y.upload(preprocessing('input.mp3'), "app:/out.txt",overwrite=True)
        print('Отправил')
        
    else:
        time.sleep(10)