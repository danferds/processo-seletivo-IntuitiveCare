import pandas as pd

class OperadoraRepository:
    def __init__(self):
        self.caminho_do_arquivo = 'datasets/dados_cadastrais_das_operadoras_ativas_na_ans/Relatorio_cadop.csv'

    def carregar_dados(self):
        """
        Carrega os dados do arquivo CSV.
        """
        try:
            base_de_dados = pd.read_csv(self.caminho_do_arquivo, sep=';', quotechar='"', encoding='utf-8')
            return base_de_dados.fillna('')
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo {self.caminho_do_arquivo} não encontrado.")
        except pd.errors.ParserError:
            raise ValueError(f"O arquivo {self.caminho_do_arquivo} tem um formato inválido.")
