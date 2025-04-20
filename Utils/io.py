
from pathlib import Path


def save_csv(df, folder: Path, filename: str):
    """
    Salva um DataFrame em formato CSV dentro da pasta especificada.
    Cria a pasta caso ela não exista.

    Parâmetros:
    - df: pandas DataFrame
    - folder: caminho Path para a pasta onde salvar
    - filename: nome do arquivo .csv
    """
    folder.mkdir(parents=True, exist_ok=True)
    output_path = folder / filename
    df.to_csv(output_path, index=False)
    print(f"✅ Arquivo salvo com sucesso: {output_path}")
