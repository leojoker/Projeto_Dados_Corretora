from pathlib import Path

def get_project_root() -> Path:
    """Retorna o diretório raiz do projeto, baseado na estrutura de pastas."""
    return Path.cwd().parent

def get_data_dir(subfolder: str) -> Path:
    """Retorna o caminho completo para uma subpasta dentro de /Data."""
    return get_project_root() / "Data" / subfolder.upper()

def get_notebook_dir() -> Path:
    """Retorna o caminho da pasta onde estão os notebooks (opcional)."""
    return get_project_root() / "Notebook"
