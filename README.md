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

