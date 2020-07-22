""" Main application entry point

 `python -m {{ cookiecutter.package_name }} ...`

"""
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from {{ cookiecutter.package_name }}.core.application import init_app
from {{ cookiecutter.package_name }}.core.settings import AppSettings, BootModeEnum

current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent


# SINGLETON FastAPI app
the_app: FastAPI = init_app()


def main():
    cfg: AppSettings = the_app.state.settings
    uvicorn.run(
        "{{ cookiecutter.package_name }}.__main__:the_app",
        host=cfg.host,
        port=cfg.port,
        reload=cfg.boot_mode == BootModeEnum.development,
        reload_dirs=[current_dir,],
        log_level=cfg.log_level_name.lower(),
    )


if __name__ == "__main__":
    main()
