""" Current version of the {{ cookiecutter.package_name }} application.
"""
import pkg_resources

__version__ = pkg_resources.get_distribution('{{ cookiecutter.package_name }}').version

major, minor, patch = __version__.split(".")

api_version: str = __version__
api_vtag: str = f"v{major}"
