import pandas as pd
import sqlalchemy
import os
import logging

from dotenv import load_dotenv

from transform import *

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()


DB_URL = os.getenv("DB_URL", "postgresql://user:pass@postgres:5432/serrabits")
DATA_DIR = os.getenv("DATA_DIR", "imdb_data")
engine = sqlalchemy.create_engine(DB_URL)

tables = {
    "name.basics.tsv": {
        "function": clean_name_basics,
        "table": "TB_NAME_BASICS",
    },
    "title.basics.tsv": {
        "function": clean_title_basics,
        "table": "TB_TITLE_BASICS",
    },
    "title.principals.tsv": {
        "function": clean_title_principals,
        "table": "TB_TITLE_PRINCIPALS",
    },
    "title.ratings.tsv": {
        "function": clean_title_ratings,
        "table": "TB_TITLE_RATINGS",
    },
    "title.episode.tsv": {
        "function": clean_title_episode,
        "table": "TB_TITLE_EPISODE",
    },
    "title.crew.tsv": {
        "function": clean_title_crew,
        "table": "TB_TITLE_CREW",
    },
    "title.akas.tsv": {
        "function": clean_akas,
        "table": "TB_TITLE_AKAS",
    },
}

if __name__ == "__main__":
    for filename, info in tables.items():
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            logging.info(f"Arquivo {filepath} não encontrado.")
            continue

        for chunk in pd.read_csv(filepath, sep="\t", chunksize=100000, encoding="utf-8", low_memory=False):
            cleaned_chunk = info["function"](chunk)
            cleaned_chunk.to_sql(info["table"], engine, if_exists="append", index=False)