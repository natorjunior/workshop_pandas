# 5. Leitura de Arquivos

Uma das principais funcionalidades do Pandas é ler dados de diversos formatos de arquivo. Vamos aprender os três formatos mais comuns!

## 📄 CSV (Comma-Separated Values)

CSV é o formato mais comum para armazenar dados tabulares.

### Lendo arquivos CSV

```python
import pandas as pd

# Ler CSV básico
df = pd.read_csv('dados.csv')

# CSV com separador diferente
df = pd.read_csv('dados.csv', sep=';')

# CSV sem cabeçalho
df = pd.read_csv('dados.csv', header=None)

# CSV com nomes de colunas personalizados
df = pd.read_csv('dados.csv', names=['col1', 'col2', 'col3'])

# Ler apenas algumas colunas
df = pd.read_csv('dados.csv', usecols=['nome', 'idade'])

# Especificar coluna como índice
df = pd.read_csv('dados.csv', index_col='id')

# Ler apenas primeiras linhas
df = pd.read_csv('dados.csv', nrows=100)
```

### Escrevendo arquivos CSV

```python
# Salvar DataFrame como CSV
df.to_csv('saida.csv', index=False)

# Com separador diferente
df.to_csv('saida.csv', sep=';', index=False)

# Com encoding específico
df.to_csv('saida.csv', encoding='utf-8', index=False)
```

### Exemplo Prático

```python
import pandas as pd

# Criar dados de exemplo
dados = {
    'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'preco': [2500, 50, 150, 800],
    'quantidade': [10, 50, 30, 15]
}
df = pd.DataFrame(dados)

# Salvar como CSV
df.to_csv('produtos.csv', index=False)

# Ler o arquivo
df_lido = pd.read_csv('produtos.csv')
print(df_lido)
```

## 📊 Excel

Pandas também suporta leitura e escrita de arquivos Excel.

### Instalação necessária

```bash
pip install openpyxl  # Para arquivos .xlsx
```

### Lendo arquivos Excel

```python
import pandas as pd

# Ler Excel (primeira planilha)
df = pd.read_excel('dados.xlsx')

# Ler planilha específica
df = pd.read_excel('dados.xlsx', sheet_name='Vendas')

# Ler múltiplas planilhas
dfs = pd.read_excel('dados.xlsx', sheet_name=None)  # Retorna dicionário

# Ler planilha por índice
df = pd.read_excel('dados.xlsx', sheet_name=0)  # Primeira planilha

# Especificar intervalo de células
df = pd.read_excel('dados.xlsx', usecols='A:C', nrows=10)
```

### Escrevendo arquivos Excel

```python
# Salvar como Excel
df.to_excel('saida.xlsx', index=False)

# Salvar múltiplas planilhas
with pd.ExcelWriter('saida.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Vendas', index=False)
    df2.to_excel(writer, sheet_name='Clientes', index=False)

# Formatar ao salvar
df.to_excel('saida.xlsx', index=False, sheet_name='Dados')
```

### Exemplo Prático

```python
import pandas as pd

# Criar dados
vendas = pd.DataFrame({
    'mes': ['Janeiro', 'Fevereiro', 'Março'],
    'vendas': [1000, 1500, 1200],
    'despesas': [800, 900, 850]
})

clientes = pd.DataFrame({
    'nome': ['João', 'Maria', 'Pedro'],
    'total_compras': [5000, 7500, 3000]
})

# Salvar em Excel com múltiplas planilhas
with pd.ExcelWriter('relatorio.xlsx', engine='openpyxl') as writer:
    vendas.to_excel(writer, sheet_name='Vendas', index=False)
    clientes.to_excel(writer, sheet_name='Clientes', index=False)

print("Excel criado com sucesso!")

# Ler de volta
vendas_lido = pd.read_excel('relatorio.xlsx', sheet_name='Vendas')
print(vendas_lido)
```

## 🔧 JSON (JavaScript Object Notation)

JSON é um formato popular para APIs e configurações.

### Lendo arquivos JSON

```python
import pandas as pd

# Ler JSON
df = pd.read_json('dados.json')

# JSON com orientação específica
df = pd.read_json('dados.json', orient='records')

# Tipos de orientação:
# - 'split': {index -> [index], columns -> [columns], data -> [values]}
# - 'records': [{column -> value}, ..., {column -> value}]
# - 'index': {index -> {column -> value}}
# - 'columns': {column -> {index -> value}}
# - 'values': apenas valores em array
```

