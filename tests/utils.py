import logging
import os
from contextlib import contextmanager
from pathlib import Path
import subprocess

logger = logging.getLogger(__name__)


@contextmanager
def inside_dir(dirpath: Path):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        logger.info("CWD now '%s'", dirpath)
        os.chdir(dirpath)
        yield
    finally:
        logger.info("CWD now '%s'", old_path)
        os.chdir(old_path)


def download_latest_simcore_at(simcore_folder: Path):
    simcore_folder = Path(simcore_folder)
    if any(simcore_folder.glob(".git")):
        subprocess.run("git checkout master".split(), cwd=simcore_folder, check=True)
    else:
        subprocess.run(
            f"git clone --depth 1 https://github.com/ITISFoundation/osparc-simcore {simcore_folder.name}".split(),
            cwd=simcore_folder.parent,
            check=True,
        )