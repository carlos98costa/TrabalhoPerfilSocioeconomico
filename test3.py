import codecs
import os
import numpy as np
import pandas as pd
import psycopg2
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import csv
from pandas import DataFrame
from collections import Counter

#arquivoCSV = sg.popup_get_file('Escolha um arquivo')
arquivoCSV = 'QUESTIONÁRIO SOCIOECONÔMICO 1 (1).csv'
df = pd.read_csv(arquivoCSV)
df_novo = df['2. Qual o período cursado?']
print(df_novo.value_counts())
plt.pie(df_novo.value_counts())
plt.show()
