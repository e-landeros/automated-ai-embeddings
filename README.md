# Automated AI Embeddings with PostgreSQL

## Introduction

This guide demonstrates how to use the new PGAI extension from Timescale to build amazing AI applications by moving the hard parts to the database. This project aims to simplify the integration of AI embeddings into your PostgreSQL database, making it easier to manage and query your data.

## Requirements

- Docker
- PostgreSQL
- Ollama
- Python 3.x

## Setting Up a Virtual Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

3. Set up the PostgreSQL database:
   ```bash
   # Instructions for setting up the database
   ```

4. Connect to the database 
docker compose exec -it db psql

5. run 01 and 02 sql files in the db_utils folder

6. download data into the data folder. 
git clone https://github.com/pydantic/pydantic-ai.git
this is just sample data i am downloading th epydantic ai library. 
we will chunk it up and store it in the database then vectorize it

7. use markdown scraper to clena up the data then chunk it up generate metadata and store it in the dtaabase table
ye its not processed yet jsut using psyco pg to

8. now run the 03 vectorizer 
this will create a new tabel usign the vectorizer worker and taake the data from the tbale and generate the embeddings and store it in a new table. the pgai library will do allthe sync automatically and check in for new data/ 

9. so how do we query the databse?



## Usage

- After setting up the environment, you can start using the PGAI extension by following these steps:
  1. Connect to your PostgreSQL database.
  2. Use the provided scripts to create embeddings.
  3. Query the embeddings as needed.

## Contributing

We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.