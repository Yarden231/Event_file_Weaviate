import os
import weaviate
import json
import requests
import pandas as pd
import math
import numpy as np

os.environ["OPENAI_APIKEY"] = "Replace with OPENAI_APIKEY"


def configure_batch(client: Client, batch_size: int, batch_target_rate: int):
    """
    Configure the weaviate client's batch so it creates objects at `batch_target_rate`.

    Parameters
    ----------
    client : Client
        The Weaviate client instance.
    batch_size : int
        The batch size.
    batch_target_rate : int
        The batch target rate as # of objects per second.
    """

    def callback(batch_results: dict) -> None:

        # you could print batch errors here
        time_took_to_create_batch = batch_size * (client.batch.creation_time/client.batch.recommended_num_objects)
        time.sleep(
            max(batch_size/batch_target_rate - time_took_to_create_batch + 1, 0)
        )

    client.batch.configure(
        batch_size=batch_size,
        timeout_retries=5,
        callback=callback,
    )



def validate_data(data):
    for key, value in list(data.items()):  # Using list() to prevent 'dictionary changed size during iteration' error
        if isinstance(value, (int, float)):
            if value is None or math.isinf(value) or math.isnan(value):
                del data[key]  # delete the key-value pair completely
    return data


def tsv_to_json(file_path):
    events = []
    with open(file_path, 'r') as file:
        for line in file:
            name, description = line.strip().split('\t')
            event_data = {
                'eventName': name,
                'description': description
            }
            events.append(event_data)

    return json.dumps(events, indent=4)



client = weaviate.Client(
    url="https://cluster1-kedu3lyz.weaviate.network",
    auth_client_secret=weaviate.AuthApiKey(api_key="Replace here"),
    additional_headers={
        "X-Openai-Api-Key": "##### Replace with OPENAI_APIKEY ####"
    }
)

#client.schema.delete_class("Event")

class_obj = {
    "class": "Event",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        }
    },
    "properties": [
        {
            "name": "eventName",
            "dataType": ["string"]
        },
        {
            "name": "description",
            "dataType": ["string"]
        }
    ]
}

client.schema.create_class(class_obj)

# Load data
data = pd.read_csv(r'C:\Users\ycohe\Desktop\first_100.csv', encoding='cp1252', header=None,
                   names=['eventName', 'description'])

with client.batch(batch_size=100) as batch:
    # Batch import all Events
    for i, d in data.iterrows():
        print(f"Importing event: {i + 1}")

        properties = {
            "eventName": d["eventName"],
            "description": d["description"],
        }

        # Validate and clean data before adding to batch
        properties = validate_data(properties)

        batch.add_data_object(properties, "Event")
        print(f"Event {i + 1} added to batch successfully!")
