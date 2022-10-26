import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt

arquivoCSV = sg.popup_get_file('Procure o seu arquivo csv para prosseguir', title='Importar', font='Arial 12', button_color='Black', background_color='grey11', text_color='white')
lerCSV = pd.read_csv(arquivoCSV)
lerCSV_df = pd.DataFrame(lerCSV)
lerCSV_df['Data de nascimento'] = ""
linha = 0

for valor in lerCSV_df.values:
    if valor[9] == 'Janeiro':
        valor[9] = 1
    elif valor[9] == 'Fevereiro':
        valor[9] = 2
    elif valor[9] == 'Março':
        valor[9] = 3
    elif valor[9] == 'Abril':
        valor[9] = 4
    elif valor[9] == 'Maio':
        valor[9] = 5
    elif valor[9] == 'Junho':
        valor[9] = 6
    elif valor[9] == 'Julho':
        valor[9] = 7
    elif valor[9] == 'Agosto':
        valor[9] = 8
    elif valor[9] == 'Setembro':
        valor[9] = 9
    elif valor[9] == 'Outubro':
        valor[9] = 10
    elif valor[9] == 'Novembro':
        valor[9] = 11
    elif valor[9] == 'Dezembro':
        valor[9] = 12

    lerCSV_df.loc[linha, 'Data de nascimento'] = f'{valor[8]}/{valor[9]}/{valor[10]}'
    linha += 1

lerCSV_df.drop(['Carimbo de data/hora', '3. Informe os 7 últimos dígitos do seu RA: (109nnnxxxxxxx) ',
             '7. Agora vamos falar sobre sua idade:\nEm qual dia você nasceu?',
             '7-1. Em qual mês você nasceu?',
             '7-2. Em qual ano você nasceu?',
             '23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em casa]',
             '23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [No trabalho]',
             '23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Na escola]',
             '23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em outros lugares]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos profissionais:]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos escolares:]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para entretenimento (músicas, vídeos, redes sociais, etc):]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para comunicação por e-mail:]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para operações bancárias:]',
             '23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para compras eletrônicas:]',
             '42. Escreva algumas linhas sobre sua história e seus sonhos de vida.'],
             inplace=True, axis=1)
list = lerCSV_df.columns[0:]

def janelaGraficos():
    sg.theme('Dark')

    layout_tela = [
        [sg.Text('QUESTIONÁRIO\nSOCIOECONÔMICO', font='20', text_color='black', justification='c', expand_x=True)],
        [sg.LB(values=list[0:], key='-input-', bind_return_key=True, enable_events=True, no_scrollbar=False,  s=(40, 4)), sg.Image(filename="fatecFranca.png")]
                ]

    janela0 = sg.Window('Gráficos', layout_tela, finalize=True,  keep_on_top=False)

    return janela0

janela0 = janelaGraficos()

while True:
    event, values = janela0.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-input-':
        valorCSV = values[event]
        contCSV = lerCSV_df[valorCSV]
        nomeGrafico = valorCSV[0]
        valueGraph = contCSV.value_counts()

        plt.pie(valueGraph,  shadow=False,  startangle=90)
        plt.title(nomeGrafico)
        plt.legend(valueGraph.index, fontsize=18, prop={'size': 5}, loc="upper left")
        plt.axis("equal")
        plt.tight_layout()
        plt.show()

print(lerCSV_df['Data de nascimento'])
janela0.close()
