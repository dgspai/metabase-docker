import os
import logging

import dotenv
import pandas as pd
import pymongo

# Data configs
input_file = "./data/2019-05-28_portuguese_hate_speech_binary_classification.csv"
output_db = "my_db"
output_collection = "hate_speech_binary"

# Load mongo configs from .env file
dotenv.load_dotenv()
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = os.getenv("MONGO_PORT")
mongo_user = os.getenv("MONGO_USER")
mongo_pass = os.getenv("MONGO_PASS")

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

if __name__ == "__main__":
    # connect to mongo, db and collection
    connection_string = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"
    logging.info(f"Connecting to {connection_string}")
    mongo_client = pymongo.MongoClient(connection_string)
    mongo_db = mongo_client[output_db]
    mongo_collection = mongo_db[output_collection]

    # read csv file
    logging.info(f"Reading {input_file}")
    df = pd.read_csv(input_file)
    logging.info(f"File shape {df.shape}")

    # you could change datatypes here to use more filters on metabase
    # df["date"] = pd.to_datetime(df["creation_date"])

    # save to mongo
    logging.info(f"Saving to {output_db}/{output_collection}")
    mongo_collection.insert_many(df.to_dict("records"))
    logging.info("Done!")
