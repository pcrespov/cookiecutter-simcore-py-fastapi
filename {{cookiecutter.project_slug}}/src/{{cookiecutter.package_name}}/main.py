"""Main application to be deployed in for example uvicorn
"""
from fastapi import FastAPI
from {{cookiecutter.package_name}}.core.application import create_app


# SINGLETON FastAPI app
the_app: FastAPI = create_app()
