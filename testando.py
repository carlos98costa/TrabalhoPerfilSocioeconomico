import csv
import pandas as pd
import tela_1
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import datetime, date

import tela_inicial


##CRIAR TELAS

def make_window(theme='Dark'):
    NAME_SIZE = 40


    def name(name):
        dots = NAME_SIZE - len(name) - 2
        return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')

    sg.theme(theme)

    layout_tela = [[sg.T('SOCIOECONÔMICO', font='18', justification='c', expand_x=True)],
                   [name('Selecione o grafico a ser mostrado'),
                    sg.LB(values=listBox[0:], key='-LB-', bind_return_key=True, enable_events=True,
                          no_scrollbar=False, s=(80, 12)), ],
                   [sg.Cancel('Voltar', size=(6, 4), button_color='gray'), sg.Cancel('Sair', size=(6, 4), button_color='red')]]

    return sg.Window('Perfil Socioeconômico - Gerar graficos', layout_tela, finalize=True, size=(800, 300))

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))


    return age

# Start of the program...
janela1, janela2, janela3 = None, None, tela_inicial.tela_inicial('Dark')

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
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'Sair':
        break

    if window == janela3 and event == 'Sobre':
        sg.popup('Sobre o programa', 'Programa feito para tratar o arquivo CSV coletado na primeira etapa do trabalho!', font='18', title='Sobre')
    if window == janela3 and event == 'Equipe':
        sg.popup('Nossa equipe:','Adriano', 'Carlos Adriano', 'João Pedro', 'Lauane Stefanny', 'Valter', font=10, text_color='white', title='Equipe' )
    if window == janela3 and event == 'Documentação':
        sg.popup('Documentação', 'Em breve!', font='18', title='Documentação')


    if window == janela3 and event == 'Continuar':
        janela3.hide()
        janela1 = tela_1.file_browser_window('Dark')
    if window == janela1 and event == 'Voltar':
        janela1.hide()
        janela3.un_hide()
    if window == janela1 and event == 'Continuar':
        arquivoCSV = values['-FILEBROWSE-']
        if values['-FILEBROWSE-'] == '':
            sg.popup('Nenhum arquivo foi selecionado, o programa será encerrado!', title='Erro')
        arquivo = open(arquivoCSV, "r", encoding='utf-8')
        df = pd.read_csv(arquivoCSV)


        #################DROPAR COLUNAS
        df.drop('3. Informe os 7 últimos dígitos do seu RA: (109nnnxxxxxxx) ', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em casa]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [No trabalho]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Na escola]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em outros lugares]', inplace=True,
                axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos profissionais:]',
            inplace=True, axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos escolares:]',
            inplace=True,
            axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para entretenimento (músicas, vídeos, redes sociais, etc):]',
            inplace=True,
            axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para comunicação por e-mail:]',
            inplace=True,
            axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para operações bancárias:]',
            inplace=True,
            axis=1)
        df.drop(
            '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para compras eletrônicas:]',
            inplace=True,
            axis=1)
        df.drop(
            '42. Escreva algumas linhas sobre sua história e seus sonhos de vida.',
            inplace=True,
            axis=1)

        df.rename(columns={df.columns[7]: '7. Em qual dia você nasceu?'}, inplace=True)


        ########TRATAR DADOS DA IDADE
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
                ###### SEPARAÇÃO
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

            current_time = datetime.now()

        current_time = datetime.now()
        idade = []

        for tamanho in listaDias[1:]:
            dataNew = (f'{tamanho[0]}/{tamanho[1]}/{tamanho[2]}')
            data = datetime.strptime(dataNew, '%d/%m/%Y')
            idade.append(calculateAge(data))



        ####CRIANDO A COLUNA IDADES
        df.insert(3, '3. Idades?', idade, allow_duplicates=True)
        #CRIANDO A LISTA DE COLUNAS A SEREM LIDAS
        listBox = df.columns[1:]

        janela1.hide()
        janela2 = make_window()

    ###NAO USANDO POR ENQUANTO
    elif window == janela1 and event == 'Continuar' and event == '-EXCEL-':
        arquivoXML = values['-FILEBROWSE-']
        df = pd.read_xml(arquivoXML)
        listBox = df.columns[1:]
        del listBox[0:5]
        janela1.hide()
        janela2 = make_window()

    # Retorna para interface anterior
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1.un_hide()


    #GERANDO A LISTBOX(AS PERGUNTAS)
    if window == janela2 and event == '-LB-':
        ##0
        gerador = values[event]
        contar = df[gerador]

        ##FORMATANDO O MATPLOIT(PARAMETROS)
        params = {
            'legend.fontsize': 8,
            'legend.loc': 'upper right',
            'legend.framealpha': 0,
            'legend.handlelength': 1.0,
            'legend.handleheight': 0.7
        }
        #CHAMANDO PARAMETROS
        plt.rcParams.update(params)
        ###LIMPANDO GRAFICOS ANTERIORES
        plt.clf()
        #PEGANDO A LOCALIZAÇÃO DOS TITULOS DO GRAFICO
        titleGrafico = gerador[0]
        #CONTAGEM DE VALORES
        valoresGrafico = contar.value_counts()
        ##GERANDO O GRAFICO
        plt.pie(valoresGrafico, autopct="%1.2f%%")
        #MOSTRA OS TITULOS DOS GRAFICOS EM RELAÇÃO A LOCALIZAÇÃO
        plt.title(titleGrafico)  ##Ok
        ##CONTANDO AS LEGENDAS
        legenda = contar.value_counts()
        ##GERANDO AS LEGENDAS A PARTIR DO CONTADOR
        plt.legend(valoresGrafico.index)

    ###MOSTRAR O GRAFICO GERADO
    plt.show()
##
window.close()
