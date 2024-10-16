import yaml

def get_database_url():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    return config['db_url']
