import json
import requests

'''
Teste do consumo da API
Todos os endpoints retornam o status code 200
Abaixo estão alguns testes para verificar se o consumo da API está funcionando

'''

def cadastro_usuario(login, senha):
    url = 'http://localhost:5000/cadastro'
    headers = {'Content-Type': 'application/json'}
    payload = {'login': login, 'senha': senha}
    response = requests.post(
        url, 
        data=json.dumps(payload), 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# cadastro_usuario('teste', 'teste')

def login(usuario, senha):
    url = 'http://localhost:5000/login'
    headers = {'Content-Type': 'application/json'}
    payload = {'login': usuario, 'senha': senha}
    response = requests.post(
        url, 
        data=json.dumps(payload), 
        headers=headers
        )
    response_data = json.loads(response.content)
    access_token = response_data['access_token']
    # print(access_token)
    return access_token
# login('vmeazevedo','123456')

def get_clientes():
    url = 'http://localhost:5000/clientes'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url, 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# get_clientes()

def get_clientes_id(id):
    url = 'http://localhost:5000/clientes/' + str(id)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url, 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# get_clientes_id(1)

def post_clientes_id(id, nome, email, telefone, plano, access_token):
    url = 'http://localhost:5000/clientes/' + str(id)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    payload = {'nome': nome, 'email': email, 'telefone': telefone, 'plano': plano}
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# post_clientes_id('4', 'Vinicius','teste@gmail.com','123456789','básico', access_token=login('vmeazevedo','123456'))

def put_clientes_id(id, nome, email, telefone, plano, access_token):
    url = 'http://localhost:5000/clientes/' + str(id)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    payload = {'nome': nome, 'email': email, 'telefone': telefone, 'plano': plano}
    response = requests.put(
        url,
        data=json.dumps(payload),
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# put_clientes_id('4', 'Vinicius Azevedo','teste@gmail.com','123456789','básico', access_token=login('vmeazevedo','123456'))

def delete_clientes_id(id, access_token):
    url = 'http://localhost:5000/clientes/' + str(id)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    response = requests.delete(
        url,
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# delete_clientes_id('4', access_token=login('vmeazevedo','123456'))

def get_user_id(id):
    url = 'http://localhost:5000/usuarios/' + str(id)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url, 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# get_user_id(2)

def delete_user_id(id, access_token):
    url = 'http://localhost:5000/usuarios/' + str(id)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    response = requests.delete(
        url, 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# delete_user_id('2', access_token=login('vmeazevedo','123456'))

def logout(access_token):
    url = 'http://localhost:5000/logout'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    response = requests.post(
        url, 
        headers=headers
        )
    response_data = json.loads(response.content)
    print(response_data)
# logout(login('vmeazevedo','123456'))