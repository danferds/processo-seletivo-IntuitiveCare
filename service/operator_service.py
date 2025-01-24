from repository.operator_repository import OperadoraRepository
import pandas as pd

class OperadoraService:
    def __init__(self):
        repository = OperadoraRepository()
        self.base_de_dados = repository.carregar_dados()

    def listar_todas_operadoras(self):
        """
        Retorna todas as operadoras como uma lista de dicionários.
        """
        return self.base_de_dados.to_dict(orient='records')

    def buscar_operadora_por_cnpj(self, cnpj):
        """
        Encontra uma operadora pelo CNPJ.
        :param cnpj: O CNPJ da operadora a ser buscada.
        :return: Dicionário representando a operadora encontrada ou None se não encontrada.
        """

        cnpj = str(cnpj)
        self.base_de_dados['CNPJ'] = self.base_de_dados['CNPJ'].astype(str)
        operadora = self.base_de_dados[self.base_de_dados['CNPJ'] == cnpj]
        
        if not operadora.empty:
            return operadora.to_dict(orient='records')[0]
        return None
