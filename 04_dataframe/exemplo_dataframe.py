"""
Exemplo completo de DataFrame
"""

import pandas as pd

def main():
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

if __name__ == "__main__":
    main()
