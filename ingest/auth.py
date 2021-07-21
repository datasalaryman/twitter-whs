import yaml

# NOTE: Add Twitter credentials in .secrets/twitter-creds.yml in main repo directory

with open(".secrets/twitter-creds.yml", "r") as stream:
    creds = (yaml.load(stream, Loader=yaml.FullLoader))


