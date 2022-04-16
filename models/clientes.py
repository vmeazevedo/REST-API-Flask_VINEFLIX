from sql_alchemy import banco

class ClienteModel(banco.Model):
    __tablename__ = 'clientes'

    # Criar as colunas da tabela
    cliente_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(50))
    email = banco.Column(banco.String(50))
    telefone = banco.Column(banco.String(20))
    plano = banco.Column(banco.String(11))


    # Cria o construtor
    def __init__(self,cliente_id, nome, email, telefone, plano):
        self.cliente_id = cliente_id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.plano = plano
    
    # Função de retorno json da requisição
    def json(self):
        return {
            'cliente_id': self.cliente_id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'plano': self.plano
        }

    @classmethod
    def find_by_id(cls, cliente_id):
        cliente = cls.query.filter_by(cliente_id=cliente_id).first()
        if cliente:
            return cliente
        return None

    def save_to_db(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_from_db(self):
        banco.session.delete(self)
        banco.session.commit()
    
    def update_dados(self, nome, email, telefone, plano):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.plano = plano
    



    