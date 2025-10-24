"""
Atividade 2: Desafio IBGE + Plotly
Análise e visualização de dados demográficos do Brasil
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def carregar_dados():
    """Carrega e explora os dados"""
    df = pd.read_csv('dados/populacao_estados.csv')
    
    print("=" * 60)
    print("DESAFIO IBGE + PLOTLY")
    print("=" * 60)
    print("\n1. EXPLORAÇÃO DOS DADOS\n")
    
    print("Primeiras linhas:")
    print(df.head())
    print()
    
    print("Informações do dataset:")
    print(df.info())
    print()
    
    print("Estatísticas descritivas:")
    print(df[['populacao', 'area_km2']].describe())
    print()
    
    return df


def analise_exploratoria(df):
    """Análise exploratória dos dados"""
    print("\n2. ANÁLISE EXPLORATÓRIA\n")
    
    # Top 5 estados mais populosos
    print("Top 5 estados mais populosos:")
    top5 = df.nlargest(5, 'populacao')
    for idx, row in top5.iterrows():
        print(f"   {row['estado']:20s} - {row['populacao']:>12,} habitantes")
    print()
    
    # Bottom 5
    print("5 estados menos populosos:")
    bottom5 = df.nsmallest(5, 'populacao')
    for idx, row in bottom5.iterrows():
        print(f"   {row['estado']:20s} - {row['populacao']:>12,} habitantes")
    print()
    
    # População por região
    print("População total por região:")
    pop_regiao = df.groupby('regiao')['populacao'].sum().sort_values(ascending=False)
    for regiao, pop in pop_regiao.items():
        porcentagem = (pop / df['populacao'].sum() * 100)
        print(f"   {regiao:15s} - {pop:>12,} habitantes ({porcentagem:.1f}%)")
    print()
    
    # Densidade demográfica
    df['densidade'] = df['populacao'] / df['area_km2']
    print("Top 5 estados com maior densidade demográfica:")
    top5_densidade = df.nlargest(5, 'densidade')
    for idx, row in top5_densidade.iterrows():
        print(f"   {row['estado']:20s} - {row['densidade']:>8.2f} hab/km²")
    print()
    
    return df


def criar_visualizacoes(df):
    """Cria visualizações com Plotly"""
    print("\n3. VISUALIZAÇÕES\n")
    print("Gerando gráficos interativos...")
    
    # 1. Gráfico de barras - Top 10 estados
    fig1 = px.bar(
        df.nlargest(10, 'populacao'),
        x='estado',
        y='populacao',
        title='Top 10 Estados Mais Populosos do Brasil',
        labels={'populacao': 'População', 'estado': 'Estado'},
        color='populacao',
        color_continuous_scale='Viridis',
        text='populacao'
    )
    fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig1.update_layout(showlegend=False)
    fig1.write_html('grafico_top10_estados.html')
    print("   ✓ Gráfico de barras criado: grafico_top10_estados.html")
    
    # 2. Gráfico de pizza - Distribuição por região
    pop_regiao = df.groupby('regiao')['populacao'].sum().reset_index()
    fig2 = px.pie(
        pop_regiao,
        values='populacao',
        names='regiao',
        title='Distribuição da População Brasileira por Região',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    fig2.write_html('grafico_populacao_regiao.html')
    print("   ✓ Gráfico de pizza criado: grafico_populacao_regiao.html")
    
    # 3. Scatter plot - População vs Área
    fig3 = px.scatter(
        df,
        x='area_km2',
        y='populacao',
        size='densidade',
        color='regiao',
        hover_name='estado',
        title='População vs Área (tamanho = densidade demográfica)',
        labels={
            'area_km2': 'Área (km²)',
            'populacao': 'População',
            'regiao': 'Região'
        },
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig3.write_html('grafico_populacao_area.html')
    print("   ✓ Gráfico de dispersão criado: grafico_populacao_area.html")
    
    # 4. Gráfico de barras horizontais - Densidade demográfica
    df_sorted = df.sort_values('densidade', ascending=True).tail(15)
    fig4 = px.bar(
        df_sorted,
        x='densidade',
        y='estado',
        orientation='h',
        title='Top 15 Estados - Densidade Demográfica',
        labels={'densidade': 'Habitantes por km²', 'estado': 'Estado'},
        color='densidade',
        color_continuous_scale='RdYlGn'
    )
    fig4.write_html('grafico_densidade.html')
    print("   ✓ Gráfico de densidade criado: grafico_densidade.html")
    
    # 5. Box plot por região
    fig5 = px.box(
        df,
        x='regiao',
        y='populacao',
        title='Distribuição da População por Região',
        labels={'populacao': 'População', 'regiao': 'Região'},
        color='regiao'
    )
    fig5.write_html('grafico_boxplot_regiao.html')
    print("   ✓ Box plot criado: grafico_boxplot_regiao.html")


def desafio_extra(df):
    """Responde às questões do desafio extra"""
    print("\n4. DESAFIO EXTRA\n")
    
    # 1. Região com maior densidade demográfica média
    densidade_regiao = df.groupby('regiao')['densidade'].mean().sort_values(ascending=False)
    print("1. Densidade demográfica média por região:")
    for regiao, densidade in densidade_regiao.items():
        print(f"   {regiao:15s} - {densidade:>8.2f} hab/km²")
    print(f"\n   → Região com maior densidade: {densidade_regiao.index[0]}")
    print()
    
    # 2. Correlação entre área e população
    correlacao = df['area_km2'].corr(df['populacao'])
    print(f"2. Correlação entre área e população: {correlacao:.4f}")
    print(f"   → {'Positiva' if correlacao > 0 else 'Negativa'} e {'forte' if abs(correlacao) > 0.7 else 'fraca' if abs(correlacao) < 0.3 else 'moderada'}")
    print()
    
    # 3. Estados com densidade acima da média
    densidade_media = df['densidade'].mean()
    estados_acima = df[df['densidade'] > densidade_media]
    print(f"3. Densidade média nacional: {densidade_media:.2f} hab/km²")
    print(f"   Estados com densidade acima da média: {len(estados_acima)}")
    print("\n   Estados:")
    for idx, row in estados_acima.sort_values('densidade', ascending=False).iterrows():
        print(f"   - {row['estado']:20s} ({row['densidade']:>8.2f} hab/km²)")


def main():
    """Executa o desafio completo"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "DESAFIO IBGE + PLOTLY" + " " * 22 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    try:
        # Carregar dados
        df = carregar_dados()
        
        # Análise exploratória
        df = analise_exploratoria(df)
        
        # Criar visualizações
        criar_visualizacoes(df)
        
        # Desafio extra
        desafio_extra(df)
        
        print("\n" + "=" * 60)
        print("DESAFIO CONCLUÍDO COM SUCESSO! ✓")
        print("=" * 60)
        print("\nArquivos HTML gerados:")
        print("  - grafico_top10_estados.html")
        print("  - grafico_populacao_regiao.html")
        print("  - grafico_populacao_area.html")
        print("  - grafico_densidade.html")
        print("  - grafico_boxplot_regiao.html")
        print("\nAbra os arquivos no navegador para visualizar os gráficos!")
        
    except FileNotFoundError as e:
        print(f"\n❌ Erro: Arquivo não encontrado - {e}")
        print("Certifique-se de estar no diretório '07_atividades_integradas'")
    except ImportError as e:
        print(f"\n❌ Erro: Biblioteca não encontrada - {e}")
        print("Instale com: pip install plotly")
    except Exception as e:
        print(f"\n❌ Erro ao executar análise: {e}")


if __name__ == "__main__":
    main()
