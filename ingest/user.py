from ingest.creds import api_url, headers
import requests

from dagster import pipeline, solid

import csv
import json

with open('.secrets/users-to-follow.csv') as f:
    users = [line.rstrip() for line in f]

@solid
def user_ingest(context):
    user_data = []
    for user in users:
        user_data = user_data + [
            requests.get(
                api_url() + f'users/{user}', 
                headers=headers()
            ).text
        ]
    context.log.info(f"Found {len(user_data)} users")
    return user_data

@solid
def user_write(context, users):
    context.log.info(users[0])
    context.log.info(str(json.loads(users[0])))
    users = [json.loads(user)["data"] for user in users]
    keys = users[0].keys()
    with open('out/users.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(users)

