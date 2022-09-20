import pandas as pd

import PySimpleGUI as sg
import matplotlib.pyplot as plt


def file_browser_window(theme='Black'):
    sg.theme(theme)
    layout_fb = [[sg.Input(), sg.FileBrowse('Escolha um arquivo', k='-FILEBROWSE-')],
                #[sg.Radio('Ler CSV', "OPCAO", default=True, size=(8, 4), k='-CSV-'),
                 #sg.Radio('Ler Excel', "OPCAO", size=(8, 4), k='-EXCEL-')],
                [sg.Ok('Continuar'), sg.Cancel('Sair')]

    ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_fb, finalize=True, size=(800, 300))
def make_window(theme='Black'):
    NAME_SIZE = 40

    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)


    layout_tela = [[sg.T('SOCIOECONÔMICO', font='_ 18', justification='c', expand_x=True)],
                [name('Selecione o grafico a ser mostrado'),
                 sg.LB(values=listBox[0:], key='-LB-', bind_return_key=True, enable_events=True, no_scrollbar=False,  s=(80,12)), ],
                #[name('Tema da tela'),
                 #sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-TEMATELA-')],
                [sg.Cancel('Voltar', size=(6, 4)), sg.Cancel('Sair', size=(6, 4))]]



    #window = sg.Window('Interface Perfil Socioeconômico', layout_tela, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)

    return sg.Window('Perfil Socioeconômico - Gerar graficos', layout_tela, finalize=True, size=(800, 300))

# Start of the program...
janela1, janela2 = file_browser_window(), None

while True:
    window,event,values = sg.read_all_windows()

    #Fechando a interface
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Sair':
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Sair':
        break

    if window == janela1 and event == 'Continuar':
        arquivoCSV = values['-FILEBROWSE-']
        df = pd.read_csv(arquivoCSV)
        listBox = df.columns[1:]
        janela1.hide()
        janela2 = make_window()
    elif window == janela1 and event == 'Continuar' and event == '-EXCEL-':
        arquivoXML = values['-FILEBROWSE-']
        df = pd.read_xml(arquivoXML)
        listBox = df.columns[1:]
        janela1.hide()
        janela2 = make_window()

    # Retorna para interface anterior
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1.un_hide()

    #theme change
    """if values['-TEMATELA-'] != sg.theme():
        sg.theme(values['-TEMATELA-'])

        janela2.close()
        janela2 = make_window()"""

    if window == janela2 and event == '-LB-':
        ##0
        gerador = values[event]
        contar = df[gerador]

        ##1
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
        plt.pie(valoresGrafico, labels=valoresGrafico.index, autopct="%1.2f%%")
        plt.title(titleGrafico)  ##Ok
        legenda = contar.value_counts()
        plt.legend()
        plt.show()

window.close()
