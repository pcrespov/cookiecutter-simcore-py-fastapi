# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import sys
from pathlib import Path

import pytest

import {{ cookiecutter.package_name }}


pytest_plugins = ["pytest_simcore.repository_paths"]


@pytest.fixture(scope="session")
def project_slug_dir(osparc_simcore_root_dir: Path) -> Path:
    # fixtures in pytest_simcore.environs
    service_folder = osparc_simcore_root_dir / "services" / "{{ cookiecutter.project_slug }}"
    assert service_folder.exists()
    assert any(service_folder.glob("src/{{ cookiecutter.package_name }}"))
    return service_folder


@pytest.fixture(scope="session")
def installed_package_dir() -> Path:
    dirpath = Path({{ cookiecutter.package_name }}.__file__).resolve().parent
    assert dirpath.exists()
    return dirpath
