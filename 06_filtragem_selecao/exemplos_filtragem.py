"""
Exemplos práticos de filtragem e seleção
"""

import pandas as pd

def criar_dataset():
    """Cria um dataset de vendas para os exemplos"""
    return pd.DataFrame({
        'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam', 'HD Externo'],
        'categoria': ['Informática', 'Periféricos', 'Periféricos', 'Informática', 'Periféricos', 'Informática'],
        'preco': [2500, 50, 150, 800, 200, 400],
        'vendidos': [10, 50, 30, 15, 25, 20],
        'estoque': [5, 100, 40, 10, 30, 15]
    })

def exemplo_query():
    """Exemplos usando query()"""
    vendas = criar_dataset()
    
    print("=== EXEMPLOS COM QUERY() ===\n")
    
    print("1. Produtos com preço entre 100 e 1000:")
    resultado = vendas.query('preco >= 100 and preco <= 1000')
    print(resultado[['produto', 'preco']])
    print()
    
    print("2. Produtos de Informática:")
    resultado = vendas.query('categoria == "Informática"')
    print(resultado[['produto', 'categoria']])
    print()
    
    print("3. Produtos com estoque crítico (< 15):")
    resultado = vendas.query('estoque < 15')
    print(resultado[['produto', 'estoque']])
    print()

def exemplo_loc():
    """Exemplos usando loc"""
    vendas = criar_dataset()
    
    print("=== EXEMPLOS COM LOC ===\n")
    
    print("1. Informática com estoque baixo:")
    resultado = vendas.loc[(vendas['categoria'] == 'Informática') & (vendas['estoque'] < 15)]
    print(resultado[['produto', 'estoque']])
    print()
    
    print("2. Seleção de colunas específicas:")
    resultado = vendas.loc[:, ['produto', 'preco', 'vendidos']]
    print(resultado)
    print()
    
    print("3. Primeira e última linha:")
    resultado = vendas.loc[[0, len(vendas)-1]]
    print(resultado)
    print()

def exemplo_iloc():
    """Exemplos usando iloc"""
    vendas = criar_dataset()
    
    print("=== EXEMPLOS COM ILOC ===\n")
    
    print("1. Top 3 produtos mais vendidos:")
    vendas_sorted = vendas.sort_values('vendidos', ascending=False)
    top3 = vendas_sorted.iloc[0:3]
    print(top3[['produto', 'vendidos']])
    print()
    
    print("2. Primeiras 2 linhas e 3 primeiras colunas:")
    resultado = vendas.iloc[0:2, 0:3]
    print(resultado)
    print()
    
    print("3. Últimas 2 linhas:")
    resultado = vendas.iloc[-2:]
    print(resultado)
    print()

def exemplo_modificacao():
    """Exemplos de modificação de dados"""
    vendas = criar_dataset()
    
    print("=== MODIFICAÇÃO DE DADOS ===\n")
    
    print("Dataset original:")
    print(vendas)
    print()
    
    # Aumentar preço dos produtos de Informática em 10%
    vendas.loc[vendas['categoria'] == 'Informática', 'preco'] *= 1.10
    
    # Calcular receita
    vendas['receita'] = vendas['preco'] * vendas['vendidos']
    
    # Marcar produtos com estoque crítico
    vendas['status'] = 'Normal'
    vendas.loc[vendas['estoque'] < 15, 'status'] = 'Crítico'
    
    print("Dataset modificado:")
    print(vendas)
    print()
    
    print("Resumo:")
    print(f"Receita total: R$ {vendas['receita'].sum():.2f}")
    print(f"Produtos em estoque crítico: {(vendas['status'] == 'Crítico').sum()}")

def main():
    exemplo_query()
    print("-" * 60)
    exemplo_loc()
    print("-" * 60)
    exemplo_iloc()
    print("-" * 60)
    exemplo_modificacao()

if __name__ == "__main__":
    main()
