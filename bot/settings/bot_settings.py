import yaml

def get_bot_token():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config.get('telegram_token')
