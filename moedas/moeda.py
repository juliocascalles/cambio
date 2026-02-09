import requests
from banco_dados.banco_dados import BancoDados


class Moeda:
    URL_API = ''

    def baixar_info(self):
        requests.get(self.URL_API, ...)
    
    def gravar(self, banco_dados: BancoDados):
        banco_dados.insere_registro( ... )
