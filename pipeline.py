from dagster import pipeline
from ingest.user import user_ingest

@pipeline
def user_pipeline():
    user_ingest()