# Application Python

Ce service est l'application Python responsable de l'importation des données CSV dans la base de données PostgreSQL.

## Dockerfile

Le fichier `Dockerfile` définit l'image Docker personnalisée pour ce service. Il installe les dépendances requises et exécute le script principal de l'application.

Extrait du `Dockerfile` :

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```