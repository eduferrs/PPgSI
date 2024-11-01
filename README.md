## Sobre
Projeto em desenvolvimento para a disciplina de Engenharia de Sistemas de Informação. 
Consiste em uma aplicação web para criação e avaliação de relatórios do Programa de Pós Graduação em Sistemas de Informação.
As principais tecnologias utilizadas são os frameworks Django (5.1.2) e Bootstrap (5.3.3).

## Execução em Linux
- Faca download e extracao dos arquivos
- Acesse a pasta pelo terminal e execute os seguintes comandos:
     - python3 -m venv .venv
     - source .venv/bin/activate
     - pip install -r requirements.txt
     - python3 manage.py makemigrations
     - python3 manage.py migrate
     - python3 manage.py runserver
- No navegador, acesse o endereço http://127.0.0.1:8000/
- Execute deactivate no terminal quando terminar de utilizar.


## Execução em Windows
- Necessário ter o python instalado (https://www.python.org/downloads/windows/)
- Faca download e extração dos arquivos deste repositório
- Acesse a pasta pelo terminal e execute os seguintes comandos:
	- python -m venv venv
	- .\scripts\activate
	- pip install -r requeriments.txt
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py runserver
- No navegador, acesse o endereço http://127.0.0.1:8000/
- Execute deactivate no terminal quando terminar de utilizar.


