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
# CONTRATO DA API

## Endpoints Disponíveis

### Autenticação
- `POST /api/token/`: Obter um token de acesso (JWT).
- `POST /api/token/refresh/`: Atualizar o token de acesso.
- `GET /api/user-info/`: Obter informações do usuário autenticado.

### Cartões
- `GET /api/cartoes/`: Listar todos os cartões disponíveis.
- `POST /api/cartoes/`: Criar um novo cartão.
- `GET /api/cartoes/{id}/`: Detalhar um cartão específico.
- `PUT /api/cartoes/{id}/`: Atualizar um cartão existente.
- `DELETE /api/cartoes/{id}/`: Excluir um cartão existente.

### Operações Específicas
- `POST /api/cartoes/file/`: Realizar operações de upload de arquivo relacionadas aos cartões.
- `GET /api/cartoes/consulta_numero/`: Realizar consulta com base no número do cartão.

## Parâmetros

- `POST /api/cartoes/` (criar um novo cartão):
  - Corpo da requisição deve conter os dados necessários para criar um cartão (ex: número do cartão, nome do titular, data de validade, etc).

- `PUT /api/cartoes/{id}/` (atualizar um cartão existente):
  - Corpo da requisição deve conter os dados a serem atualizados do cartão (ex: número do cartão, nome do titular, data de validade, etc).

## Autenticação

- Para acessar endpoints que requerem autenticação (exceto `/api/token/`), é necessário incluir o token JWT no cabeçalho `Authorization`.

## Observações

- Certifique-se de estar autenticado para acessar endpoints que exigem autenticação.
- Para operações específicas como upload de arquivo ou consulta por número de cartão, utilize os endpoints correspondentes com os métodos HTTP corretos (POST e GET, respectivamente).

Este arquivo README fornece informações sobre os requisitos, instalação e desenvolvimento do projeto, além de detalhar o contrato da API de Cartões. Utilize as instruções para configurar o ambiente, desenvolver e interagir com a API de acordo com as especificações fornecidas.
