# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import sys
from pathlib import Path
import pytest
import os

from utils import download_latest_simcore_at

current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent


@pytest.fixture(scope="session")
def repo_dir() -> Path:
    repo_path = current_dir.parent
    assert any(repo_path.glob(".git"))
    return repo_path


@pytest.fixture(scope="session")
def pylintrc(repo_dir) -> Path:
    path = repo_dir / ".pylintrc"
    assert path.exists()
    return path


@pytest.fixture(scope="session")
def cached_output_dir(repo_dir) -> Path:
    cache_dir = repo_dir / ".output-cached"
    os.makedirs(cache_dir)
    return cache_dir


@pytest.fixture(scope="session")
def osparc_simcore_repo(cached_output_dir) -> Path:
    simcore_folder = cached_output_dir / "osparc-simcore"

    download_latest_simcore_at(simcore_folder)
    assert simcore_folder.exists()
    assert (simcore_folder / "services").exists()
    return simcore_folder


@pytest.fixture(scope="session")
def osparc_simcore_services_folder(osparc_simcore_repo):
    return osparc_simcore_repo / "services"
