"""
Exemplo completo: Leitura de múltiplos formatos
"""

import pandas as pd
import os

def criar_dados_exemplo():
    """Cria um DataFrame de exemplo"""
    dados = {
        'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
        'categoria': ['Informática', 'Periféricos', 'Periféricos', 'Informática', 'Periféricos'],
        'preco': [2500.00, 50.00, 150.00, 800.00, 200.00],
        'estoque': [10, 50, 30, 15, 25],
        'fornecedor': ['Tech Corp', 'Tech Corp', 'Key Masters', 'Screen Pro', 'Cam Plus']
    }
    return pd.DataFrame(dados)

def salvar_em_multiplos_formatos(df):
    """Salva o DataFrame em CSV, Excel e JSON"""
    print("Salvando em diferentes formatos...")
    
    # CSV
    df.to_csv('produtos.csv', index=False, encoding='utf-8')
    print("✓ produtos.csv criado")
    
    # Excel
    df.to_excel('produtos.xlsx', index=False, sheet_name='Produtos')
    print("✓ produtos.xlsx criado")
    
    # JSON
    df.to_json('produtos.json', orient='records', indent=2, force_ascii=False)
    print("✓ produtos.json criado")

def ler_e_comparar():
    """Lê os arquivos salvos e compara"""
    print("\n=== Lendo CSV ===")
    df_csv = pd.read_csv('produtos.csv')
    print(df_csv.head())
    
    print("\n=== Lendo Excel ===")
    df_excel = pd.read_excel('produtos.xlsx')
    print(df_excel.head())
    
    print("\n=== Lendo JSON ===")
    df_json = pd.read_json('produtos.json')
    print(df_json.head())
    
    return df_csv

def analise_dados(df):
    """Faz uma análise rápida dos dados"""
    print("\n=== ANÁLISE ===")
    print(f"Total de produtos: {len(df)}")
    print(f"Valor total em estoque: R$ {(df['preco'] * df['estoque']).sum():.2f}")
    print(f"\nProdutos por categoria:")
    print(df['categoria'].value_counts())
    print(f"\nEstatísticas de preço:")
    print(df['preco'].describe())

def main():
    # Criar dados de exemplo
    df = criar_dados_exemplo()
    print("=== DADOS CRIADOS ===")
    print(df)
    print()
    
    # Salvar em múltiplos formatos
    salvar_em_multiplos_formatos(df)
    
    # Ler e comparar
    df_lido = ler_e_comparar()
    
    # Análise
    analise_dados(df_lido)
    
    # Limpar arquivos (opcional)
    # os.remove('produtos.csv')
    # os.remove('produtos.xlsx')
    # os.remove('produtos.json')

if __name__ == "__main__":
    main()
