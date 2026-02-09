from pipelines.pipeline import Pipeline
from moedas.dolar_americano import Dolar
from moedas.renminbi_chines import Renminbi
from relatorios.comparativo_evolucao import Comparativo
from relatorios.sugestao_investimentos import SugestaoInvestimentos
from banco_dados.ms_sql_server import MsSqlServer
from banco_dados.mongodb import MongoDB


pipeline = Pipeline(
    moedas=[Dolar, Renminbi], # --- Moedas dos EUA e China
    relatorios=[Comparativo, SugestaoInvestimentos],
    bancos_dados=[MsSqlServer, MongoDB]
)

pipeline.executa()