-- Semantic Search
SELECT
    content,
    embedding <=> ai.ollama_embed('nomic-embed-text', 'what is an agent?', host => 'http://ollama:11434') as distance
FROM documentation_embeddings
ORDER BY distance
LIMIT 5;