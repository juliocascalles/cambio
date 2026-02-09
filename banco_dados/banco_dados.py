class BancoDados:
    def __init__(self, conexao):
        self.conexao = conexao

    def cria_tabela(self):
        self.conexao.execute("CREATE TABLE ...")
    
    def insere_registro(self, **dados):
        self.conexao.execute('INSERT INTO ...')

    def consulta(self, filtro=None):
        cursor = self.conexao.execute('SELECT * FROM ...')
        return cursor.fetchall()
