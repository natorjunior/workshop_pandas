# 2. Pandas - Introdução e Instalação

## O que é o Pandas?

Pandas é uma biblioteca Python de código aberto que fornece estruturas de dados de alto desempenho e fáceis de usar, além de ferramentas de análise de dados.

### Por que usar Pandas?

- **Fácil manipulação de dados:** Trabalhe com dados tabulares de forma intuitiva
- **Performance:** Operações otimizadas para grandes conjuntos de dados
- **Flexibilidade:** Suporta diversos formatos de arquivo
- **Integração:** Funciona bem com outras bibliotecas (NumPy, Matplotlib, etc.)

## Instalação

### Usando pip

```bash
pip install pandas
```

### Instalação com suporte a Excel

```bash
pip install pandas openpyxl
```

### Instalação completa (com visualização)

```bash
pip install pandas openpyxl plotly matplotlib
```

## Primeiros Passos

### Importando a biblioteca

```python
import pandas as pd
```

**Convenção:** Sempre importamos pandas como `pd` - é uma prática padrão na comunidade Python.

### Verificando a versão

```python
print(pd.__version__)
```

## Estruturas de Dados Principais

Pandas trabalha principalmente com duas estruturas de dados:

1. **Series:** Estrutura unidimensional (como uma coluna)
2. **DataFrame:** Estrutura bidimensional (como uma tabela)

### Exemplo Rápido

```python
import pandas as pd

# Criando uma Series
temperaturas = pd.Series([22, 25, 19, 23, 21])
print(temperaturas)

# Criando um DataFrame
dados = {
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [25, 30, 22],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(dados)
print(df)
```

## Recursos Úteis

- [Documentação oficial](https://pandas.pydata.org/docs/)
- [Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Próximos Passos

Vamos nos aprofundar nas **Series** na próxima seção: [Series](../03_series)
