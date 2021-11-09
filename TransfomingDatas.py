import pandas as pd
import datetime

diaH = datetime.date.today().day
mesH = datetime.date.today().month
anoH = datetime.date.today().year
newFileName = f'Dados_Tratados_{diaH}_{mesH}_{anoH}'

path = 'I:/Documentos/Programacao/Projetos de Python/Tratamento/GrossFile.csv'
df = pd.read_csv(path,delimiter=";",header=0)
df.head()

#Função para substituir . por / das colunas da lista "cols"
def substituiDatas(newFile):    
    cols = ['CRDD', 'Planned Deadline'] #List of used columns
    for col in cols:
        df[col] = df[col].str.replace('.','/',regex=True) #
        df.to_excel(f'I:/Documentos/Programacao/Projetos de Python/Tratamento/{newFile}.xlsx',sheet_name='Dados tratados', na_rep='')

substituiDatas(newFile=newFileName)
