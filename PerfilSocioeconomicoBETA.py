import codecs
import os
import numpy as np
import pandas as pd
import psycopg2
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import csv
from pandas import DataFrame

arquivoCSV = sg.popup_get_file('Escolha um arquivo', background_color='DarkOrange1')
df = pd.read_csv(arquivoCSV)
use_custom_titlebar = False

listBox = df.columns[1:]
print(listBox)


def make_window(theme='Dark'):
    NAME_SIZE = 40

    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)


    layout_l = [[name('Selecione o grafico a ser mostrado'),
                 sg.LB(values=listBox[0:85], key='-LB-', bind_return_key=True, enable_events=True, no_scrollbar=True,  s=(80,10)), ],]


    layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('SOCIOECONÔMICO', font='_ 18', justification='c', expand_x=True)],
              [sg.Col(layout_l)]]

    window = sg.Window('Interface Perfil Socioeconômico', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)
                                                  # Show 30% complete on ProgressBar
    return window

# Start of the program...
window = make_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-LB-':
        gerador = values[event]
        contar = df[gerador]
        contar.value_counts()
        plt.pie(contar.value_counts())
        plt.show()
        print(contar)


window.close()
