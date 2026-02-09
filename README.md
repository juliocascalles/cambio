# Cambio

Projeto de estudo para
* baixar cotações de moedas
* gravar no banco de dados
* emitir relatórios

Classes:
* BancoDados
    * método cria_tabela -  faz o `CREATE TABLE...`
    * método insere_registro - faz o `INSERT INTO ...`
    * método consulta - faz `SELECT * FROM ...`
* Moeda
    * atributo de classe `URL_API` contém o endereço da API
    * método baixar_info faz um **request.get** na API
    * gravar: envia os dados para um objeto do tipo _BancoDados_
* Relatorio
    * método processar_dados faz consulta em um _BancoDados_
    * método exibe_informacoes mostra as informações na tela

