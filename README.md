imdb_pipeline/
├── docker-compose.yml
├── .env
├── postgres/
│   └── init.sql
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── download.py          # Faz download e extração dos datasets .tsv.gz
│   ├── ingest.py            # Carrega os arquivos no PostgreSQL
│   └── transform.py         # Limpezas ou transformações adicionais
├── requirements.txt
├── dbt/                     # (opcional) DBT models para BI e cientistas
└── README.md

dbt/
├── Dockerfile                       # Dockerfile que usamos para build do container DBT
├── dbt_project.yml                  # Configuração principal do projeto DBT
├── profiles.yml                     # Configurações de conexão com o banco
├── models/
│   ├── basic_info.sql               # Modelo que retorna nome + ano de nascimento/morte
│   ├── known_actors.sql             # Modelo com atores/atrizes da tabela name_basics
│   └── staging/
│       ├── name_basics.sql          # (opcional) staging dos dados brutos
│       └── ...                      # outros arquivos de staging
├── snapshots/                       # (opcional) snapshots para versionar dados
├── seeds/                           # (opcional) arquivos CSV carregáveis como tabelas
├── macros/                          # (opcional) funções Jinja personalizadas
└── tests/                           # (opcional) testes personalizados ou complexos

