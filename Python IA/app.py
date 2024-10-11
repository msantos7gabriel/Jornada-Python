import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

tabela = pd.read_csv('Python IA/clientes.csv')

# Na Criação de modelo de ia voce n pode ter str na sua base de dados

# Label enconder transforma o valor str para um numero inteiro equivalente
coder_profissao = LabelEncoder()
# Transformou
tabela['profissao'] = coder_profissao.fit_transform(tabela['profissao'])

coder_credito = LabelEncoder()
tabela['mix_credito'] = coder_credito.fit_transform(tabela['mix_credito'])

coder_pagamento = LabelEncoder()
tabela['comportamento_pagamento'] = coder_pagamento.fit_transform(
    tabela['comportamento_pagamento'])

# X Colunas que eu irei usar para previsão
# Y Quem eu quero prever

# 20 - 40 para teste
# 80 - 60 para treino
# Mais coluna mais dados de treino tendem a precisar
# Poucas colunas - para o teste
x = tabela.drop(columns=['score_credito', 'id_cliente'])
y = tabela['score_credito']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)


# Criar dois modelos de IA
# Arvores de decisão -> Random Florest
modelo_RF = RandomForestClassifier()

# Vizinhos Próximos (Nearest Neighbors) -> KNN
modelo_knn = KNeighborsClassifier()

# Treinando os modelo de IA
modelo_RF.fit(x_treino, y_treino)
print('Fim do Treino 1')
modelo_knn.fit(x_treino, y_treino)
print('Fim do Treino 2')

# Testando as previsão
previsão_RF = modelo_RF.predict(x_teste)
previsão_knn = modelo_knn.predict(x_teste)

# Calcular a precisão das previsões dos modelos de ai
print(f'ACC do modelo RF: {accuracy_score(y_teste, previsão_RF)}')
print(f'ACC do modelo KNN: {accuracy_score(y_teste, previsão_knn)}')


tabela_novo = pd.read_csv('python ia/novos_clientes.csv')

# Label enconder transforma o valor str para um numero inteiro equivalente
tabela_novo['profissao'] = coder_profissao.fit_transform(
    tabela_novo['profissao'])

tabela_novo['mix_credito'] = coder_credito.fit_transform(
    tabela_novo['mix_credito'])

tabela_novo['comportamento_pagamento'] = coder_pagamento.fit_transform(
    tabela_novo['comportamento_pagamento'])

previsão = modelo_RF.predict(tabela_novo)
print(previsão)
