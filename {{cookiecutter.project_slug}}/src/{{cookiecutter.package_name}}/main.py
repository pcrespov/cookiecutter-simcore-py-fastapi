"""Main application to be deployed by uvicorn (or equivalent) server

"""
from fastapi import FastAPI
import logging

from {{cookiecutter.package_name}}.core.application import create_app
from {{cookiecutter.package_name}}.core.settings import ApplicationSettings


the_settings = ApplicationSettings.create_from_envs()
logging.basicConfig(level=the_settings.log_level)
logging.root.setLevel(the_settings.log_level)

# SINGLETON FastAPI app
the_app: FastAPI = create_app(the_settings)
