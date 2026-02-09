from relatorios.relatorio import Relatorio
from banco_dados.banco_dados import BancoDados


class SugestaoInvestimentos(Relatorio):
    def processar_dados(self, banco_dados: BancoDados):
        for cotacao in banco_dados.consulta():
            ...

    def exibe_informacoes(self):
        ...
