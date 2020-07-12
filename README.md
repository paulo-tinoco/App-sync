## Objetivo do projeto

Esse projeto tem o objetivo de consumir uma API a cada 30 minutos e sincronizar com os dados em um banco de dados.


## Instalação local

 1. Crie uma virtual virtual environment python
 
 `$ python -m venv venv`
 
 2. Ative a environment
 
 `$ source venv/bin/activate`
 
 3. Instale as dependências
 
 `(venv)$ pip install -r requirements.txt`

 4. Inicilize a aplicação:
 
 `python run.py`


## Rodando em docker através do Dockerfile

1. Faça o build baseado no Dockerfile
 
 `$ docker build -t appsync:latest .`

2. Inicialize o docker
 
 `$ docker run appsync:latest`

## Rodando em docker através do dockerhub

 1. Faça o pull da imagem no dockerhub
 
 `$ docker pull tinoco/appsync`
 
 2. Inicialize o docker
 
 `$ docker run tinoco/appsync:latest`