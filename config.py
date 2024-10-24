from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str  # Путь к файлу SQLite

@dataclass
class BotConfig:
    token: str
    admin_id: int  # Telegram ID администратора

@dataclass
class Config:
    bot: BotConfig
    database: DatabaseConfig  # Изменили имя атрибута с db на database

def load_config() -> Config:
    env = Env()
    env.read_env()
    
    return Config(
        database=DatabaseConfig(  # Изменили имя атрибута с db на database
            database=env.str("DATABASE_URL")
        ),
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
            admin_id=env.int("ADMIN_ID")
        )
    )