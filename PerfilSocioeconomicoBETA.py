import pandas as pd

import PySimpleGUI as sg
import matplotlib.pyplot as plt


arquivoCSV = sg.popup_get_file('Escolha um arquivo', background_color='Black')
df = pd.read_csv(arquivoCSV)
use_custom_titlebar = False


listBox = df.columns[1:]





def make_window(theme=None):
    NAME_SIZE = 40

    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)


    layout_l = [[name('Selecione o grafico a ser mostrado'),
                 sg.LB(values=listBox[0:85], key='-LB-', bind_return_key=True, enable_events=True, no_scrollbar=True,  s=(80,10)), ],
                [name('Tema da tela'),
                 sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-TEMATELA-')],]


    layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('SOCIOECONÔMICO', font='_ 18', justification='c', expand_x=True)],
              [sg.Col(layout_l)]]

    window = sg.Window('Interface Perfil Socioeconômico', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    return window

# Start of the program...
window = make_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #theme change
    if values['-TEMATELA-'] != sg.theme():
        sg.theme(values['-TEMATELA-'])

        window.close()
        window = make_window()

    if event == '-LB-':
        ##0
        gerador = values[event]
        contar = df[gerador]
        print(contar)

        ##1
        refItems = []
        qtdItems = []

        for item in contar:
            refItems.append(contar.value_counts())

        print(f'Aqui está o refitem {refItems[0]}')

        test1 = refItems[0]
        indexGraph = contar.value_counts().index
        #index2 = pd.Index(contar)
        #i2Final = index2.value_counts()
        """string = index2
        str(string)
        print(string[0])
        removerXD = "'(),"
        for x in range(len(removerXD)):
            string = string.replace(removerXD[x], "")

        #print(string)"""
        ##02
        plt.clf()
        titleGrafico = gerador[0]
        valoresGrafico = contar.value_counts()
        #plt.pie(valoresGrafico, labels=list(indexGraph), wedgeprops={"ec": "k"})
        plt.pie(valoresGrafico, labels=valoresGrafico.index, autopct="%1.2f%%")
        plt.title(titleGrafico)  ##Ok
        legenda = contar.value_counts()
        plt.legend()
        plt.show()


window.close()
