import pandas as pd

# Criando uma lista de dados para preencher a planilha
dados = []

# Número total de linhas
num_linhas = 30

# Preenchendo a lista de dados com informações fictícias
for i in range(num_linhas):
    nome = f'Devedor_{i+1}'
    valor = (i+1) * 100  # Valor fictício
    num_parcelas = i + 1
    total = valor * num_parcelas
    dados.append([nome, valor, num_parcelas, total])

# Criando o DataFrame
df = pd.DataFrame(dados, columns=['Nome', 'Valor', 'Número de Parcelas', 'Total'])

# Salvando o DataFrame em um arquivo Excel
df.to_excel('dividas.xlsx', index=False)

print("Planilha de dívidas criada com sucesso!")