# Guia Rápido do Workshop

## 📋 Checklist de Progresso

Use este checklist para acompanhar seu progresso no workshop:

- [ ] **1. Introdução e Ambientação**
  - [ ] Configurar ambiente de trabalho
  - [ ] Instalar Jupyter/Python
  - [ ] Verificar instalação

- [ ] **2. Pandas - Introdução e Instalação**
  - [ ] Entender o que é Pandas
  - [ ] Instalar Pandas e dependências
  - [ ] Testar importação

- [ ] **3. Series**
  - [ ] Criar Series
  - [ ] Operações básicas
  - [ ] Indexação
  - [ ] ✅ Atividade: Notas de alunos

- [ ] **4. DataFrame**
  - [ ] Criar DataFrames
  - [ ] Manipular índices
  - [ ] Operações básicas
  - [ ] Adicionar/remover dados

- [ ] **5. Leitura de Arquivos**
  - [ ] Ler CSV
  - [ ] Ler Excel
  - [ ] Ler JSON
  - [ ] Escrever arquivos

- [ ] **6. Filtragem e Seleção**
  - [ ] Usar query()
  - [ ] Usar loc
  - [ ] Usar iloc
  - [ ] Filtros complexos

- [ ] **7. Atividades Integradas**
  - [ ] ✅ Análise de linha (CSV)
  - [ ] ✅ Análise diagonal (CSV)
  - [ ] ✅ Análise de área verde (CSV)
  - [ ] ✅ Desafio IBGE + Plotly

## 🎯 Ordem Recomendada

1. Siga as seções na ordem (01 → 07)
2. Leia a teoria em cada README.md
3. Execute os exemplos de código
4. Faça as atividades práticas
5. Teste diferentes variações

## 🏃 Quick Start

```bash
# Clone o repositório
git clone https://github.com/natorjunior/workshop_pandas.git
cd workshop_pandas

# Instale as dependências
pip install -r requirements.txt

# Teste a instalação
python -c "import pandas as pd; print(f'Pandas {pd.__version__} instalado!')"

# Execute uma atividade de exemplo
cd 03_series
python atividade_notas.py
```

## 📂 Estrutura de Arquivos

```
workshop_pandas/
├── README.md                          # Visão geral do workshop
├── requirements.txt                   # Dependências
│
├── 01_introducao/
│   └── README.md                      # Introdução e setup
│
├── 02_pandas_instalacao/
│   └── README.md                      # O que é Pandas
│
├── 03_series/
│   ├── README.md                      # Teoria de Series
│   └── atividade_notas.py            # ✅ Atividade prática
│
├── 04_dataframe/
│   ├── README.md                      # Teoria de DataFrame
│   └── exemplo_dataframe.py          # Exemplos práticos
│
├── 05_leitura_arquivos/
│   ├── README.md                      # Como ler arquivos
│   ├── exemplo_leitura.py            # Script de exemplo
│   ├── exemplo_produtos.csv          # Dados de exemplo
│   └── exemplo_produtos.json         # Dados de exemplo
│
├── 06_filtragem_selecao/
│   ├── README.md                      # query(), loc, iloc
│   └── exemplos_filtragem.py         # Exemplos práticos
│
└── 07_atividades_integradas/
    ├── README.md                      # Atividades finais
    ├── atividade_csv.py              # ✅ 3 análises CSV
    ├── desafio_ibge.py               # ✅ Análise IBGE
    └── dados/                         # Datasets
        ├── linha.csv
        ├── diagonal.csv
        ├── area_verde.csv
        └── populacao_estados.csv
```

## 💡 Dicas

1. **Pratique**: Execute cada exemplo de código
2. **Experimente**: Modifique os exemplos
3. **Resolva**: Tente resolver antes de ver as soluções
4. **Documente**: Faça anotações dos conceitos importantes
5. **Pergunte**: Use a documentação oficial quando tiver dúvidas

## 🔗 Links Úteis

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Plotly Python](https://plotly.com/python/)

## ❓ Troubleshooting

### Erro: ModuleNotFoundError: No module named 'pandas'
```bash
pip install pandas
```

### Erro ao ler Excel
```bash
pip install openpyxl
```

### Erro com Plotly
```bash
pip install plotly
```

### Problemas com encoding
Use `encoding='utf-8'` ao ler/escrever arquivos CSV:
```python
df = pd.read_csv('arquivo.csv', encoding='utf-8')
```

## 🎓 Certificação

Ao completar todas as atividades, você terá:
- ✅ Domínio de Series e DataFrames
- ✅ Capacidade de ler/escrever múltiplos formatos
- ✅ Habilidade de filtrar e selecionar dados
- ✅ Experiência com análise exploratória
- ✅ Conhecimento de visualização com Plotly

**Parabéns por completar o Workshop de Pandas!** 🎉
