import pandas as pd
import numpy as np

# Import da base de dados
tabela = pd.read_csv('python insights/cancelamentos.csv')

# Dropando uma coluna inútil
tabela = tabela.drop(columns='CustomerID')

# Dropando as tabelas com colunas(alguma) vazias
tabela = tabela.dropna()
print(tabela.info())
