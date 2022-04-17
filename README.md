![VINEFLIX-removebg-preview (1)](https://user-images.githubusercontent.com/40063504/163687066-2d473abd-eda6-499a-bca9-840b15d9aa1b.png)


# REST-API-Flask_VINEFLIX
Aplicação REST API de gerenciamento de informações cadastrais em Python utilizando Framework Flask e padrão MVC com controle de cadastro de usuário, login e logout.

![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0) [![Twitter Follow](https://img.shields.io/twitter/follow/vmeazevedo.svg?style=social)](https://twitter.com/vmeazevedo) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Vinícius_Azevedo%20-blue)](https://www.linkedin.com/in/vin%C3%ADcius-azevedo-45180ab2/)

![Star](https://img.shields.io/github/stars/vmeazevedo/REST-API-Flask_VINEFLIX?style=social)
![Fork](https://img.shields.io/github/forks/vmeazevedo/REST-API-Flask_VINEFLIX?label=Fork&style=social)

## Requirements

```sh
pip install -r requirements.txt
```

## Utilização
1. Clone o repositório para sua máquina

   ``
   git clone https://github.com/vmeazevedo/REST-API-Flask_VINEFLIX
   ``
2. Execute o arquivo python ``app.py``.
3. Abra o POSTMAN e importe a collection ``REST_API - VineFlix.postman_collection.json``, localizada na pasta ``collection``.
4. Via ``POSTMAN`` execute a request de ``Cadastro`` para criar um novo ``user_id``, ele será necessário para criação do token.
5. Execute a request de ``Confirmação`` para validar o seu novo cadastro.
6. Execute a request de ``Login`` para que o token seja gerado validando assim suas demais requests.
7. O arquivo ``swagger.json`` contém toda a documentação da API e pode ser encontra na pasta ``swagger``. Use o site (``https://editor.swagger.io/``) para importar o arquivo e ver a documentação online.
8. Em caso de dúvida sobre o consumo da API, a documentação dos testes se encontra na pasta ``teste``.
9. Após a utilização execute a Request de ``Logout`` para invalidar seu token de sessão.

## Ex
<font color=\"green\">GET</font>/clientes
