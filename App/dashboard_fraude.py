import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(layout='wide', page_title='Análise de Risco - Corretora Internacional')

st.title("🚨 Painel de Detecção de Fraudes - Leads Convertidos")

# Carregar dados
data_path = Path(__file__).resolve().parent.parent / "Data" / "FINAL" / "suspeitos_leads.csv"
df = pd.read_csv(data_path)

st.markdown("Este painel apresenta os *leads convertidos* com padrão suspeito, como depósitos baixos e atividade imediata.")

# Filtros
col1, col2 = st.columns(2)
with col1:
    origem = st.multiselect("Filtrar por Origem", df['origem'].unique(), default=list(df['origem'].unique()))
with col2:
    pais = st.multiselect("Filtrar por País", df['pais'].unique(), default=list(df['pais'].unique()))

df_filtro = df[df['origem'].isin(origem) & df['pais'].isin(pais)]

st.dataframe(df_filtro.sort_values("valor_deposito").reset_index(drop=True))

st.metric("Total de Leads Suspeitos", len(df_filtro))
