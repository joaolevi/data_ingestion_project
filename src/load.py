import pandas as pd
import sqlalchemy
import os

DB_URL = "postgresql://user:pass@postgres:5432/serrabits"
DATA_DIR = "imdb_data"
engine = sqlalchemy.create_engine(DB_URL)

# Mapeamento dos arquivos para nomes de tabela
tables = {
    "name.basics.tsv": "name_basics",
    "title.basics.tsv": "title_basics",
    # "title.crew.tsv": "title_crew",
    # "title.episode.tsv": "title_episode",
    # "title.principals.tsv": "title_principals",
    # "title.ratings.tsv": "title_ratings",
}

if __name__ == "__main__":
    for file, table in tables.items():
        file_path = os.path.join(DATA_DIR, file)
        print(f"Ingerindo {file} para tabela {table}...")

        # Lê o arquivo em partes
        for chunk in pd.read_csv(file_path, sep="\t", na_values="\\N", low_memory=False, chunksize=1000):
            chunk.to_sql(table, engine, if_exists="append", index=False)

        print(f"Tabela {table} criada com sucesso!")