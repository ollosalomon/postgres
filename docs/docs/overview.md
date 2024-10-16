# Aperçu du projet

Ce projet est conçu pour automatiser l'importation de données à partir d'un fichier CSV dans une base de données PostgreSQL. Il utilise plusieurs services Docker pour gérer la base de données, une interface d'administration PostgreSQL (pgAdmin), et la documentation avec MkDocs.

## Objectifs principaux :

- Importer des fichiers CSV dans PostgreSQL.
- Gérer et visualiser la base de données via pgAdmin.
- Documenter le projet à l'aide de MkDocs.
- Conteneuriser et automatiser l'exécution des services avec Docker Compose.

## Structure du projet :

- `app/` : Contient l'application Python qui effectue l'importation de données.
- `db/` : Dossier monté pour stocker les données PostgreSQL localement.
- `docs/` : Dossier contenant les fichiers de documentation MkDocs.
- `Dockerfile` : Définit l'image Docker personnalisée pour l'application.
- `docker-compose.yml` : Orchestre les services Docker pour l'application, PostgreSQL, pgAdmin, et la documentation.
