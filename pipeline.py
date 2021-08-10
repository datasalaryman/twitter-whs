from dagster import pipeline
from ingest.user import user_ingest, user_write

@pipeline
def user_pipeline():
    user_write(user_ingest())
    