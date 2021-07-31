import datetime
from numpy.lib.function_base import append
import pandas as pd
import numpy as np


#Importando o csv de casos e mortes de covid
df = pd.read_csv('caso_full.csv', index_col=0)
#print(df)

#Importando o csv de vacinação
df2 = pd.read_csv('vacinacao_covid_full.csv')
print(df2)

dataset_indexEstados2 = df2.set_index("UF")
print(dataset_indexEstados2)

#Filtrando índices com o placetype = estados
dfestados = df.loc[df['place_type']=='state'] 
#print(dfestados)

#Criando as classes que irão comporto o índice do dataset - Atributo state é filtrado e uma lista é criada com todas as siglas de estados
estados = dfestados['state']
#print(estados)
estadosfilter = np.unique(estados)
#print(estadosfilter)
list_estadosfilter = list(set(estadosfilter))
countestados = len(list_estadosfilter)
#print(list_estadosfilter)
#print(countestados)

#criando lista de código do estado do ibge
cod_estado = dfestados['city_ibge_code']
cod_estado = np.unique(cod_estado)
cod_estado = list(set(cod_estado))
#Transformando os valores de float para inteiro
cod_estado = [int(i) for i in cod_estado]
#print(cod_estado)

#Configurando o índex do dataset
dataset_indexEstados = dfestados.set_index("state")
print (dataset_indexEstados)
#lendataset = len(dataset_indexEstados)
#print(dataset_indexEstados)
#print(lendataset)

#Criando as litas que irão compor o dataset
Populacao_Estimada = []
Casos_covid = []
Mortes_covid = []
Vacinacao_covid = []

#Criando índice para a lista de estados, pois o python necessita de um índice numérico para iterar.
c=0
for indexlist in list_estadosfilter:
    if indexlist[0] == indexlist[-1]:
        c+=1

#iterando todos     
for i, indexlist in enumerate(list_estadosfilter):
    #print (i, indexlist)
    Populacao_Estimada.append(int(dataset_indexEstados.estimated_population[list_estadosfilter[i]].mean()))
    Casos_covid.append(dataset_indexEstados.new_confirmed[list_estadosfilter[i]].sum())
    Mortes_covid.append(dataset_indexEstados.new_deaths[list_estadosfilter[i]].sum())
    Vacinacao_covid.append(dataset_indexEstados2.quantidade[list_estadosfilter[i]].sum())

'''
print("código do estado")
print(print(list_estadosfilter))
print("/h")


print("código do estado")
print(print(cod_estado))
print("/h")


print("População estimada:")
print(Populacao_Estimada)

print("/h")

print("Casos de Covid")
print(Casos_covid)
print("/h")

print('Morte de Covid')
print(Mortes_covid)
print("/h")

print('Vacinação de Covid')
print(Vacinacao_covid)
print("/h")'''

print("_________________________________***************************************___________________________________")

#Criando a tabela final   
Dataset_covid_Final = pd.DataFrame({'Estado':list_estadosfilter,'Codigo_Estado_IBGE':cod_estado, 'Populacao_Estimada':Populacao_Estimada, 'Casos_Covid':Casos_covid, 'Mortes_Covid':Mortes_covid, 'Vacinacao_Covid':Vacinacao_covid},index=list_estadosfilter,)
print(Dataset_covid_Final)

#Exportando o dataset final
#Dataset_covid_Final.to_csv('dataset_covid_minerado.csv',index=False)
