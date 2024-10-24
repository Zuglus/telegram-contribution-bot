from dataclasses import dataclass
from environs import Env

@dataclass
class BotConfig:
    token: str

@dataclass
class Config:
    bot: BotConfig

def load_config() -> Config:
    env = Env()
    env.read_env()
    
    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN")
        )
    )