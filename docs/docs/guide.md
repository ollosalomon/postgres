# Guide d'installation et d'exécution

Ce guide couvre les étapes nécessaires pour configurer et exécuter le pipeline de copie de données CSV vers une base de données PostgreSQL.

## Prérequis
- Docker et Docker Compose installés.
- Un fichier CSV avec les données à insérer dans la base de données.

## Étapes :

### Clonage du dépôt
Clonez le dépôt du projet :
```bash
git clone https://github.com/ollosalomon/csv_to_postgres.git
cd data-copy-pipeline
```



### Comment exécuter le projet


# Comment exécuter le projet

## Étapes pour démarrer tous les services

1. **Configurer les variables d'environnement** : Créez un fichier `.env` à la racine du projet et ajoutez les détails suivants :
```
POSTGRES_USER=myuser 
POSTGRES_PASSWORD=mypassword 
POSTGRES_DB=mydatabase
```

2. **Exécuter Docker Compose** : Lancez la commande suivante pour démarrer tous les services :
```bash
docker-compose up
```