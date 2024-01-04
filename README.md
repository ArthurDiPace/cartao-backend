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

## Variáveis De Ambiente

Crie o arquivo .env com as variáveis a partir deste arquivo:
```shell
# DATABASE Configuration
DB_NAME=cartoes
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

ALLOWED_HOSTS='*'
SECRET_KEY="django-insecure-^ett4b85j7$h$d9nc9oy86_)c54&i&wi@(_o%fnuu_$#_d!6q2"
DEBUG=True
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

