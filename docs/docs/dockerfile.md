# Dockerfile - Explication détaillée

Le fichier `Dockerfile` configure l'image Docker pour l'application Python, incluant toutes les dépendances et les fichiers nécessaires pour l'importation des données CSV.

## Étapes principales :

1. **Image de base** : Utilisation de l'image légère `python:3.9-slim` pour réduire la taille de l'image.
2. **Définition du répertoire de travail** : Le répertoire de travail est défini à `/app`, ce qui centralise tous les fichiers dans ce dossier.
3. **Installation des dépendances** : Les dépendances Python listées dans le fichier `requirements.txt` sont installées via `pip`.
4. **Copie des fichiers du projet** : Le reste du code est copié dans le conteneur.
5. **Exécution de l'application** : Le script `main.py` est exécuté pour démarrer l'importation des données.

## Exemple complet du Dockerfile :

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

