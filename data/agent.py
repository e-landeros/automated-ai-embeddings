import psycopg2
import json
from psycopg2.extras import execute_values

from pydantic_ai import Agent, Tool
from pydantic import BaseModel
from pydantic_ai.models.ollama import OllamaModel

import nest_asyncio
nest_asyncio.apply()

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def fetch_search_results(search_text):
    # Reconnect to the database
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Define the query with a placeholder
    query = """
    SELECT
        content,
        embedding <=> ai.ollama_embed('nomic-embed-text', %s, host => 'http://ollama:11434') as distance
    FROM documentation_embeddings
    ORDER BY distance
    LIMIT 1;
    """

    try:
        # Execute the query with the search_text variable
        cur.execute(query, (search_text,))
        results = cur.fetchall()
        
        # Print results in markdown format
        for row in results:
            print(f"## Search Result (Distance: {row[1]:.4f})\n")
            # add markdown formatting
            print(f"{row[0]}\n")
            print("---\n")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Always close cursor and connection
        cur.close()
        conn.close()


ollama_model = OllamaModel(
    model_name='llama3.2',  
    base_url='http://localhost:11434/v1/',  
)

agent = Agent(ollama_model)


result = agent.run_sync('Where were the olympics held in 2011?')
print(result.data)
print(result.usage())