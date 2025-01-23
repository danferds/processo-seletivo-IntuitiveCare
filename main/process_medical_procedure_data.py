from scripts.extraction_pdf import extrair_tabelas_pdf, concatenar_tabelas
from scripts.dataset_column_utils import renomear_colunas
import pandas as pd
CAMINHO_PDF = r"docs/anexos/Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.pdf"
CAMINHO_DF = r"datasets/rol_de_procedimentos_e_eventos_em_saude/rol_de_procedimentos_e_eventos_em_saude.csv"
MAPEAMENTO_COLUNAS = {
    "OD": "odontologica",
    "AMB": "ambulatorial",
    "HCO": "hospitalar_com_obstetricia",
    "HSO": "hospitalar_sem_obstetricia",
    "REF": "plano_referencia",
    "PAC": "procedimento_de_alta_complexidade",
    "DUT": "diretriz_de_utilizacao",
    "PROCEDIMENTO": "procedimento",
    "RN\r(alteração)": "rn\(alteracao)",
    "VIGÊNCIA": "vigencia",
    "SUBGRUPO": "subgrupo",
    "GRUPO": "grupo",
    "CAPÍTULO": "capitulo"
}

tabelas_extraidas = extrair_tabelas_pdf(CAMINHO_PDF)
tabelas_concatenadas = concatenar_tabelas(tabelas_extraidas)
nome_arquivo = "rol_de_procedimentos_e_eventos_em_saude.csv"
tabelas_concatenadas.to_csv(nome_arquivo, index=False, header=False)


df = pd.read_csv(CAMINHO_DF)
df_com_colunas_renomeadas = renomear_colunas(df, MAPEAMENTO_COLUNAS)
nome_arquivo = "rol_de_procedimentos_e_eventos_em_saude_com_colunas_renomeadas.csv"
df_com_colunas_renomeadas.to_csv(nome_arquivo, index=False, header=True)