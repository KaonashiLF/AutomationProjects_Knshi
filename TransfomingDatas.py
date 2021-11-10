import pandas as pd
import datetime
#import pyautogui as pg
import time

diaH = datetime.date.today().day
mesH = datetime.date.today().month
anoH = datetime.date.today().year
newFileName = f'Dados_Tratados_{diaH}_{mesH}_{anoH}'

path = 'I:/Documentos/Programacao/Projetos de Python/Tratamento/GrossFile.csv'
df = pd.read_csv(path,delimiter=";",header=0)
df.head()

colsDate=['CRDD', 'Planned Deadline']
colsAPA='Shipment Number'
colsBPB='SBU'
colsLI='LeveIndicator'
nullValue=''
bar='/'
dot='.'
colsI='Indicator'
numA = 1
print(type(colsI))
def extraiExcel():
    df.to_excel(f'I:/Documentos/Programacao/Projetos de Python/Tratamento/{newFileName}.xlsx',sheet_name='Dados tratados', na_rep='') #Extração do datafame para um arquivo em excel

#Função para substituir . por / das colunas da lista "cols"
def replaceValues(colunas,toreplace,replaced):
    if type(colunas) is list: #Verifica se o valor recebido no parâmetro "colunas" é do tipo lista
        for col in colunas: #Se for do tipo lista, ele irá ler os itens desta lista e para cada item, ele irá executar o código abaixo
            df[col] = df[col].str.replace(toreplace,replaced,regex=True) #Para cada item (col) da minha lista (colunas), ele irá executar a substituição
            df.head(10)
    elif type(colunas) is str:
        df[colunas] = df[colunas].str.replace(toreplace,replaced,regex=True) #Se for do tipo string, irá realizar a substituição
    else:
        print('Erro!')
        time.sleep(10)
        #pg.alert(title='Erro',text=f'Os tipos de variáveis aceitos são: list e string.\n\nO tipo da variável inputada é:\n{type(colunas)}')


#Tratamento de substituição de valores
replaceValues(
    colunas=colsDate,
    toreplace='.',
    replaced='/'
    )

replaceValues(
    colunas=colsBPB,
    toreplace='BPB/',
    replaced=''
    )

replaceValues(
    colunas=colsAPA,
    toreplace='APA/',
    replaced=''
    )

#Função sendo executada para extrair a base tratada
extraiExcel()