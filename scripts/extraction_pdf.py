from tabula import read_pdf
import pandas as pd

def extrair_tabelas_pdf(caminho_pdf):
    """
    Extrai tabelas de um arquivo PDF.
    :param caminho_pdf: Caminho para o arquivo PDF.
    :return: Lista de DataFrames extraídos.
    """

    tabelas_extraidas = read_pdf(caminho_pdf, pages="all", multiple_tables=True, pandas_options={'header': None})
    return tabelas_extraidas

def concatenar_tabelas(data_frames):
    """
    Concatena uma lista de DataFrames em um único DataFrame.
    :param data_frames: Lista de DataFrames.
    :return: DataFrame concatenado.
    """

    tabelas_concatenadas = pd.concat(data_frames, ignore_index=True)
    return tabelas_concatenadas