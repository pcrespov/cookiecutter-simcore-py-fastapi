""" Current version of the {{ cookiecutter.package_name }} application.
"""
import pkg_resources

__version__ = pkg_resources.get_distribution('{{ cookiecutter.package_name }}').version
assert __version__=="{{ cookiecutter.version }}", "Did you `pip install` this package?" # nosec

major, minor, patch = __version__.split(".")

api_version = __version__
api_vtag: str = f"v{major}"
