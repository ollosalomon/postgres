
### Interface pgAdmin


# Service pgAdmin

pgAdmin est un outil d'administration web pour PostgreSQL. Ce service permet de gérer visuellement la base de données, de créer des requêtes, et d'explorer les schémas.

## Configuration du service :

- **Image** : `dpage/pgadmin4`
- **Nom du conteneur** : `csv_to_postgres_pipeline`
- **Ports** : Le service expose le port 80 (port par défaut de pgAdmin) et est accessible localement via le port 5557.
- **Variables d'environnement** : Vous pouvez vous connecter à l'interface pgAdmin avec l'email et mot de passe suivants :
  - Email : `debug@debug.com`
  - Mot de passe : `debug`

## Accès :

Une fois le service en marche, vous pouvez accéder à l'interface via [http://localhost:5557](http://localhost:5557).
