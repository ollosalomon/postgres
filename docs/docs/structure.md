# Structure du Projet

Voici une description de la structure des fichiers et dossiers principaux de ce projet.

```bash
csv_to_postgres_pipeline/
│
├── data/                         # Répertoire contenant les fichiers CSV
│   └── myfile.csv                # Exemple de fichier CSV
│
├── db/                           # Répertoire pour les données persistantes de PostgreSQL
│   └── ...                       # Fichiers générés par PostgreSQL
│
├── docs/                         # Documentation du projet (MkDocs)
│   ├── index.md                  # Page d'accueil de la documentation
│   ├── guide/                    # Sous-dossiers pour la documentation détaillée
│   └── ...                       # Autres fichiers de documentation
│
├── Dockerfile                    # Fichier Docker pour construire l'application
├── docker-compose.yml            # Configuration pour Docker Compose
├── requirements.txt              # Dépendances Python pour le projet
└── app.py                       # Script principal pour l'importation CSV vers PostgreSQL
```