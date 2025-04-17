import pandas as pd
import sqlalchemy
import os

DB_URL = "postgresql://user:pass@postgres:5432/serrabits"
DATA_DIR = "imdb_data"
engine = sqlalchemy.create_engine(DB_URL)

def clean_name_basics(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk['nconst'] = df_chunk['nconst'].str.replace("nm", "")
    df_chunk['nconst'] = df_chunk['nconst'].astype(int, errors='ignore')
    df_chunk['birthYear'] = pd.to_numeric(df_chunk['birthYear'], errors='coerce')
    df_chunk['birthYear'] = df_chunk['birthYear'].astype(int, errors='ignore')
    df_chunk['deathYear'] = pd.to_numeric(df_chunk['deathYear'], errors='coerce')
    df_chunk['deathYear'] = df_chunk['deathYear'].astype(int, errors='ignore')
    df_chunk = df_chunk.dropna(subset=["nconst"])

    return df_chunk

def clean_title_basics(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['isAdult'] = df_chunk['isAdult'].astype(int)
    df_chunk['startYear'] = df_chunk['startYear'].astype(int)
    df_chunk['endYear'] = df_chunk['endYear'].astype(int)
    
    df_chunk['runtimeMinutes'] = pd.to_numeric(df_chunk['runtimeMinutes'], errors='coerce')
    df_chunk['runtimeMinutes'] = df_chunk['runtimeMinutes'].astype(int)

    return df_chunk

def clean_title_principals(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst", "nconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['nconst'] = df_chunk['nconst'].str.replace("nm", "")
    df_chunk['nconst'] = df_chunk['nconst'].astype(int)

    return df_chunk

def clean_title_ratings(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['averageRating'] = pd.to_numeric(df_chunk['averageRating'], errors='coerce')
    df_chunk['numVotes'] = pd.to_numeric(df_chunk['numVotes'], errors='coerce')

    return df_chunk

def clean_title_episode(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst", "parentTconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['parentTconst'] = df_chunk['parentTconst'].str.replace("tt", "")
    df_chunk['parentTconst'] = df_chunk['parentTconst'].astype(int)

    return df_chunk

def clean_title_crew(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst", "directors"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)

    # Converte a coluna 'directors' para uma lista de inteiros
    df_chunk['directors'] = df_chunk['directors'].str.split(",").apply(lambda x: [int(director.replace("nm", "")) for director in x])
    df_chunk['writes'] = df_chunk['writes'].str.split(",").apply(lambda x: [int(director.replace("nm", "")) for director in x])

    return df_chunk

def clean_akas(df_chunk):
    # Remove linhas com valores ausentes
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['isOriginalTitle'] = df_chunk['isOriginalTitle'].astype(bool)

    return df_chunk

# Mapeamento dos arquivos para nomes de tabela
tables = {
    "name.basics.tsv": {
        "function": clean_name_basics,
        "table": "TB_NAME_BASICS",
    },
    "title.basics.tsv": {
        "function": clean_title_basics,
        "table": "TB_TITLE_BASICS",
    },
    # "title.principals.tsv": {
    #     "function": clean_title_principals,
    #     "table": "TB_TITLE_PRINCIPALS",
    # },
    # "title.ratings.tsv": {
    #     "function": clean_title_ratings,
    #     "table": "TB_TITLE_RATINGS",
    # },
    # "title.episode.tsv": {
    #     "function": clean_title_episode,
    #     "table": "TB_TITLE_EPISODE",
    # },
    # "title.crew.tsv": {
    #     "function": clean_title_crew,
    #     "table": "TB_TITLE_CREW",
    # },
    # "akas.tsv": {
    #     "function": clean_akas,
    #     "table": "TB_TITLE_AKAS",
    # },
}

if __name__ == "__main__":
    for filename, info in tables.items():
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Arquivo {filepath} não encontrado.")
            continue

        # Lê o arquivo em pedaços
        for chunk in pd.read_csv(filepath, sep="\t", chunksize=100000, encoding="utf-8", low_memory=False):
            # Limpa os dados
            cleaned_chunk = info["function"](chunk)

            # Insere os dados no banco de dados
            cleaned_chunk.to_sql(info["table"], engine, if_exists="append", index=False)