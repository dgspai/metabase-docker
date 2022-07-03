# Metabase-docker
Simple repository for playing with metabase + mongo with docker

## Repository guides

## Requirements

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)
- Python 3+

## Starting up metabase stack

1. Rename .env.example
   1. Change its default values
2. Rune `docker-compose up`

## Importing data

1. Install python requirements running `pip install -r requirements.txt`
2. Edit the file `import_to_mongo.py` 
   1. Set the right `input_file` with your data file
   2. Set the right `output_db` (It will be created if it doesn't exist)
   3. Set the right `output_collection` (It will be created if it doesn't exist)
3. Run `python import_to_mongo.py`

## Stopping metabase stack when you're done

Run `docker-compose down`

# Tools information

- [Docker](https://www.docker.com/get-started/)
- [Mongo](https://www.mongodb.com/docs/manual/tutorial/getting-started/)
- [mongo-express](https://github.com/mongo-express/mongo-express)
- [Metabase](https://www.metabase.com/docs/latest/users-guide/01-what-is-metabase.html)
- [Connecting Metabase to MongoDB](https://www.metabase.com/docs/latest/administration-guide/databases/mongodb.html#connecting-to-mongodb)