````markdown
# Automated AI Embeddings with PostgreSQL and pgAI

This project demonstrates how to leverage the pgAI extension for PostgreSQL to efficiently manage and query AI embeddings within your database. By automating the embedding process, we simplify the integration of AI capabilities into your applications. This example uses Ollama to generate embeddings and store them in PostgreSQL.

## Key Features

* **Automated Embeddings:** pgAI automatically generates and updates embeddings for new or modified data.
* **Efficient Storage:**  Leverage PostgreSQL's robust data management capabilities for your embeddings.
* **Simplified Queries:** Easily perform similarity searches and other vector-based queries directly within PostgreSQL.
* **Scalability:** Benefit from PostgreSQL's scalability to handle large datasets and complex AI applications.

## Requirements

* Docker
* PostgreSQL
* TimescaleDB
* pgAI extension
* Ollama
* Python 3.x

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/e-landeros/automated-ai-embeddings.git](https://github.com/e-landeros/automated-ai-embeddings.git)
   cd yourproject
````

2.  **Build and run the Docker container:**

    ```bash
    docker-compose up --build
    ```

3.  **Connect to the database:**

    ```bash
    docker compose exec -it db psql
    ```

4.  **Enable required extensions:**

    ```sql
    CREATE EXTENSION IF NOT EXISTS vector;
    CREATE EXTENSION IF NOT EXISTS ai CASCADE;
    ```

5.  **Create the documentation table:**

    ```sql
    CREATE TABLE documentation (
        id SERIAL PRIMARY KEY,
        source_file TEXT,
        title TEXT,
        content TEXT,
        metadata JSONB
    );
    ```

6.  **Download sample data:**

    ```bash
    git clone [https://github.com/pydantic/pydantic-ai.git](https://github.com/pydantic/pydantic-ai.git) data
    ```

7.  **Process and load data:** (Use the provided scripts to clean, chunk, and load the data into the `documentation` table.)

8.  **Create the vectorizer:**

    ```sql
    SELECT ai.create_vectorizer(
        'documentation'::regclass,
        destination => 'documentation_embeddings',
        embedding => ai.embedding_ollama('nomic-embed-text', 768),
        chunking => ai.chunking_recursive_character_text_splitter('content')
    );
    ```

9.  **Monitor the vectorizer worker:**

    ```bash
    docker compose logs -f vectorizer-worker
    ```

## Usage

**Querying Embeddings:**

```sql
-- Semantic Search
SELECT
    content,
    embedding <=> ai.ollama_embed('nomic-embed-text', 'what is an agent?', host => 'http://ollama:11434') as distance
FROM documentation_embeddings
ORDER BY distance
LIMIT 5;
```

## Contributing

Contributions are welcome\! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](https://www.google.com/url?sa=E&source=gmail&q=LICENSE).

