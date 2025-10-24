# 7. Atividades Integradas

Bem-vindo às atividades práticas! Aqui você aplicará todos os conceitos aprendidos em desafios reais.

## 📊 Estrutura das Atividades

1. **Atividades com CSV** - Manipulação de dados geométricos
   - Análise de linha
   - Análise diagonal
   - Cálculo de área verde
   
2. **Desafio IBGE + Plotly** - Visualização de dados demográficos

---

## 🎯 Atividade 1: Análise de Dados em CSV

### Contexto

Você recebeu três arquivos CSV com dados diferentes e precisa realizar análises específicas em cada um.

### 1.1 - Análise de Linha (linha.csv)

**Objetivo:** Analisar dados dispostos em linha e extrair informações estatísticas.

**Arquivo:** `dados/linha.csv`

**Tarefas:**
1. Carregar o arquivo CSV
2. Calcular a média dos valores
3. Encontrar o valor máximo e mínimo
4. Contar quantos valores são maiores que a média

```python
import pandas as pd

# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
import pandas as pd

# Carregar dados
df = pd.read_csv('dados/linha.csv')

print("=== ANÁLISE DE LINHA ===")
print(f"Dados:\n{df}")
print()

# Análise
media = df['valor'].mean()
maximo = df['valor'].max()
minimo = df['valor'].min()
acima_media = (df['valor'] > media).sum()

print(f"Média: {media:.2f}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Valores acima da média: {acima_media}")
```
</details>

### 1.2 - Análise Diagonal (diagonal.csv)

**Objetivo:** Trabalhar com dados em formato de matriz e calcular a soma da diagonal principal.

**Arquivo:** `dados/diagonal.csv`

**Tarefas:**
1. Carregar o arquivo CSV (matriz 5x5)
2. Extrair os valores da diagonal principal
3. Calcular a soma da diagonal
4. Identificar o maior valor da diagonal

```python
import pandas as pd

# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv('dados/diagonal.csv', index_col=0)

print("=== ANÁLISE DIAGONAL ===")
print(f"Matriz:\n{df}")
print()

# Extrair diagonal
diagonal = np.diag(df.values)

print(f"Diagonal: {diagonal}")
print(f"Soma da diagonal: {diagonal.sum()}")
print(f"Maior valor da diagonal: {diagonal.max()}")
```
</details>

### 1.3 - Análise de Área Verde (area_verde.csv)

**Objetivo:** Analisar dados de áreas verdes em diferentes bairros de uma cidade.

**Arquivo:** `dados/area_verde.csv`

**Tarefas:**
1. Carregar o arquivo CSV
2. Calcular o total de área verde por região
3. Identificar os 3 bairros com maior área verde
4. Calcular a porcentagem de área verde por bairro

```python
import pandas as pd

# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
import pandas as pd

# Carregar dados
df = pd.read_csv('dados/area_verde.csv')

print("=== ANÁLISE DE ÁREA VERDE ===")
print(f"Dados:\n{df}")
print()

# Análise
print("Total por região:")
total_regiao = df.groupby('regiao')['area_verde_m2'].sum()
print(total_regiao)
print()

print("Top 3 bairros com maior área verde:")
top3 = df.nlargest(3, 'area_verde_m2')
print(top3[['bairro', 'area_verde_m2']])
print()

# Porcentagem
df['porcentagem'] = (df['area_verde_m2'] / df['area_total_m2'] * 100).round(2)
print("Porcentagem de área verde por bairro:")
print(df[['bairro', 'porcentagem']])
```
</details>

---

## 🌍 Atividade 2: Desafio IBGE + Plotly

### Contexto

Você trabalhará com dados demográficos do IBGE e criará visualizações interativas usando Plotly.

### Dataset

Utilizaremos dados de população por estado brasileiro.

**Arquivo:** `dados/populacao_estados.csv`

### Tarefas

1. **Carregar e explorar os dados**
   - Carregar o CSV
   - Visualizar as primeiras linhas
   - Verificar tipos de dados

2. **Análise exploratória**
   - Estados mais populosos (Top 5)
   - Estados menos populosos (Bottom 5)
   - População média por região
   - Densidade demográfica

3. **Visualizações com Plotly**
   - Gráfico de barras: Top 10 estados mais populosos
   - Gráfico de pizza: Distribuição por região
   - Gráfico de dispersão: População vs Área
   - Mapa coroplético do Brasil

### Código Base

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Carregar dados
df = pd.read_csv('dados/populacao_estados.csv')

# 2. Exploração
print("=== DADOS DO IBGE ===")
print(df.head())
print()
print(df.info())
print()

# 3. Análise
print("=== TOP 5 ESTADOS MAIS POPULOSOS ===")
top5 = df.nlargest(5, 'populacao')
print(top5[['estado', 'populacao']])
print()

# 4. Visualizações
# Gráfico de barras
fig = px.bar(
    df.nlargest(10, 'populacao'),
    x='estado',
    y='populacao',
    title='Top 10 Estados Mais Populosos',
    labels={'populacao': 'População', 'estado': 'Estado'},
    color='populacao',
    color_continuous_scale='Viridis'
)
fig.show()

# Gráfico de pizza
pop_regiao = df.groupby('regiao')['populacao'].sum().reset_index()
fig = px.pie(
    pop_regiao,
    values='populacao',
    names='regiao',
    title='Distribuição da População por Região'
)
fig.show()
```

### Desafio Extra

Crie uma análise completa que responda:
1. Qual região tem a maior densidade demográfica média?
2. Qual a correlação entre área e população?
3. Quais estados têm densidade acima da média nacional?

Veja o arquivo `desafio_ibge.py` para a solução completa!

---

## 📝 Código Completo das Atividades

Execute os seguintes arquivos para ver as soluções:

- `atividade_csv.py` - Todas as análises de CSV
- `desafio_ibge.py` - Análise completa com Plotly

---

## 🎓 Certificação

Parabéns! Você completou o Workshop de Pandas! 🎉

### O que você aprendeu:
- ✅ Conceitos fundamentais de Series e DataFrame
- ✅ Operações e manipulação de dados
- ✅ Leitura e escrita de arquivos (CSV, Excel, JSON)
- ✅ Filtragem e seleção com query(), loc e iloc
- ✅ Análise exploratória de dados
- ✅ Visualização com Plotly

### Próximos Passos:
1. Pratique com seus próprios datasets
2. Explore a documentação oficial do Pandas
3. Aprenda sobre limpeza de dados avançada
4. Estude Machine Learning com Scikit-learn
5. Aprenda sobre Big Data com Dask ou PySpark

## 📚 Recursos Adicionais

- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Plotly Documentation](https://plotly.com/python/)
- [IBGE - Dados Abertos](https://www.ibge.gov.br/)

---

**Obrigado por participar do Workshop!** 🚀
