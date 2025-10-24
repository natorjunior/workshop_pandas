# 4. DataFrame

## O que é um DataFrame?

Um **DataFrame** é uma estrutura de dados bidimensional do Pandas, similar a uma planilha Excel ou tabela SQL. É a estrutura mais utilizada no Pandas!

Características:
- **Linhas e colunas** rotuladas
- **Colunas** podem ter tipos diferentes (números, texto, datas, etc.)
- **Tamanho mutável**

## Criando DataFrames

### A partir de um dicionário

```python
import pandas as pd

# Dicionário com listas
dados = {
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [25, 30, 22, 28],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília'],
    'salario': [3500, 4200, 3000, 3800]
}

df = pd.DataFrame(dados)
print(df)
```

Saída:
```
      nome  idade           cidade  salario
0      Ana     25        São Paulo     3500
1    Bruno     30   Rio de Janeiro     4200
2  Carlos     22  Belo Horizonte     3000
3    Diana     28         Brasília     3800
```

### Com índices personalizados

```python
df = pd.DataFrame(dados, index=['ID1', 'ID2', 'ID3', 'ID4'])
print(df)
```

### A partir de uma lista de dicionários

```python
dados = [
    {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Bruno', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Carlos', 'idade': 22, 'cidade': 'Belo Horizonte'}
]

df = pd.DataFrame(dados)
print(df)
```

## Índices e Acesso

### Visualizando informações básicas

```python
# Primeiras linhas
print(df.head())  # Padrão: 5 linhas

# Últimas linhas
print(df.tail(3))  # 3 últimas linhas

# Informações sobre o DataFrame
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Dimensões (linhas, colunas)
print(df.shape)

# Nome das colunas
print(df.columns)

# Nome dos índices
print(df.index)
```

### Acessando colunas

```python
# Uma coluna (retorna Series)
print(df['nome'])
# ou
print(df.nome)

# Múltiplas colunas (retorna DataFrame)
print(df[['nome', 'idade']])
```

### Acessando linhas

```python
# Por posição (iloc)
print(df.iloc[0])        # Primeira linha
print(df.iloc[0:2])      # Primeiras duas linhas

# Por rótulo (loc)
print(df.loc[0])         # Linha com índice 0
print(df.loc[0:2])       # Linhas 0 até 2 (inclusivo)
```

### Acessando células específicas

```python
# loc[linha, coluna]
print(df.loc[0, 'nome'])

# iloc[linha, coluna]
print(df.iloc[0, 0])

# Múltiplas células
print(df.loc[0:1, ['nome', 'idade']])
```

## Operações Básicas

### Adicionando colunas

```python
# Nova coluna calculada
df['salario_anual'] = df['salario'] * 12

# Nova coluna com valor fixo
df['pais'] = 'Brasil'

# Nova coluna condicional
df['categoria'] = df['idade'].apply(lambda x: 'Jovem' if x < 25 else 'Adulto')
```

### Removendo colunas

```python
# Remover uma coluna
df_novo = df.drop('pais', axis=1)

# Remover múltiplas colunas
df_novo = df.drop(['pais', 'categoria'], axis=1)

# Remover in-place (modifica o DataFrame original)
df.drop('pais', axis=1, inplace=True)
```

### Adicionando linhas

```python
# Novo registro
novo_funcionario = pd.DataFrame({
    'nome': ['Eduardo'],
    'idade': [27],
    'cidade': ['Curitiba'],
    'salario': [3600]
})

df = pd.concat([df, novo_funcionario], ignore_index=True)
```

### Removendo linhas

```python
# Remover por índice
df_novo = df.drop(0)

# Remover múltiplas linhas
df_novo = df.drop([0, 1])
```

### Ordenando dados

```python
# Ordenar por uma coluna
df_ordenado = df.sort_values('idade')

# Ordem decrescente
df_ordenado = df.sort_values('salario', ascending=False)

# Ordenar por múltiplas colunas
df_ordenado = df.sort_values(['cidade', 'idade'])
```

### Filtrando dados

```python
# Filtro simples
jovens = df[df['idade'] < 25]

# Múltiplos filtros (AND)
resultado = df[(df['idade'] > 25) & (df['salario'] > 3500)]

# Múltiplos filtros (OR)
resultado = df[(df['cidade'] == 'São Paulo') | (df['cidade'] == 'Rio de Janeiro')]

# Filtro com isin
grandes_cidades = df[df['cidade'].isin(['São Paulo', 'Rio de Janeiro'])]
```

### Agregações

```python
# Média de uma coluna
print(df['idade'].mean())

# Múltiplas estatísticas
print(df['salario'].agg(['mean', 'median', 'std']))

# Agrupar e agregar
print(df.groupby('cidade')['salario'].mean())
```

## Lidando com Valores Faltantes

```python
# Verificar valores nulos
print(df.isnull())
print(df.isnull().sum())  # Contar nulos por coluna

# Remover linhas com valores nulos
df_limpo = df.dropna()

# Preencher valores nulos
df_preenchido = df.fillna(0)
df_preenchido = df.fillna({'idade': 0, 'salario': df['salario'].mean()})
```

## Renomeando Colunas

```python
# Renomear colunas específicas
df_renomeado = df.rename(columns={'nome': 'nome_completo', 'idade': 'anos'})

# Renomear todas as colunas
df.columns = ['NOME', 'IDADE', 'CIDADE', 'SALARIO']
```

## Exemplo Completo

```python
import pandas as pd

# Criar DataFrame
funcionarios = pd.DataFrame({
    'nome': ['Ana Silva', 'Bruno Costa', 'Carlos Santos', 'Diana Oliveira'],
    'idade': [25, 30, 22, 28],
    'departamento': ['TI', 'RH', 'TI', 'Vendas'],
    'salario': [3500, 4200, 3000, 3800],
    'anos_empresa': [2, 5, 1, 3]
})

print("=== DADOS ORIGINAIS ===")
print(funcionarios)
print()

print("=== INFORMAÇÕES BÁSICAS ===")
print(f"Dimensões: {funcionarios.shape}")
print(f"Colunas: {list(funcionarios.columns)}")
print()

print("=== ESTATÍSTICAS ===")
print(funcionarios.describe())
print()

# Adicionar coluna calculada
funcionarios['salario_anual'] = funcionarios['salario'] * 12

print("=== SALÁRIO MÉDIO POR DEPARTAMENTO ===")
print(funcionarios.groupby('departamento')['salario'].mean())
print()

print("=== FUNCIONÁRIOS DE TI ===")
funcionarios_ti = funcionarios[funcionarios['departamento'] == 'TI']
print(funcionarios_ti)
print()

print("=== TOP 2 SALÁRIOS ===")
top_salarios = funcionarios.nlargest(2, 'salario')
print(top_salarios[['nome', 'salario']])
```

## Próximos Passos

Agora vamos aprender a ler dados de arquivos: [Leitura de Arquivos](../05_leitura_arquivos)
