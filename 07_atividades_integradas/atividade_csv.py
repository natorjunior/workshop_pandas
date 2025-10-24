"""
Atividade 1: Análise de dados em CSV
Solução completa para linha, diagonal e área verde
"""

import pandas as pd
import numpy as np


def analise_linha():
    """Análise de dados em linha"""
    print("=" * 60)
    print("ATIVIDADE 1.1 - ANÁLISE DE LINHA")
    print("=" * 60)
    
    # Carregar dados
    df = pd.read_csv('dados/linha.csv')
    
    print("\nDados carregados:")
    print(df)
    print()
    
    # Análise
    media = df['valor'].mean()
    maximo = df['valor'].max()
    minimo = df['valor'].min()
    acima_media = (df['valor'] > media).sum()
    
    print("RESULTADOS:")
    print(f"Média dos valores: {media:.2f}")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
    print(f"Quantidade de valores acima da média: {acima_media}")
    print(f"Soma total: {df['valor'].sum()}")
    print(f"Desvio padrão: {df['valor'].std():.2f}")


def analise_diagonal():
    """Análise da diagonal de uma matriz"""
    print("\n" + "=" * 60)
    print("ATIVIDADE 1.2 - ANÁLISE DIAGONAL")
    print("=" * 60)
    
    # Carregar dados
    df = pd.read_csv('dados/diagonal.csv', index_col=0)
    
    print("\nMatriz carregada:")
    print(df)
    print()
    
    # Extrair diagonal
    diagonal = np.diag(df.values)
    
    print("RESULTADOS:")
    print(f"Valores da diagonal: {diagonal}")
    print(f"Soma da diagonal: {diagonal.sum()}")
    print(f"Média da diagonal: {diagonal.mean():.2f}")
    print(f"Maior valor da diagonal: {diagonal.max()}")
    print(f"Menor valor da diagonal: {diagonal.min()}")


def analise_area_verde():
    """Análise de áreas verdes"""
    print("\n" + "=" * 60)
    print("ATIVIDADE 1.3 - ANÁLISE DE ÁREA VERDE")
    print("=" * 60)
    
    # Carregar dados
    df = pd.read_csv('dados/area_verde.csv')
    
    print("\nDados carregados:")
    print(df)
    print()
    
    # Análise
    print("RESULTADOS:")
    print("\n1. Total de área verde por região:")
    total_regiao = df.groupby('regiao')['area_verde_m2'].sum().sort_values(ascending=False)
    for regiao, total in total_regiao.items():
        print(f"   {regiao}: {total:,} m²")
    
    print("\n2. Top 3 bairros com maior área verde:")
    top3 = df.nlargest(3, 'area_verde_m2')
    for idx, row in top3.iterrows():
        print(f"   {idx+1}º. {row['bairro']}: {row['area_verde_m2']:,} m²")
    
    print("\n3. Porcentagem de área verde por bairro:")
    df['porcentagem_verde'] = (df['area_verde_m2'] / df['area_total_m2'] * 100).round(2)
    df_sorted = df.sort_values('porcentagem_verde', ascending=False)
    for idx, row in df_sorted.iterrows():
        print(f"   {row['bairro']}: {row['porcentagem_verde']:.2f}%")
    
    print(f"\n4. Estatísticas gerais:")
    print(f"   Total de área verde: {df['area_verde_m2'].sum():,} m²")
    print(f"   Média de área verde por bairro: {df['area_verde_m2'].mean():,.0f} m²")
    print(f"   Porcentagem média de área verde: {df['porcentagem_verde'].mean():.2f}%")
    
    # Bairros com boa cobertura verde (> 5%)
    bairros_bons = df[df['porcentagem_verde'] > 5]
    print(f"   Bairros com > 5% de área verde: {len(bairros_bons)}")


def main():
    """Executa todas as análises"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "ATIVIDADES COM CSV - WORKSHOP PANDAS" + " " * 11 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    try:
        analise_linha()
        analise_diagonal()
        analise_area_verde()
        
        print("\n" + "=" * 60)
        print("TODAS AS ATIVIDADES CONCLUÍDAS COM SUCESSO! ✓")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"\n❌ Erro: Arquivo não encontrado - {e}")
        print("Certifique-se de estar no diretório '07_atividades_integradas'")
    except Exception as e:
        print(f"\n❌ Erro ao executar análise: {e}")


if __name__ == "__main__":
    main()
