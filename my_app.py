from dataclasses import dataclass, field
from typing import Any, List

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf, MISSING

@dataclass
class DBConfig:
    host: str = "localhost"
    port: int = MISSING
    driver: str = MISSING

@dataclass
class MySQLConfig(DBConfig):
    driver: str = "mysql"
    port: int = 3306

@dataclass
class PostGreSQLConfig(DBConfig):
    driver: str = "postgresql"
    port: int = 5432
    timeout: int = 10

defaults = [
    {"db": "postgresql"}
]


@dataclass
class Config:
    defaults: List[Any] = field(default_factory=lambda: defaults)
    db: Any = MISSING

# @dataclass
# class MyConfig:
#     db: PostgresSQLConfig = field(default_factory=PostgresSQLConfig)
#     ui: UserInterface = field(default_factory=UserInterface)


cs = ConfigStore.instance()
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)
cs.store(name="config", node=Config)


@hydra.main(version_base=None, config_name="config")
def my_app(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))
    print('=============================')
    # print(f"Title={cfg.ui.title}, size={cfg.ui.width}x{cfg.ui.height} pixels")


if __name__ == "__main__":
    my_app()
