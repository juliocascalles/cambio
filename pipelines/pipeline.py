from dataclasses import dataclass
from banco_dados.banco_dados import BancoDados
from moedas.moeda import Moeda
from relatorios.relatorio import Relatorio


@dataclass
class Pipeline:
    moedas: list[Moeda]
    bancos_dados: list[BancoDados]
    relatorios: list[Relatorio]

    def carrega_dados(self):
        moeda: Moeda
        banco_dados: BancoDados
        for moeda in self.moedas:
            moeda.baixar_info()
            for banco_dados in self.bancos_dados:
                moeda.gravar(banco_dados)

    def emite_relatorios(self):
        relatorio: Relatorio
        banco_dados: BancoDados
        for relatorio in self.relatorios:
            for banco_dados in self.bancos_dados:
                relatorio.processar_dados(banco_dados)
            relatorio.exibe_informacoes()

    def executa(self):
        self.carrega_dados()
        self.emite_relatorios()