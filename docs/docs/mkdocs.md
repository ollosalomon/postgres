# Service MkDocs

Ce service utilise MkDocs pour générer et servir la documentation du projet. MkDocs est un générateur de documentation statique très simple à configurer.

## Configuration du service :

- **Image** : `squidfunk/mkdocs-material`
- **Nom du conteneur** : `mkdocs`
- **Ports** : Le service expose le port 8000, accessible localement via le port 9026.
- **Command** : La commande `mkdocs serve --dev-addr=0.0.0.0:8000` démarre MkDocs en mode développement et sert la documentation en direct.

## Création de la documentation :

Les fichiers Markdown de documentation sont placés dans le répertoire `docs/`. Chaque fichier représente une section de la documentation du projet.

Pour modifier ou ajouter de la documentation, il suffit de créer un fichier Markdown (.md) dans ce répertoire et de le lier dans le fichier `mkdocs.yml`.
