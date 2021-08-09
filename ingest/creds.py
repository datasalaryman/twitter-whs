import yaml

# NOTE: Add Twitter credentials in .secrets/twitter-creds.yml in main repo directory

with open(".secrets/twitter-creds.yml", "r") as stream:
    creds = (yaml.load(stream, Loader=yaml.FullLoader))

def api_key():
    return creds['api_key']

def api_secret():
    return creds['api_secret']

def bearer_token():
    return creds['bearer_token']
