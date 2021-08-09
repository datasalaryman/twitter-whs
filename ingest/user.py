from creds import api_url, headers
import requests

from dagster import pipeline, solid

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

@pipeline
def user_pipeline():
    user_ingest()

from dagster import execute_pipeline

if __name__ == "__main__":
    result = execute_pipeline(user_pipeline)
