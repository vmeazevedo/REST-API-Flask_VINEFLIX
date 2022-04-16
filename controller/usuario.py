from models.usuario import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help='Login é obrigatório')
atributos.add_argument('senha', type=str, required=True, help='Senha é obrigatório')

class User(Resource):
    def get(self, user_id):
        user = UserModel.find_by_user_id(user_id)
        if user:
            return user.json(), 200
        return {'message': 'Usuário não encontrado'}, 404

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_by_user_id(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'Erro ao deletar usuário'}, 500
            return {'message': 'Usuário deletado'}, 200 
        return {'message': 'Usuário não encontrado'}, 404
    
class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()
        
        if UserModel.find_by_login(dados['login']):
            return {'message': 'Usuário já existe'}, 400
        
        user = UserModel(**dados)
        try:
            user.save_user()
        except:
            return {'message': 'Erro ao criar usuário'}, 500
        return {'message': 'Usuário criado com sucesso'}, 201

class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'Usuário ou senha inválidos'}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            BLACKLIST.add(jti)
        except:
            return {'message': 'Erro ao deslogar'}, 500
        return {'message': 'Usuário deslogado'}, 200