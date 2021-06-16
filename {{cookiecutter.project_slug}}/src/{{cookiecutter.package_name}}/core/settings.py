{% set package_prefix = cookiecutter.project_slug.upper() -%}

from typing import Optional

from pydantic import Field

from models_library.settings.base import BaseCustomSettings
from models_library.settings.postgres import PostgresSettings
from models_library.basic_types import LogLevel, BootModeEnum, BuildTargetEnum


class Settings(BaseCustomSettings):
    # DOCKER
    SC_BOOT_MODE: Optional[BootModeEnum]
    SC_BOOT_TARGET: Optional[BuildTargetEnum]


    {{ package_prefix }}_LOG_LEVEL: LogLevel = Field(
        LogLevel.INFO, env=["{{ package_prefix }}_LOGLEVEL", "LOG_LEVEL", "LOGLEVEL"]
    )

    {{ package_prefix }}_POSTGRES: PostgresSettings

    @classmethod
    def create_from_envs(cls) -> "Settings":
        cls.set_defaults_with_default_constructors(
            [
                ("{{ package_prefix }}_POSTGRES", PostgresSettings),
            ]
        )
        return cls()
