# Projeto de Dados - Corretora Internacional

Este projeto simula o pipeline de dados de uma corretora internacional com foco em:

- Conversão de leads
- Previsão de crescimento
- Detecção de fraudes
- Visualização com dashboards interativos (Streamlit)

Todos os dados foram gerados de forma sintética com controle de crescimento e padrões realistas, refletindo o comportamento esperado de uma operação de marketing digital no mercado financeiro.

---

## 📘 Notebooks Principais

- [🔁 ETL e Geração de Leads Simulados](./Notebooks/ETL/gerador_leads_fake.ipynb)
- [📊 Análise Preditiva de Conversão](./Notebooks/Modelagem/preditivo_conversao_e_crescimento_final.ipynb)
- [🔍 Detecção de Fraudes (Anomalias)](./Notebooks/Fraude/deteccao_anomalias.ipynb)
- [📈 Dashboard Interativo com Streamlit](./App/app_dashboard.py)

---

## 🚀 Tecnologias Utilizadas

- Python (Pandas, NumPy, Faker, Scikit-Learn)
- Visualização: Matplotlib, Seaborn, Streamlit
- Organização: Pathlib, Estrutura modular
- Geração de dados simulados com crescimento progressivo

---

## 🗂 Estrutura do Projeto

```bash
PROJETO_DADOS_CORRETORA/
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

## 📈 Resultados Esperados

- 📊 Indicadores de performance por canal, país e perfil
- 🤖 Modelo de conversão de leads com explicação das variáveis
- 🕵️‍♂️ Identificação de usuários com comportamento suspeito
- 📉 Previsão de crescimento da base de leads para os próximos meses
- 📬 Relatórios gerados automaticamente em PDF

---

## ✨ Próximos Passos

- [ ] Integração com base de dados real
- [ ] Deploy dos dashboards com autenticação
- [ ] Geração automática de alertas via Telegram
- [ ] Enriquecimento de dados com fontes externas (IP, localização, etc.)

---

## 👤 Autor

**Leonardo Barbosa**  
Analista de Dados com foco em Business Intelligence e Prevenção de Riscos  
Instrutor do MBA em Ciência de Dados da CBF Academy  
🔗 [GitHub](https://github.com/leojoker)  
🔗 [LinkedIn](https://www.linkedin.com/in/leonardo-barbosa777/)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
---