### Escrevendo arquivos JSON

```python
# Salvar como JSON
df.to_json('saida.json', orient='records', indent=2)

# Diferentes orientações
df.to_json('saida.json', orient='records')  # Lista de objetos
df.to_json('saida.json', orient='index')    # Objeto de objetos
```

### Exemplo Prático

```python
import pandas as pd
import json

# Criar dados
dados = {
    'usuarios': [
        {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'},
        {'nome': 'Bruno', 'idade': 30, 'cidade': 'Rio de Janeiro'},
        {'nome': 'Carlos', 'idade': 22, 'cidade': 'Belo Horizonte'}
    ]
}

# Salvar JSON manualmente
with open('usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

# Ler com Pandas
df = pd.read_json('usuarios.json', orient='records')
print(df)

# Salvar com Pandas
df.to_json('usuarios_saida.json', orient='records', indent=2, force_ascii=False)
```

## 📋 Outros Formatos

Pandas suporta muitos outros formatos:

```python
# SQL
df = pd.read_sql('SELECT * FROM tabela', conexao)

# HTML
df = pd.read_html('pagina.html')[0]  # Retorna lista de DataFrames

# Parquet (formato otimizado)
df = pd.read_parquet('dados.parquet')
df.to_parquet('saida.parquet')

# Clipboard (área de transferência)
df = pd.read_clipboard()
df.to_clipboard()
```

## 🎯 Exemplo Completo: Trabalhando com Múltiplos Formatos

Veja o arquivo `exemplo_leitura.py` para um exemplo completo de leitura e conversão entre formatos.

```python
import pandas as pd

# Criar dados de exemplo
dados = {
    'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'categoria': ['Informática', 'Periféricos', 'Periféricos', 'Informática', 'Periféricos'],
    'preco': [2500.00, 50.00, 150.00, 800.00, 200.00],
    'estoque': [10, 50, 30, 15, 25],
    'fornecedor': ['Tech Corp', 'Tech Corp', 'Key Masters', 'Screen Pro', 'Cam Plus']
}

df = pd.DataFrame(dados)

# Salvar em diferentes formatos
print("Salvando em diferentes formatos...")
df.to_csv('produtos.csv', index=False, encoding='utf-8')
df.to_excel('produtos.xlsx', index=False, sheet_name='Produtos')
df.to_json('produtos.json', orient='records', indent=2, force_ascii=False)

print("Arquivos criados com sucesso!")

# Ler de volta e comparar
print("\n=== Lendo CSV ===")
df_csv = pd.read_csv('produtos.csv')
print(df_csv.head())

print("\n=== Lendo Excel ===")
df_excel = pd.read_excel('produtos.xlsx')
print(df_excel.head())

print("\n=== Lendo JSON ===")
df_json = pd.read_json('produtos.json')
print(df_json.head())

# Análise rápida
print("\n=== ANÁLISE ===")
print(f"Total de produtos: {len(df)}")
print(f"Valor total em estoque: R$ {(df['preco'] * df['estoque']).sum():.2f}")
print(f"\nProdutos por categoria:")
print(df['categoria'].value_counts())
```

## ⚠️ Dicas Importantes

1. **Encoding**: Se tiver problemas com acentos, use `encoding='utf-8'` ou `encoding='latin-1'`
2. **Performance**: Para arquivos grandes, use `chunksize` para ler em partes
3. **Memória**: Use `usecols` para ler apenas as colunas necessárias
4. **Tipos**: Use `dtype` para especificar tipos de dados e economizar memória

```python
# Ler CSV em chunks
for chunk in pd.read_csv('arquivo_grande.csv', chunksize=1000):
    processar(chunk)

# Especificar tipos
df = pd.read_csv('dados.csv', dtype={'id': int, 'valor': float})

# Tratar valores faltantes na leitura
df = pd.read_csv('dados.csv', na_values=['NA', 'N/A', 'null'])
```

## Próximos Passos

Agora que sabemos ler dados, vamos aprender a filtrar e selecionar: [Filtragem e Seleção](../06_filtragem_selecao)
