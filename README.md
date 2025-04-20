# 📊 Projeto de Dados — Corretora Internacional

Este projeto foi desenvolvido com o objetivo de estruturar, automatizar e potencializar a jornada de dados de uma corretora internacional, desde a ingestão de leads até a geração de insights para tomada de decisão. A solução inclui ETL, análise exploratória, modelagem preditiva, detecção de fraudes e visualização interativa com dashboards e relatórios.

---

## 🚀 Objetivos

- 📥 Automatizar a ingestão de dados exportados do CRM
- 🔍 Realizar análises exploratórias por canal, país e perfil
- 📈 Construir modelos preditivos para conversão de leads e crescimento da base
- 🚨 Detectar possíveis fraudes com base em anomalias nos dados
- 🧾 Gerar relatórios gerenciais em PDF com alertas
- 📊 Criar dashboards interativos com **Streamlit**
- 🤖 Preparar o sistema para integração com **Telegram**

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

## 🛠 Tecnologias e Bibliotecas

- **Python**: pandas, numpy, scikit-learn, pathlib, faker, matplotlib, seaborn
- **Visualização**: Power BI, Streamlit
- **Modelagem**: RandomForestClassifier, métricas de classificação
- **Detecção de Fraude**: Score de risco e análise de anomalias
- **Automação**: Geração dinâmica de CSVs e pastas por semana
- **Deploy Futuro**: Integração com Telegram e relatórios por e-mail

---

## 🧪 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-corretora.git
   cd projeto-corretora
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os notebooks na seguinte ordem:
   - `Notebooks/ETL/gerador_leads_semanal.ipynb`
   - `Notebooks/ETL/ETL_Leads.ipynb`
   - `Notebooks/EDA/analyze_leads_completo.ipynb`
   - `Notebooks/Modelagem/...`
   - `Notebooks/Fraude/...`

4. Execute o dashboard (opcional):
   ```bash
   streamlit run App/dashboard.py
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