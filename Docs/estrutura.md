# 🧠 Estrutura do Projeto - ETL de Leads | Corretora Internacional

Este documento descreve a estrutura de pastas, módulos e responsabilidades do projeto de análise e tratamento de dados de leads, baseado em arquivos CSV exportados de um CRM.

---

## 📁 Estrutura Geral

```
Projeto_Dados_Corretora/
├── App/                      # Dashboards e relatórios automatizados
│   ├── dashboard.py
│   ├── dashboard_fraude.py
│   └── export_suspeitos.py
│
├── Data/
│   ├── RAW/                  # Dados brutos simulados (por semana)
│   │   └── FULL_SIMULATED/{ano}/{mes}/{ano_mes_semana}.csv
│   ├── PROCESSED/            # Dados tratados para análises
│   └── FINAL/                # Dados finais para Power BI e relatórios
│
├── Docs/                     # Documentação técnica e estratégica
│   ├── CONTRIBUTING.md
│   ├── estrutura.md
│   ├── planner_estudo_corretora.md
│   ├── README_en.md
│   ├── ROADMAP.md
│   └── relatorio_leads_corretora.pdf
│
├── Images/                   # Imagens para README, docs, dashboards
│   └── banner_github_project.png
│
├── Notebooks/                # Cadernos organizados por módulo
│   ├── ETL/
│   │   ├── ETL_Leads.ipynb
│   │   └── gerador_leads_semanal.ipynb
│   ├── EDA/
│   │   └── analyze_leads_completo.ipynb
│   ├── Modelagem/
│   │   ├── preditivo_conversao_corrigido.ipynb
│   │   └── preditivo_corrigido_mes_ano_modelo.ipynb
│   └── Fraude/
│       └── fraude_anomalias_leads.ipynb
│
├── Src/
│   └── Utils/                # Funções reutilizáveis e caminhos do projeto
│       ├── __init__.py
│       ├── io.py
│       └── paths.py
│
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🔧 Módulos Utilitários

### `Utils/paths.py`
Contém funções para localizar diretórios do projeto:

- `get_project_root()`: raiz do projeto
- `get_data_dir("RAW")`: caminho para subpastas de dados (`RAW`, `PROCESSED`, `FINAL`)
- `get_notebook_dir()`: caminho da pasta de notebooks

### `Utils/io.py`
Funções auxiliares para leitura e gravação de dados:

- `save_csv(df, path, filename)`: salva um DataFrame em CSV na pasta desejada

---

## 🧪 Teste

### `test_paths.py`
Permite testar se os diretórios principais estão sendo resolvidos corretamente.

---

## 📌 Observações
- O projeto está preparado para crescer com visualizações em Power BI, Streamlit ou análise preditiva com Python.
- Toda a estrutura foi pensada para ser reutilizável, clara e portátil entre ambientes.

---

## 👨‍💼 Autor
Leonardo Barbosa  
Instrutor do MBA em Ciência de Dados - CBF Academy  
[LinkedIn](https://www.linkedin.com/in/leonardo-barbosa777)
