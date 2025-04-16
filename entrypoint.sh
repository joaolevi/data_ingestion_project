#!/bin/bash

set -e

echo "Iniciando processo de download..."
poetry run python src/extract.py

echo "Download finalizado. Iniciando ingestão..."
poetry run python src/load.py

echo "Ingestão finalizada."

# Mantém o container vivo se necessário
exec "$@"