import pandas as pd

def clean_name_basics(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk['nconst'] = df_chunk['nconst'].str.replace("nm", "")
    df_chunk['nconst'] = df_chunk['nconst'].astype(int, errors='ignore')
    df_chunk['birthYear'] = pd.to_numeric(df_chunk['birthYear'], errors='coerce')
    df_chunk['birthYear'] = df_chunk['birthYear'].astype(int, errors='ignore')
    df_chunk['deathYear'] = pd.to_numeric(df_chunk['deathYear'], errors='coerce')
    df_chunk['deathYear'] = df_chunk['deathYear'].astype(int, errors='ignore')
    df_chunk = df_chunk.dropna(subset=["nconst"])

    return df_chunk

def clean_title_basics(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    
    df_chunk['isAdult'] = pd.to_numeric(df_chunk['isAdult'], errors='coerce')
    df_chunk['isAdult'] = df_chunk['isAdult'].astype(int, errors='ignore')
    
    df_chunk['startYear'] = pd.to_numeric(df_chunk['startYear'], errors='coerce')
    df_chunk['startYear'] = df_chunk['startYear'].astype(int, errors='ignore')
    
    df_chunk['endYear'] = pd.to_numeric(df_chunk['endYear'], errors='coerce')
    df_chunk['endYear'] = df_chunk['endYear'].astype(int, errors='ignore')
    
    df_chunk['runtimeMinutes'] = pd.to_numeric(df_chunk['runtimeMinutes'], errors='coerce')
    df_chunk['runtimeMinutes'] = df_chunk['runtimeMinutes'].astype(int, errors='ignore')

    return df_chunk

def clean_title_principals(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["tconst", "nconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['nconst'] = df_chunk['nconst'].str.replace("nm", "")
    df_chunk['nconst'] = df_chunk['nconst'].astype(int)
    
    df_chunk['ordering'] = pd.to_numeric(df_chunk['ordering'], errors='coerce')
    df_chunk['ordering'] = df_chunk['ordering'].astype(int, errors='ignore')
    
    df_chunk['characters'] = df_chunk['characters'].str.replace(r'\[|\]', '', regex=True).str.strip('"')

    return df_chunk

def clean_title_ratings(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['averageRating'] = pd.to_numeric(df_chunk['averageRating'], errors='coerce')
    
    df_chunk['numVotes'] = pd.to_numeric(df_chunk['numVotes'], errors='coerce')
    df_chunk['numVotes'] = df_chunk['numVotes'].astype(int, errors='ignore')

    return df_chunk

def clean_title_episode(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["tconst", "parentTconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)
    df_chunk['parentTconst'] = df_chunk['parentTconst'].str.replace("tt", "")
    df_chunk['parentTconst'] = df_chunk['parentTconst'].astype(int)
    
    df_chunk['seasonNumber'] = pd.to_numeric(df_chunk['seasonNumber'], errors='coerce')
    df_chunk['seasonNumber'] = df_chunk['seasonNumber'].astype(int, errors='ignore')
    df_chunk['episodeNumber'] = pd.to_numeric(df_chunk['episodeNumber'], errors='coerce')
    df_chunk['episodeNumber'] = df_chunk['episodeNumber'].astype(int, errors='ignore')

    return df_chunk

def clean_title_crew(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["tconst"])
    df_chunk['tconst'] = df_chunk['tconst'].str.replace("tt", "")
    df_chunk['tconst'] = df_chunk['tconst'].astype(int)

    df_chunk['directors'] = df_chunk['directors'].str.replace("nm", "")
    df_chunk['directors'] = pd.to_numeric(df_chunk['directors'], errors='coerce')
    df_chunk['directors'] = df_chunk['directors'].astype(int, errors='ignore')

    df_chunk['writers'] = df_chunk['writers'].str.replace("nm", "")
    df_chunk['writers'] = pd.to_numeric(df_chunk['writers'], errors='coerce')
    df_chunk['writers'] = df_chunk['writers'].astype(int, errors='ignore')

    return df_chunk

def clean_akas(df_chunk: pd.DataFrame) -> pd.DataFrame:
    df_chunk = df_chunk.dropna(subset=["titleId"])
    df_chunk['titleId'] = df_chunk['titleId'].str.replace("tt", "")
    
    df_chunk['ordering'] = pd.to_numeric(df_chunk['ordering'], errors='coerce')
    df_chunk['ordering'] = df_chunk['ordering'].astype(int, errors='ignore')
    
    df_chunk['isOriginalTitle'] = pd.to_numeric(df_chunk['isOriginalTitle'], errors='coerce')
    df_chunk['isOriginalTitle'] = df_chunk['isOriginalTitle'].astype(int, errors='ignore')

    return df_chunk
