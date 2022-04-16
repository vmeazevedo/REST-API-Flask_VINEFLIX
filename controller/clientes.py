from flask_restful import Resource, reqparse
from models.clientes import ClienteModel
from flask_jwt_extended import jwt_required

class Clientes(Resource):
    # Metodo get
    def get(self):
        return {'clientes': [clientes.json() for clientes in ClienteModel.query.all()]}

class Cliente(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help='Nome do cliente é obrigatório')
    argumentos.add_argument('email', type=str, required=True, help='Email do cliente é obrigatório')
    argumentos.add_argument('telefone', type=str, required=True, help='Telefone do cliente é obrigatório')
    argumentos.add_argument('plano', type=str, required=True, help='Plano do cliente é obrigatório')
    

    # Metodo get by id
    def get(self, cliente_id):
        # Se meu id existir no banco, retorna o cliente
        cliente = ClienteModel.find_by_id(cliente_id)
        if cliente:
            return cliente.json(), 200
        return {'message': 'Cliente não encontrado'}, 404
    
    # Metodo post
    @jwt_required()
    def post(self, cliente_id):
        # Se meu id existir no banco, retorna msg de erro
        if ClienteModel.find_by_id(cliente_id):
            return {"message": "Cliente já cadastrado!"}, 400

        # Se não, cria um novo cliente validando se o plano está correto
        lista_planos = ['básico', 'intermediário', 'avançado']
        dados = Cliente.argumentos.parse_args()
        cliente = ClienteModel(cliente_id, **dados)
        if cliente and dados['plano'] in lista_planos:
            try:
                cliente.save_to_db()
            except:
                return {'message': 'Erro ao inserir o cliente'}, 500
            return cliente.json(), 201
        else:
            return {'message': 'Plano inválido'}, 404

    # Metodo put
    @jwt_required()
    def put(self, cliente_id):
        # Se meu id existir e o plano estiver correto, atualiza o cliente
        lista_planos = ['básico', 'intermediário', 'avançado']
        dados = Cliente.argumentos.parse_args()
        cliente_encontrado = ClienteModel.find_by_id(cliente_id)
        if cliente_encontrado and dados['plano'] in lista_planos:
            cliente_encontrado.update_dados(**dados)
            try:
                cliente_encontrado.save_to_db()
            except:
                return {'message': 'Erro ao atualizar o cliente'}, 500
            return cliente_encontrado.json(), 200
            
        # Se não, cria um novo cliente validando se o plano está correto
        cliente = ClienteModel(cliente_id, **dados)
        if cliente and dados['plano'] in lista_planos:
            try:
                cliente.save_to_db()
            except:
                return {'message': 'Erro ao inserir o cliente'}, 500
            return cliente.json(), 201
        
        else:
            return {'message': 'Plano inválido'}, 404

    # Metodo delete
    @jwt_required()
    def delete(self, cliente_id):
        cliente = ClienteModel.find_by_id(cliente_id)
        if cliente:
            try:
                cliente.delete_from_db()
            except:
                return {'message': 'Erro ao deletar o cliente'}, 500
            return {'message': 'Cliente deletado'}, 200
        return {'message': 'Cliente não encontrado'}, 404
      
