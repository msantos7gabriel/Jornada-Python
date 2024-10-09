import pyautogui as py
import pandas as pd
import os
from time import sleep

py.PAUSE = 0.5


def abrir_opera():
    py.press('win')
    py.write('opera')
    py.press('enter')
    abrir_sys()


def abrir_sys():
    sleep(2)
    py.click(250, 50, clicks=1)
    py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login',
             )
    py.press('enter')
    sleep(3)
    py.press('tab')
    py.write('admin@gmail.com')
    py.press('tab')
    py.write('12345')
    py.press('tab')
    py.press('enter')
    sleep(2)
    ler_db()


def ler_db():
    global tabela
    tabela = pd.read_csv('Python Power Up/produtos.csv')
    for i in range(len(tabela)):
        cad_produtos(i)


def cad_produtos(i):
    py.click(750, 250)
    for name in list(tabela.columns):
        cod = tabela.loc[i, name]
        if pd.isna(cod):
            py.press('tab')
        else:
            py.write(str(cod))
            py.press('tab')
    py.press('enter')
    py.press('home')


abrir_opera()
