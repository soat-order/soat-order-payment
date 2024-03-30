```
https://znasibov.info/posts/2022/09/18/hexarch_di_python_part_2.html
```

**Start Aplicacao(server)**
```
$ uvicorn src.main:app
```

**Start aplicacao(server) faz o restart(--reload) automaticamente**
```
$ uvicorn src.main:app --reload
```

**Start Aplicacao(server) faz o restart automaticamente**
$python3 src/app/main.py

**DOCKER**
```
# start mongodb
docker-compose -f docker-compose-mongodb.yml up -d

# start mongodb e deploy da aplicacao
docker-compose up -d
#
```
**swagger**
```
http://localhost:8000/docs
http://localhost:8000/redoc
```

**Caso porta estiver in use 8000**
```
$lsof -i :8000
$ kill -9 PID
```

**
```
@dataclass
class Customer():
    # _id: uuid.UUID = field(default_factory=uuid.uuid4)
    # id: str = field(init=False,default_factory=uuid.uuid4)
    id: str = field(init=False)
    name: str
    documentNumber: str
    email: str
    phoneNumber: str
```

**Criando Ambiente Virtual**
```
$python3 -m venv .env
$python3 -m venv .venv
```

**Ativando Ambiente Virtual**
```
$source .venv/bin/activate
export PYTHONPATH=$PWD/app

# deprecated
$. .env/bin/activate
```

**Desativando Ambiente Virtual**
```
$deactivate
```

***RUN SOAT-ORDER-PAYMENT***
```
.venv/bin/python app/main.py 
```

**TESTS**
```
# padrao relatorio tela coverage
pytest --cov=app/src/core/usecase/ app/tests/

# gera relatorio
pytest --junitxml=tests/test-results.xml --cov=./app/src/core/usecase/ --cov-report=xml --cov-report=html

pytest --junitxml=tests/report/test-results.xml --cov=./app/src/core/usecase/ --cov-report=xml 

# simples
pytest -cov=codigo app/tests/
```

**AWS SQS**
```
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name sqs-payment-order --region sa-east-1
aws --endpoint-url http://localhost:4566 sqs create-queue --queue-name sqs-payment-order --profile soat-order
aws --endpoint-url http://localhost:4566 sqs list-queues --profile soat-order

aws --endpoint-url http://localhost:4566 sqs send-message --queue-url http://localhost:4566/000000000000/sqs-payment-error --message-body '{"orderId": "dd997384-20f4-4967-bc2c-dbc8a015b742", "amountPaid": 17.0, "dateTimePaid": "2024-03-29T15:10:30.996891", "status": "CANCELED"}'

```


**Dependencias Instalando**
- **fastapi** lib de framework REST
- **gunvicorn e uvicorn** lib de webservers 
- **sql** lib de mapeamento de dominio
- **sqlalchemy** lib ORM para mapeamento e filtro SQL
- **mysql-connector-python** lib de conexão para MySQL
- **asyncmy** lib ORM para conexao async para MySQL
- **greenlet** lib dependencia do asyncmy para MySQL

```
$pip install fastapi gunicorn uvicorn
$pip install sql
$pip install sqlalchemy
#$pip install mysql-connector-python
$pip install asyncmy
pip install jwt
$pip freeze > requirements.txt
$pip install -r requirements.txt
```

**comandos**
- **remover __pycache__**: find . -type d -name __pycache__ -exec rm -r {} \+
- **desabilitar __pycache__**: export PYTHONDONTWRITEBYTECODE=1
- **desinstalar todas libs**: pip freeze | xargs pip uninstall -y
