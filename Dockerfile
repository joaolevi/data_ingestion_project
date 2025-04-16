FROM python:3.11-slim

# 1. Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y curl build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.8.2
# 3. Adiciona Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"
    
# 4. Define o diretório de trabalho
WORKDIR /app

# 5. Copia os arquivos do projeto
COPY pyproject.toml poetry.lock* ./
RUN poetry install

# 6. Instala as dependências usando o Poetry
RUN poetry install --no-root

# 7. Copia o restante do código (src/ e entrypoint.sh)
COPY src/ ./src/
COPY entrypoint.sh /app/entrypoint.sh

# 8. Dar permissão de execução para o script de entrada
RUN chmod +x /app/entrypoint.sh

# 9. Definir o entrypoint
ENTRYPOINT ["poetry", "run", "/app/entrypoint.sh"]