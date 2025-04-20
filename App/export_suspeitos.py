from pathlib import Path
import pandas as pd

# Caminho para dados
df_path = Path.cwd().parent / "Data" / "PROCESSED" / "leads_processados_para_pbi.csv"
df = pd.read_csv(df_path, parse_dates=["data_cadastro"])

# Filtrar leads convertidos e aplicar lógica de suspeição
df['dias_ate_1o_trade'] = df['dias_ate_1o_trade'].fillna(0)
df['valor_deposito'] = df['valor_deposito'].fillna(0)

df_convertidos = df[df['status_conversao'] == 'Convertido'].copy()
suspeitos = df_convertidos[(df_convertidos['valor_deposito'] < 300) & (df_convertidos['dias_ate_1o_trade'] < 1)]

# Exportar CSV
export_path = Path.cwd().parent / "Data" / "FINAL" / "suspeitos_leads.csv"
suspeitos.to_csv(export_path, index=False)
print(f"Arquivo exportado: {export_path}")
