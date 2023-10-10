'''Para fazer o desafio, use o seguinte csv:
http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/9664de94-9f07-4adc-848d-b6ef56510762 

Usando a biblioteca pandas, faça alguns filtros  no dataset do link anterior

1-Selecione as pessoas vacinadas de Recife do sexo feminino da cor parda e preta maior de 60 anos
2-Selecione as pessoas  que se vacinaram nos meses de abril e maio do sexo masculino
Além do código, escreva no reade.me como você chegou na solução.'''

import pandas as pd
#1Questao
df_arquivo= pd.read_csv("C:/Users/PC/Downloads/vacinados.csv",sep=",")
df_arquivo[(df_arquivo['sexo']=='FEMININO') & ((df_arquivo['raca_cor']=='PARDA') | (df_arquivo['raca_cor']=='PRETA')) & (df_arquivo['idade']>60) ]
#2Questao
df_arquivo['data_vacinacao']= pd.to_datetime(df_arquivo['data_vacinacao'])
segunda_consulta= df_arquivo[(df_arquivo['data_vacinacao'].dt.month.isin([11,12])) & (df_arquivo['sexo']=='MASCULINO')]
