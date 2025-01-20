def renomear_colunas(df, mapeamento):
    """
    Renomeia as colunas de um DataFrame com base em um dicionário de mapeamento.
    :param df: DataFrame original.
    :param mapeamento: Dicionário de mapeamento {coluna_original: nova_coluna}.
    :return: DataFrame com colunas renomeadas.
    """

    df_renomeado = df.rename(columns=mapeamento)
    return df_renomeado