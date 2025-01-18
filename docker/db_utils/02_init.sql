-- Create the documentation table
CREATE TABLE documentation (
    id SERIAL PRIMARY KEY,
    source_file TEXT,
    title TEXT,
    content TEXT,
    metadata JSONB
);