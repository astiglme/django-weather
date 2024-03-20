# Django Weather App

## Application

### Prerequisites

```shell
pipenv install django
pipenv install djangorestframework
pipenv install openmeteo-requests
pipenv install requests-cache retry-requests numpy pandas
pipenv install psycopg2
```

### Usage

```shell
python manage.py migrate
python manage.py runserver
```

### Query

get meteo data
```shell
curl -X GET http://127.0.0.1:8000/api/meteo/get/
```

get data
```shell
curl -X GET http://127.0.0.1:8000/api/daytemp/read/1104

curl -X GET http://127.0.0.1:8000/api/daytemp/list/
```

create data
```shell
curl -X POST http://127.0.0.1:8000/api/daytemp/create/ -d '{"date": "1971-01-01", "temp": 1.23}' -H "Content-Type: application/json"

curl -X POST http://127.0.0.1:8000/api/daytemp/create/ -d '[{"date": "1971-01-01", "temp": 1.23}]' -H "Content-Type: application/json"
```

update data
```shell
curl -X PUT http://127.0.0.1:8000/api/daytemp/update/123 -d '{"date": "1971-01-01", "temp": 1.23}' -H "Content-Type: application/json"
```

delete data
```shell
curl -X DELETE http://127.0.0.1:8000/api/daytemp/delete/123
```

delete all
```shell
curl -X DELETE http://127.0.0.1:8000/api/daytemp/delete/0
```

### Build Docker

in weather app directory:
```shell
pip freeze -l > requirements.txt
docker build -t stigito/django-weather:1.0 .

```

## Ansible

```shell
ansible-playbook -i inventories/local setup.yml --diff --check
ansible-playbook -i inventories/local start.yml --diff --check
ansible-playbook -i inventories/local stop.yml --diff --check
```