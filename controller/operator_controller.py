from flask import jsonify, request
from service.operator_service import OperadoraService


class OperadoraController:
    def __init__(self, app):
        self.service = OperadoraService()

        app.add_url_rule('/operadoras', view_func=self.get_operadoras, methods=['GET'])
        app.add_url_rule('/operadoras/<cnpj>', view_func=self.get_operadora_por_cnpj, methods=['GET'])

    def get_operadoras(self):
        """
        Retorna todas as operadoras como uma lista de dicionários.
        """
        operadoras = self.service.listar_todas_operadoras()
        return jsonify(operadoras)

    def get_operadora_por_cnpj(self, cnpj):
        """
        Encontra uma operadora pelo CNPJ.
        :param cnpj: O CNPJ da operadora a ser buscada.
        return: Dicionário representando a operadora encontrada ou "Operadora não encontrada".
        """
        operadora = self.service.buscar_operadora_por_cnpj(cnpj)
        if operadora:
            return jsonify(operadora)
        return jsonify({"error": "Operadora não encontrada"}), 404