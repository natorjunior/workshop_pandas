# 6. Filtragem e Seleção

Agora vamos aprender as técnicas mais poderosas para filtrar e selecionar dados em um DataFrame!

## 🔍 Métodos de Seleção

Pandas oferece três métodos principais para selecionar dados:
- **query()**: Seleção usando expressões SQL-like
- **loc**: Seleção baseada em rótulos
- **iloc**: Seleção baseada em posições

## query()

O método `query()` permite filtrar dados usando uma sintaxe similar a SQL.

### Sintaxe básica

```python
import pandas as pd

# Criar DataFrame de exemplo
dados = {
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'idade': [25, 30, 22, 28, 35],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Brasília', 'São Paulo'],
    'salario': [3500, 4200, 3000, 3800, 5000]
}
df = pd.DataFrame(dados)
```

### Exemplos de query()

```python
# Filtro simples
resultado = df.query('idade > 25')
print(resultado)

# Filtro com string
resultado = df.query('cidade == "São Paulo"')
print(resultado)

# Múltiplos filtros (AND)
resultado = df.query('idade > 25 and salario > 3500')
print(resultado)

# Múltiplos filtros (OR)
resultado = df.query('cidade == "São Paulo" or cidade == "Rio de Janeiro"')
print(resultado)

# Usando variáveis externas
idade_minima = 25
resultado = df.query('idade > @idade_minima')
print(resultado)

# Operadores de comparação
resultado = df.query('idade >= 25 and idade <= 30')
print(resultado)

# in / not in
resultado = df.query('cidade in ["São Paulo", "Brasília"]')
print(resultado)

resultado = df.query('cidade not in ["Rio de Janeiro"]')
print(resultado)
```

### Vantagens do query()

- Sintaxe mais legível para filtros complexos
- Performance melhor em DataFrames grandes
- Fácil usar variáveis externas com `@`

## loc

O método `loc` seleciona dados baseado em **rótulos** (nomes de índices e colunas).

### Sintaxe: df.loc[linhas, colunas]

```python
import pandas as pd

dados = {
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'idade': [25, 30, 22, 28, 35],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Brasília', 'São Paulo'],
    'salario': [3500, 4200, 3000, 3800, 5000]
}
df = pd.DataFrame(dados)
```

### Exemplos de loc

```python
# Selecionar uma linha
print(df.loc[0])

# Selecionar múltiplas linhas
print(df.loc[0:2])  # Índices 0, 1, 2 (inclusivo!)

# Selecionar linhas específicas
print(df.loc[[0, 2, 4]])

# Selecionar linha e coluna específica
print(df.loc[0, 'nome'])

# Selecionar linhas e múltiplas colunas
print(df.loc[0:2, ['nome', 'idade']])

# Selecionar todas as linhas, colunas específicas
print(df.loc[:, ['nome', 'salario']])

# Filtro condicional
print(df.loc[df['idade'] > 25])

# Filtro com múltiplas condições
print(df.loc[(df['idade'] > 25) & (df['salario'] > 3500)])

# Modificar valores
df.loc[df['idade'] > 30, 'salario'] = df['salario'] * 1.1
```

### Com índices personalizados

```python
# DataFrame com índice personalizado
df_indexed = df.set_index('nome')

# Acessar por nome
print(df_indexed.loc['Ana'])

# Múltiplos nomes
print(df_indexed.loc[['Ana', 'Carlos']])

# Slice por nomes
print(df_indexed.loc['Ana':'Carlos'])  # Inclusivo!
```

## iloc

O método `iloc` seleciona dados baseado em **posições** (inteiros).

### Sintaxe: df.iloc[linhas, colunas]

```python
# Primeira linha
print(df.iloc[0])

# Primeiras três linhas
print(df.iloc[0:3])  # 0, 1, 2 (exclusivo!)

# Última linha
print(df.iloc[-1])

# Linhas específicas
print(df.iloc[[0, 2, 4]])

# Linha e coluna por posição
print(df.iloc[0, 0])  # Primeira linha, primeira coluna

# Múltiplas linhas e colunas
print(df.iloc[0:2, 0:3])  # 2 primeiras linhas, 3 primeiras colunas

# Todas as linhas, colunas específicas
print(df.iloc[:, [0, 3]])  # Todas linhas, colunas 0 e 3

# Slice negativo
print(df.iloc[-3:])  # Últimas 3 linhas

# Modificar por posição
df.iloc[0, 3] = 4000  # Modifica salário da primeira linha
```

