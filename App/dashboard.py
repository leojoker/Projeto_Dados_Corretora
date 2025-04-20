import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Dashboard de Leads', layout='wide')

# Carregar dados
DATA_PATH = Path(__file__).resolve().parent.parent / 'Data' / 'FINAL' / 'indicadores_por_canal.csv'
df = pd.read_csv(DATA_PATH)

st.title('📊 Dashboard de Indicadores - Leads da Corretora')
st.dataframe(df)
