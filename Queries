import os
import weaviate
import json
import requests


os.environ["OPENAI_APIKEY"] = "#### ADD ####"

client = weaviate.Client(
    url="https://cluster1-kedu3lyz.weaviate.network",
    auth_client_secret=weaviate.AuthApiKey(api_key="YwATdOchKm3PBAv7LoXQv2nnZ51F2JNyF9nX"),
    additional_headers={
        "X-Openai-Api-Key": "#### ADD ####",
    }
)


nearText = {"concepts": ["Index (PMI) Final in France"]}

response = (
    client.query
    .get("Event", ["eventName", "description"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))
