# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import sys
from pathlib import Path

import pytest

import {{ cookiecutter.package_name }}

current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent
pytest_plugins = ["pytest_simcore.environs"]


@pytest.fixture(scope="session")
def project_slug_dir(osparc_simcore_root_dir) -> Path:
    # uses pytest_simcore.environs.osparc_simcore_root_dir
    service_folder = osparc_simcore_root_dir / "services" / "{{ cookiecutter.project_slug }}"
    assert service_folder.exists()
    assert any(service_folder.glob("src/{{ cookiecutter.package_name }}"))
    return service_folder


@pytest.fixture(scope="session")
def installed_package_dir() -> Path:
    dirpath = Path({{ cookiecutter.package_name }}.__file__).resolve().parent
    assert dirpath.exists()
    return dirpath
