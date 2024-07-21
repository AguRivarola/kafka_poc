# POC kafka con python y docker
El objetivo de este POC es generar la infraestructura para levantar una API que genere un mensaje, lo transmita a travez de un topico de Kafka y sea consumido por otra API python que escuche ese topico.

# Dependencias
- Python 3.12.4
    - pip
        - quixstreams
        - request

- Docker

# Crear python env

```bash
python -m venv env
source env/bin/activate #Linux
source env/Scripts/activate #Windows
```

# Instalar dependencias

```bash
pip install quixtreams request
```

# Generar `requirements.txt`

```bash
python -m pip freeze > requirements.txt
```

# Probar el proyecto

```bash
- docker build -t base_kfk -f DockerfileBaseImg . 
- docker build -t producer -f Dockerfile_producer .
- docker build -t consumer -f Dockerfile_consumer .
- docker build -t processor -f Dockerfile_processor .
- docker-compose up -d
```