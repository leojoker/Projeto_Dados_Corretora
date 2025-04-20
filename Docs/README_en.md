# 📊 ETL and Lead Analysis Project – International Brokerage

This project simulates a complete data pipeline (ETL) for a lead tracking system used by an international brokerage company. It is designed to receive CRM-exported CSV files, process them with Python, and generate insights and dashboards.

---

## 🎯 Goals

- Clean and structure raw lead data from CSV
- Calculate conversion-related KPIs
- Generate final datasets for BI tools
- Enable interactive visualizations (Power BI or Streamlit)

---

## 📁 Project Structure

```
Projeto_Dados_Corretora/
├── App/                  # Streamlit dashboard (in progress)
├── Data/
│   ├── RAW/             # Raw files (CSV exported from CRM)
│   ├── PROCESSED/       # Cleaned data
│   └── FINAL/           # Aggregated indicators
├── Notebook/
│   └── ETL_Leads.ipynb  # Main ETL notebook
├── notebooks_extras/    # Prototypes and experiments
├── Utils/
│   ├── io.py            # I/O utilities (save_csv)
│   └── paths.py         # Path management
├── docs/
│   └── estrutura.md     # Project structure overview
├── test_paths.py        # Path validation script
├── LICENSE              # MIT License
├── README.md            # (Portuguese version)
├── README_en.md         # (This file)
└── requirements.txt     # Python dependencies
```

---

## 📈 Main KPIs
- Lead conversion rate
- Average time to first trade
- Deposit amount per origin
- Conversion by country and lead profile

---

## 🔧 Stack
- Python (pandas, numpy, pathlib)
- Jupyter Notebooks
- Power BI / Streamlit
- CSV input (simulating CRM exports)

---

## 👨‍💼 Author
**Leonardo Barbosa**  
Data Scientist | BI Analyst  
CBF Academy MBA Instructor  
[LinkedIn](https://www.linkedin.com/in/leonardo-barbosa777)
