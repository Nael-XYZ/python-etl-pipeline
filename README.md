# Python ETL Pipeline

A robust ETL pipeline for data processing using Python and PostgreSQL.

## Features
- Extract data from multiple sources (CSV, JSON, API)
- Transform with pandas
- Load into PostgreSQL
- Logging and error handling
- Configurable via YAML

## Setup
```bash
pip install -r requirements.txt
python main.py --config config.yaml
```

## Structure
```
extractors/   → Data source connectors
transformers/ → Data transformation logic
loaders/      → Database loading utilities
```

## License
MIT
