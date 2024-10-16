
### Fichier `docker-compose.yml`

# Docker Compose - Explication

Le fichier `docker-compose.yml` orchestre plusieurs services Docker pour automatiser l'exécution du projet. Il permet de démarrer tous les services (base de données, application, pgAdmin, documentation) en une seule commande.

## Services :

1. **db** : Service PostgreSQL pour stocker les données.
2. **app** : Application Python qui importe les données CSV dans PostgreSQL.
3. **pgadmin** : Interface web pour administrer la base de données PostgreSQL.
4. **docs** : Génère et sert la documentation via MkDocs.

## Exemple complet du fichier :

```yaml
services:
  db:
    image: postgres:13
    container_name: postgres_db
    env_file:
      - .env
    volumes:
      - ./db:/var/lib/postgresql/data
    ports:
      - "5482:5432"
  
  app:
    build: .
    depends_on:
      - db
    volumes:
      - ./data:/data
    environment:
      DATABASE_URL: postgresql://myuser:mypassword@db:5432/mydatabase

  pgadmin:
    container_name: csv_to_postgres_pipeline
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: debug@debug.com
      PGADMIN_DEFAULT_PASSWORD: debug
    ports:
      - "5557:80"
    restart: always

  docs:
    image: minidocks/mkdocs:latest
    container_name: mkdocs
    volumes:
      - ./docs/:/docs 
    restart: always
    ports:
      - "9026:9000"
    stdin_open: true
    tty: true
    command: mkdocs serve --config-file /docs/mkdocs.yml --dev-addr 0.0.0.0:9000

```