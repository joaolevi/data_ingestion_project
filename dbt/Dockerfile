FROM python:3.13-slim

# Instala dependências
RUN apt-get update && \
    apt-get install -y build-essential git && \
    pip install --no-cache-dir dbt-core dbt-postgres && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

CMD ["bash"]
