import yaml
import logging

def setup_logging():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    log_level = config.get('log_level', 'INFO')
    log_file = config.get('log_file', 'bot.log')

    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    return logging.getLogger()

