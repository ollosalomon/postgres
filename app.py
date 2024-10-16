import os
import pandas as pd
from sqlalchemy import create_engine

# Lire les variables d'environnement
db_url = os.getenv('DATABASE_URL')

csv_file_path = '/data/example_data.csv'

def copy_data(csv_file_path):
    try:
        data = pd.read_csv(csv_file_path)
        print(f"Fichier CSV '{csv_file_path}' lu avec succès.")

        # Connexion à la base de données
        engine = create_engine(db_url)
        print("Connexion à la base de données réussie.")

        # ici j'insère les données dans la table (création de la table si nécessaire)
        table_name = 'my_table'
        data.to_sql(table_name, engine, if_exists='replace', index=False)
        
        print(f"Les données ont été insérées dans la table {table_name}.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{csv_file_path}' est introuvable.")
    except Exception as e:
        print(f"Erreur : {str(e)}")

copy_data(csv_file_path)