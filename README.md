# cartao-backend

Este projeto implementa o app de cartões

## Requisitos
- Python = 3.10.12
- PostgreSQL = 14.9

## Instalação
Crie um ambiente virtual e ative-o

```shell
python3 -m venv env && source env/bin/activate
```

Instale as dependências do sistema
```shell
pip install -r requirements.txt
```

Crie seu Superuser
```shell
python manage.py createsuperuser
```

## Desenvolvimento

Para criar alguma migração, utilize o comando abaixo
```shell
python manage.py makemigrations
```

Para aplicar as migrações, utilize o comando abaixo
```shell
python manage.py migrate
```

Para rodar o servidor de desenvolvimento você pode usar o seguinte comando
```shell
python manage.py runserver
```
## CONTRATO DA API
Endpoints Disponíveis:
Autenticação:

POST /api/token/: Endpoint para obter um token de acesso (JWT).
POST /api/token/refresh/: Endpoint para atualizar o token de acesso.
GET /api/user-info/: Endpoint para obter informações do usuário autenticado.
Cartões:

GET /api/cartoes/: Endpoint para listar todos os cartões disponíveis.
POST /api/cartoes/: Endpoint para criar um novo cartão.
GET /api/cartoes/{id}/: Endpoint para detalhar um cartão específico.
PUT /api/cartoes/{id}/: Endpoint para atualizar um cartão existente.
DELETE /api/cartoes/{id}/: Endpoint para excluir um cartão existente.
Operações Específicas:

POST /api/cartoes/file/: Endpoint para realizar operações de upload de arquivo relacionadas aos cartões.
GET /api/cartoes/consulta_numero/: Endpoint para realizar consulta com base no número do cartão.
Parâmetros:
POST /api/cartoes/ (criar um novo cartão):

Corpo da requisição deve conter os dados necessários para criar um cartão (ex: número do cartão, nome do titular, data de validade, etc).
PUT /api/cartoes/{id}/ (atualizar um cartão existente):

Corpo da requisição deve conter os dados a serem atualizados do cartão (ex: número do cartão, nome do titular, data de validade, etc).
Autenticação:
Para acessar endpoints que requerem autenticação (exceto /api/token/), é necessário incluir o token JWT no cabeçalho Authorization.
Observações:
Certifique-se de estar autenticado para acessar endpoints que exigem autenticação.
Para operações específicas como upload de arquivo ou consulta por número de cartão, utilize os endpoints correspondentes com os métodos HTTP corretos (POST e GET, respectivamente).
Este contrato da API detalha os endpoints disponíveis, os métodos HTTP permitidos, os parâmetros necessários e outras informações importantes para interagir com a API de Cartões. Certifique-se de seguir as convenções e padrões do Django REST Framework ao realizar solicitações para cada endpoint.
