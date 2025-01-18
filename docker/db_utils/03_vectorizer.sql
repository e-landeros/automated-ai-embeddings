
-- Create the vectorizer
SELECT ai.create_vectorizer(
    'documentation'::regclass,
    destination => 'documentation_embeddings',
    embedding => ai.embedding_ollama('nomic-embed-text', 768),
    chunking => ai.chunking_recursive_character_text_splitter('content')
);