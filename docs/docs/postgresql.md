# Service PostgreSQL

Ce service utilise l'image officielle PostgreSQL version 13. PostgreSQL est un système de gestion de bases de données relationnelles qui stocke les données importées à partir du fichier CSV.

## Configuration du service :

- **Image** : `postgres:13`
- **Nom du conteneur** : `postgres_db`
- **Volumes** : Le dossier local `./db` est monté sur le conteneur à `/var/lib/postgresql/data`. Cela permet de stocker les données de manière persistante.
- **Ports** : Le service expose le port PostgreSQL par défaut (5432) et le rend accessible localement via le port 5482.

## Fichier `.env` :

Le fichier `.env` contient les variables d'environnement pour PostgreSQL comme le nom d'utilisateur, le mot de passe, et le nom de la base de données.

Exemple :
```
POSTGRES_USER=myuser POSTGRES_PASSWORD=mypassword POSTGRES_DB=mydatabase
```

## Accès :

Vous pouvez interagir avec la base de données en utilisant des outils comme `psql` ou via l'interface pgAdmin (voir la section pgAdmin).
