"""
Atividade Prática: Sistema de Notas de Alunos
"""

import pandas as pd

def main():
    # Criar Series de notas
    notas = pd.Series({
        'Ana': 8.5,
        'Bruno': 7.0,
        'Carlos': 9.0,
        'Diana': 6.5,
        'Eduardo': 8.0
    })

    print("=== NOTAS DA TURMA ===")
    print(notas)
    print()

    # Estatísticas
    print("=== ESTATÍSTICAS ===")
    print(f"Média: {notas.mean():.2f}")
    print(f"Maior nota: {notas.max()}")
    print(f"Menor nota: {notas.min()}")
    print(f"Desvio padrão: {notas.std():.2f}")
    print()

    # Alunos aprovados
    print("=== APROVADOS (nota >= 7) ===")
    aprovados = notas[notas >= 7]
    print(aprovados)
    print(f"Taxa de aprovação: {len(aprovados)/len(notas)*100:.1f}%")
    print()

    # Recuperação
    print("=== APÓS RECUPERAÇÃO ===")
    notas['Diana'] = 7.5
    print(f"Nova nota da Diana: {notas['Diana']}")
    print(f"Nova média da turma: {notas.mean():.2f}")
    print()

    # Bônus
    print("=== NOTAS COM BÔNUS (+0.5) ===")
    notas_finais = notas + 0.5
    print(notas_finais)

if __name__ == "__main__":
    main()
