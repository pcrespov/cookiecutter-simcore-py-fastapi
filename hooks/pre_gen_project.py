import os
from pathlib import Path

work_dir = Path(os.getcwd()).resolve()
module_name = "{{ cookiecutter.project_slug }}"

print(f"Buidling {module_name} in '{work_dir}' ...")
