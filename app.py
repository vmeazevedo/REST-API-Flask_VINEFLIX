from flask import Flask, jsonify
from flask_restful import Api
from controller.clientes import Clientes, Cliente
from controller.usuario import User, UserConfirm, UserRegister, UserLogin, UserLogout, UserConfirm
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'segredo'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

# Criar o banco primeiro
@app.before_first_request
def criar_banco():
    banco.create_all()


@jwt.token_in_blocklist_loader
def verifica_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'resultado': 'Token de acesso inválido!'}), 401


# Criação das rotas
api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<string:cliente_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserConfirm, '/confirmacao/<int:user_id>')



if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)