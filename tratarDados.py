import csv

import pandas as pd

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import datetime
from datetime import datetime, date
from dateutil.relativedelta import relativedelta




def file_browser_window(theme='Black'):
    sg.theme(theme)
    layout_fb = [#[sg.Input(), sg.FileBrowse('Escolha um arquivo', k='-FILEBROWSE-')],
                 # [sg.Radio('Ler CSV', "OPCAO", default=True, size=(8, 4), k='-CSV-'),
                 # sg.Radio('Ler Excel', "OPCAO", size=(8, 4), k='-EXCEL-')],
                 [sg.Ok('Continuar'), sg.Cancel('Sair')]

                 ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_fb, finalize=True, size=(800, 300))


def make_window(theme='Black'):
    NAME_SIZE = 40

    def name(name):
        dots = NAME_SIZE - len(name) - 2
        return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')

    sg.theme(theme)

    layout_tela = [[sg.T('SOCIOECONÔMICO', font='_ 18', justification='c', expand_x=True)],
                   [name('Selecione o grafico a ser mostrado'),
                    sg.LB(values=listBox[0:], key='-LB-', bind_return_key=True, enable_events=True, no_scrollbar=False,
                          s=(80, 12)), ],
                   # [name('Tema da tela'),
                   # sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-TEMATELA-')],
                   [sg.Cancel('Voltar', size=(6, 4)), sg.Cancel('Sair', size=(6, 4))]]

    # window = sg.Window('Interface Perfil Socioeconômico', layout_tela, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)

    return sg.Window('Perfil Socioeconômico - Gerar graficos', layout_tela, finalize=True, size=(800, 300))


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))


    return age


# Start of the program...
janela1, janela2 = file_browser_window(), None

while True:
    window, event, values = sg.read_all_windows()

    # Fechando a interface
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Sair':
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Sair':
        break

    if window == janela1 and event == 'Continuar':
        #arquivoCSV = values['-FILEBROWSE-']
        arquivoCSV = "QUESTIONÁRIO SOCIOECONÔMICO 1.csv"
        arquivo = open(arquivoCSV)
        df = pd.read_csv(arquivoCSV)

        ##dadosIdade = pd.read_csv(arquivoCSV, usecols=[8, 9, 10])
        ##print(dadosIdade.head())
        #linhas = pd.read_csv(arquivoCSV, usecols=[8, 9, 10], skiprows=range(0), nrows=1)
        linhas = csv.reader(arquivo)
        listaDias = []
        for linha in linhas:
            if linha[8] == "1":
                linha[8] = "01"
            if linha[8] == "2":
                linha[8] = "02"
            if linha[8] == "3":
                linha[8] = "03"
            if linha[8] == "4":
                linha[8] = "04"
            if linha[8] == "5":
                linha[8] = "05"
            if linha[8] == "6":
                linha[8] = "06"
            if linha[8] == "7":
                linha[8] = "07"
            if linha[8] == "8":
                linha[8] = "08"
            if linha[8] == "9":
                linha[8] = "09"
                ######
            if linha[9] == "Janeiro":
                linha[9] = "01"
            if linha[9] == "Fevereiro":
                linha[9] = "02"
            if linha[9] == "Março":
                linha[9] = "03"
            if linha[9] == "Abril":
                linha[9] = "04"
            if linha[9] == "Maio":
                linha[9] = "05"
            if linha[9] == "Junho":
                linha[9] = "06"
            if linha[9] == "Julho":
                linha[9] = "07"
            if linha[9] == "Agosto":
                linha[9] = "08"
            if linha[9] == "Setembro":
                linha[9] = "09"
            if linha[9] == "Outubro":
                linha[9] = "10"
            if linha[9] == "Novembro":
                linha[9] = "11"
            if linha[9] == "Dezembro":
                linha[9] = "12"


            datas = (f'{linha[8]}{linha[9]}{linha[10]}')
            dia = linha[8]
            mes = linha[9]
            ano = linha[10]



            data = dia, mes, ano
            listaDias.append(data)

            #print(type(dia))
            #print(dia, mes, ano)
            #data = datetime.strptime(f'{dia}, {mes}, {ano}', '%d %b %Y')
            #print(data)
            current_time = datetime.now()
            #print(datas)


        current_time = datetime.now()
        idade = []

        for tamanho in listaDias[1:]:
            #print(tamanho)
            dataNew = (f'{tamanho[0]}/{tamanho[1]}/{tamanho[2]}')

            data = datetime.strptime(dataNew, '%d/%m/%Y')

            idade = calculateAge(data)
            print(idade)
            #idadeFinal = idade / 365
            #print(idadeFinal)
            #date_str = tamanho


        listBox = df.columns[8:11]
        janela1.hide()
        janela2 = make_window()
        #print(listaDias[1:])



    """elif window == janela1 and event == 'Continuar' and event == '-EXCEL-':
        arquivoXML = values['-FILEBROWSE-']
        df = pd.read_xml(arquivoXML)
        #listBox = df.columns[1:]
        janela1.hide()
        janela2 = make_window()"""


    # Retorna para interface anterior
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1.un_hide()

    # theme change
    """if values['-TEMATELA-'] != sg.theme():
        sg.theme(values['-TEMATELA-'])

        janela2.close()
        janela2 = make_window()"""

    if window == janela2 and event == '-LB-':
        ##0
        gerador = values[event]
        print(gerador)
        contar = df[gerador]



        ##1
        indexGraph = contar.value_counts().index
        # index2 = pd.Index(contar)
        # i2Final = index2.value_counts()
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
        # print(valoresGrafico)
        if event == '-LB-' and titleGrafico == "7-2. Em qual ano você nasceu?":
            plt.title('7-2. Idade')
            idade = contar.value_counts()
            for vezes in idade:
                print(vezes)



            # print(contar)
            plt.pie(idade, labels=vezes.index, autopct="%1.2f%%")
            ##print(idade)

        else:
            plt.pie(valoresGrafico, labels=valoresGrafico.index, autopct="%1.2f%%")
            plt.title(titleGrafico)  ##Ok
        legenda = contar.value_counts()
        plt.legend()
        plt.show()

make_window()
window.close()
