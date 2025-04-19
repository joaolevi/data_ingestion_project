FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y curl build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.8.2
ENV PATH="/root/.local/bin:$PATH"
    
WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN poetry install
RUN poetry install --no-root

COPY src/ ./src/
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["poetry", "run", "/app/entrypoint.sh"]