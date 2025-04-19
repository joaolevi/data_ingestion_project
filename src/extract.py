# src/download.py
import os
import requests
from tqdm import tqdm
import gzip
import shutil
from dotenv import load_dotenv
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

URLS = [
    "https://datasets.imdbws.com/name.basics.tsv.gz",
    "https://datasets.imdbws.com/title.basics.tsv.gz",
    "https://datasets.imdbws.com/title.crew.tsv.gz",
    "https://datasets.imdbws.com/title.episode.tsv.gz",
    "https://datasets.imdbws.com/title.principals.tsv.gz",
    "https://datasets.imdbws.com/title.ratings.tsv.gz",
]

DATA_DIR = os.getenv("DATA_DIR", "imdb_data")
os.makedirs(DATA_DIR, exist_ok=True)

def download_and_extract(url: str):
    filename = url.split("/")[-1]
    gz_path = os.path.join(DATA_DIR, filename)
    tsv_path = gz_path.replace(".gz", "")

    logging.info(f"Baixando {filename}...")
    r = requests.get(url, stream=True, verify=False)
    with open(gz_path, 'wb') as f:
        for chunk in tqdm(r.iter_content(chunk_size=8192)):
            f.write(chunk)

    logging.info(f"Extraindo {filename}...")
    with gzip.open(gz_path, 'rb') as f_in:
        with open(tsv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.remove(gz_path)

if __name__ == "__main__":
    for url in URLS:
        download_and_extract(url)
