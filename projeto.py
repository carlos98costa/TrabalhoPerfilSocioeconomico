import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

formularioCSV = sg.popup_get_file('Escolha o arquivo', title= 'Perfil Socieconomico')
df = pd.read_csv(formularioCSV)

df2 = pd.read_csv('QUESTIONÁRIO SOCIOECONÔMICO 1.csv', usecols=[8, 9, 10])

df.drop('Carimbo de data/hora', inplace = True, axis = 1)
df.drop('3. Informe os 7 últimos dígitos do seu RA: (109nnnxxxxxxx) ', inplace = True, axis = 1)
df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em casa]', inplace = True, axis = 1)
df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [No trabalho]', inplace = True, axis = 1)
df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Na escola]', inplace = True, axis = 1)
df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em outros lugares]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos profissionais:]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos escolares:]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para entretenimento (músicas, vídeos, redes sociais, etc):]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para comunicação por e-mail:]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para operações bancárias:]', inplace = True, axis = 1)
df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para compras eletrônicas:]', inplace = True, axis = 1)
df.drop('42. Escreva algumas linhas sobre sua história e seus sonhos de vida.', inplace = True, axis = 1 )

df2.rename(columns={df2.columns[0]: '7. Em qual dia você nasceu?'}, inplace=True)
list = df.columns[0:]
#Criar as janelas e estilos(layout)

def janela_pesquisa():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Escolha o grafico a ser mostrado')],
    
        [sg.LB(values=list[0:], key = 'gr', bind_return_key=True, enable_events = True, no_scrollbar=True, s=(40, 4))],

    ]
    janela1 = sg.Window('Grafico', layout, finalize = True)
    return janela1

janela1 = janela_pesquisa()

    
while True:
    event,values = janela1.read()

    #Quando janela for fechada
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'gr':
        valor = values[event]
        cont = df[valor]
        nomegr = valor[0]
        grafico = cont.value_counts()
        print(df2.columns[0])

        plt.pie(grafico, autopct = '%1.0f%%')
        plt.title(nomegr)
        plt.legend(grafico.index)
        plt.show()

janela1.close()

dia = {"1":"01", "2":"02", "3":"03", "4":"04", "5":"05", "6":"06", "7":"07", "8":"08", "9":"09", "10":"10", "11":"11", "12":"12", "13":"13",
       "14":"14", "15":"15", "16":"16", "17":"17", "18":"18", "19":"19", "20":"20", "21":"21", "22":"22", "23":"23", "24":"24", "25":25,
       "26":"26", "27":"27", "28":"28", "29":"29", "30":"30", "31":"31"}
meses = {'Janeiro': "1", "Fevereiro": "2", "Março": "3", "Abril": "4", "Maio": "5", "Junho": "6", "Julho": "7", "Agosto": "8", "Setembro": "9", "Outubro": "10", "Novembro": "11", "Dezembro": "12"}

for i in df2.index:
    dia = df2.columns[0][i]
    print(meses[df2['7-1. Em qual mês você nasceu?'][i]])
    print(dia)