## 📊 Comparação: query() vs loc vs iloc

| Característica | query() | loc | iloc |
|---------------|---------|-----|------|
| Baseado em | Expressões | Rótulos | Posições |
| Legibilidade | Alta | Média | Baixa |
| Flexibilidade | Filtros | Tudo | Tudo |
| Performance | Boa | Boa | Melhor |
| Modificação | Não | Sim | Sim |

### Quando usar cada um?

**query()**
- Filtros complexos com múltiplas condições
- Código mais legível
- Quando vem de SQL

**loc**
- Seleção por nomes de colunas
- Índices personalizados
- Modificar valores

**iloc**
- Seleção por posição
- Primeiras/últimas linhas
- Quando posição importa mais que o nome

## 🎯 Exemplos Práticos

### Exemplo 1: Análise de Vendas

```python
import pandas as pd

vendas = pd.DataFrame({
    'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam', 'HD Externo'],
    'categoria': ['Informática', 'Periféricos', 'Periféricos', 'Informática', 'Periféricos', 'Informática'],
    'preco': [2500, 50, 150, 800, 200, 400],
    'vendidos': [10, 50, 30, 15, 25, 20],
    'estoque': [5, 100, 40, 10, 30, 15]
})

# query: Produtos com preço entre 100 e 1000
print("=== Preço entre 100 e 1000 ===")
resultado = vendas.query('preco >= 100 and preco <= 1000')
print(resultado)

# loc: Produtos de Informática com estoque baixo
print("\n=== Informática com estoque < 15 ===")
resultado = vendas.loc[(vendas['categoria'] == 'Informática') & (vendas['estoque'] < 15)]
print(resultado)

# iloc: Top 3 produtos mais vendidos
print("\n=== Top 3 mais vendidos ===")
vendas_sorted = vendas.sort_values('vendidos', ascending=False)
top3 = vendas_sorted.iloc[0:3]
print(top3[['produto', 'vendidos']])
```

### Exemplo 2: Atualização de Dados

```python
# Criar cópia para modificar
df_vendas = vendas.copy()

# Aumentar preço dos produtos de Informática em 10%
df_vendas.loc[df_vendas['categoria'] == 'Informática', 'preco'] *= 1.10

# Calcular receita
df_vendas['receita'] = df_vendas['preco'] * df_vendas['vendidos']

# Marcar produtos com estoque crítico
df_vendas['status'] = 'Normal'
df_vendas.loc[df_vendas['estoque'] < 15, 'status'] = 'Crítico'

print(df_vendas)
```

### Exemplo 3: Combinando Métodos

```python
# Selecionar produtos específicos e colunas específicas
produtos_interesse = ['Notebook', 'Monitor']
colunas_interesse = ['produto', 'preco', 'estoque']

# Método 1: query + loc
resultado1 = vendas.query('produto in @produtos_interesse').loc[:, colunas_interesse]

# Método 2: loc duplo
resultado2 = vendas.loc[vendas['produto'].isin(produtos_interesse), colunas_interesse]

print(resultado1)
```

## 🔧 Técnicas Avançadas

### Múltiplas condições complexas

```python
# Operador & (AND) e | (OR)
resultado = df.loc[
    (df['idade'] > 25) & 
    (df['salario'] > 3500) & 
    (df['cidade'].isin(['São Paulo', 'Rio de Janeiro']))
]

# Usando query (mais legível)
resultado = df.query(
    'idade > 25 and salario > 3500 and cidade in ["São Paulo", "Rio de Janeiro"]'
)
```

### Seleção por padrão (regex)

```python
# Colunas que contêm 'sal'
colunas_sal = df.loc[:, df.columns.str.contains('sal')]

# Linhas onde nome começa com 'A'
linhas_a = df.loc[df['nome'].str.startswith('A')]
```

### Seleção inversa

```python
# Todos exceto primeiras 2 linhas
resultado = df.iloc[2:]

# Todas colunas exceto 'nome'
colunas_sem_nome = df.loc[:, df.columns != 'nome']

# Usando drop
resultado = df.drop(columns=['nome'])
```

## 📝 Exercícios

Veja o arquivo `exercicios_filtragem.py` para praticar!

## Próximos Passos

Agora vamos aplicar tudo que aprendemos em atividades práticas: [Atividades Integradas](../07_atividades_integradas)
