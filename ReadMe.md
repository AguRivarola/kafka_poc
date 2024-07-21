# POC kafka con python y docker
El objetivo de este POC es generar la infraestructura para levantar una API que genere un mensaje, lo transmita a travez de un topico de Kafka y sea consumido por otra API python que escuche ese topico.

# Dependencias
- Python 3.12.4
    - pip
        - quixstreams (all)
        - request (producer)
        - pygsheets (sheets)

- Docker

# Crear python env

```bash
python -m venv env
source env/bin/activate #Linux
source env/Scripts/activate #Windows
```

# Instalar dependencias segun corresponda

```bash
pip install quixtreams 
pip install request 
pip install pygsheets
```

# Generar `requirements.txt`

```bash
python -m pip freeze > requirements.txt
```
# Sheets integration
Para poder usar la integracion de sheets, deberiamos dirigirnos a
[google sheets integration with python](https://developers.google.com/sheets/api/quickstart/python?hl=es-419)
Una ves realizado los pasos y garantizados los permisos para lectura y escritura de Drive y Sheets, vamos a descargar el json con los secrets y copiarlo con el nombre de `client_secret.json` a la misma altura que los main y los dockerfiles.

Antes de armar el docker de sheets, debemos generar el token de la app. 

``` bash
python -c 'from main_sheets import authorize_sheets; authorize_sheets()'
```
Seguir pasos para authorizar la app y luego podremos generar el docker con nuestros accesos personales.

Crear un nuevo sheet con el nombre `Weather Sheet` en la raiz de google y ya podremos correr la app.

# Probar el proyecto

```bash
- docker build -t base_kfk -f DockerfileBaseImg . 
- docker build -t producer -f Dockerfile_producer .
- docker build -t consumer -f Dockerfile_consumer .
- docker build -t processor -f Dockerfile_processor .
- docker build -t sheets -f Dockerfile_sheets .
- docker-compose up -d
```

