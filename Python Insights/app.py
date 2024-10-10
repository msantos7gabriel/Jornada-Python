import pandas as pd
import numpy as np
import plotly.express as px

# Import da base de dados
tabela = pd.read_csv('python insights/cancelamentos_sample.csv')

# Dropando uma coluna inútil
tabela = tabela.drop(columns='CustomerID')

# Dropando as tabelas com colunas(alguma) vazias
tabela = tabela.dropna()

# Contando os valores da tabela
# cancelou = tabela['cancelou'].value_counts()

# em percentual = normalizado
cancelou = tabela['cancelou'].value_counts(normalize=True)
print(cancelou.map("{:.1%}".format))

for coluna in list(tabela.columns):
    # Criando o gráfico
    gráfico = px.histogram(tabela, x=coluna, color='cancelou', text_auto=True)
    # Mostrando o gráfico
    # gráfico.show()

# Filtrei os valores de uma tabela com uma condição
tabela = tabela[tabela['duracao_contrato'] != 'Monthly']

tabela = tabela[tabela['dias_atraso'] <= 20]

tabela = tabela[tabela['ligacoes_callcenter'] <= 4]
# Fim Da filtragem 

cancelou = tabela['cancelou'].value_counts(normalize=True)
print(cancelou.map("{:.1%}".format))
