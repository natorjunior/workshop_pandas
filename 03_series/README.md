# 3. Series

## O que é uma Series?

Uma **Series** é uma estrutura de dados unidimensional do Pandas, similar a uma lista ou array, mas com índices rotulados.

Pense nela como uma **coluna** de uma planilha Excel.

## Criando Series

### A partir de uma lista

```python
import pandas as pd

# Series simples
notas = pd.Series([7.5, 8.0, 6.5, 9.0])
print(notas)
```

Saída:
```
0    7.5
1    8.0
2    6.5
3    9.0
dtype: float64
```

### Com índices personalizados

```python
notas = pd.Series([7.5, 8.0, 6.5, 9.0], 
                  index=['Ana', 'Bruno', 'Carlos', 'Diana'])
print(notas)
```

Saída:
```
Ana       7.5
Bruno     8.0
Carlos    6.5
Diana     9.0
dtype: float64
```

### A partir de um dicionário

```python
notas_dict = {
    'Ana': 7.5,
    'Bruno': 8.0,
    'Carlos': 6.5,
    'Diana': 9.0
}
notas = pd.Series(notas_dict)
print(notas)
```

## Operações Básicas

### Operações matemáticas

```python
# Adicionar 1 ponto a todas as notas
notas_bonus = notas + 1
print(notas_bonus)

# Média das notas
media = notas.mean()
print(f"Média: {media}")

# Máximo e mínimo
print(f"Maior nota: {notas.max()}")
print(f"Menor nota: {notas.min()}")
```

### Estatísticas descritivas

```python
# Resumo estatístico
print(notas.describe())
```

## Acesso e Índices

### Acesso por posição

```python
# Primeiro elemento
print(notas[0])  # ou notas.iloc[0]

# Últimos dois elementos
print(notas[-2:])
```

### Acesso por rótulo

```python
# Acessar nota da Ana
print(notas['Ana'])

# Acessar múltiplos alunos
print(notas[['Ana', 'Diana']])
```

### Filtros condicionais

```python
# Alunos com nota maior que 7
aprovados = notas[notas > 7]
print(aprovados)

# Alunos com nota entre 7 e 8
print(notas[(notas >= 7) & (notas <= 8)])
```

## Métodos Úteis

```python
# Contar elementos
print(notas.count())

# Somar todos os valores
print(notas.sum())

# Ordenar valores
print(notas.sort_values())

# Ordenar por índice
print(notas.sort_index())

# Verificar valores únicos
print(notas.unique())
```

## 🎯 Atividade Prática: Sistema de Notas de Alunos

Vamos criar um sistema simples para gerenciar notas de alunos!

### Exercício 1: Criando a Series

Crie uma Series com as notas dos seguintes alunos:
- Ana: 8.5
- Bruno: 7.0
- Carlos: 9.0
- Diana: 6.5
- Eduardo: 8.0

```python
# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
import pandas as pd

notas = pd.Series({
    'Ana': 8.5,
    'Bruno': 7.0,
    'Carlos': 9.0,
    'Diana': 6.5,
    'Eduardo': 8.0
})
print(notas)
```
</details>

### Exercício 2: Análise das Notas

Com a Series criada:
1. Calcule a média das notas
2. Encontre a maior e menor nota
3. Liste os alunos aprovados (nota >= 7)
4. Adicione 0.5 pontos de bônus para todos

```python
# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
# 1. Média
print(f"Média da turma: {notas.mean():.2f}")

# 2. Maior e menor
print(f"Maior nota: {notas.max()}")
print(f"Menor nota: {notas.min()}")

# 3. Aprovados
aprovados = notas[notas >= 7]
print("Alunos aprovados:")
print(aprovados)

# 4. Bônus
notas_com_bonus = notas + 0.5
print("\nNotas com bônus:")
print(notas_com_bonus)
```
</details>

### Exercício 3: Recuperação

Diana fez a prova de recuperação e tirou 7.5. Atualize a nota dela e recalcule a média da turma.

```python
# Seu código aqui
```

<details>
<summary>Ver solução</summary>

```python
# Atualizar nota
notas['Diana'] = 7.5

# Nova média
print(f"Nova média da turma: {notas.mean():.2f}")
print("\nNotas atualizadas:")
print(notas)
```
</details>

## Código Completo da Atividade

```python
import pandas as pd

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

print("\n=== ESTATÍSTICAS ===")
print(f"Média: {notas.mean():.2f}")
print(f"Maior nota: {notas.max()}")
print(f"Menor nota: {notas.min()}")
print(f"Desvio padrão: {notas.std():.2f}")

print("\n=== APROVADOS (nota >= 7) ===")
aprovados = notas[notas >= 7]
print(aprovados)
print(f"Taxa de aprovação: {len(aprovados)/len(notas)*100:.1f}%")

print("\n=== APÓS RECUPERAÇÃO ===")
notas['Diana'] = 7.5
print(f"Nova média: {notas.mean():.2f}")

print("\n=== NOTAS COM BÔNUS (+0.5) ===")
notas_finais = notas + 0.5
print(notas_finais)
```

## Próximos Passos

Agora que você domina Series, vamos aprender sobre **DataFrames**: [DataFrame](../04_dataframe)
