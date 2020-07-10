# Cookiecutter simcore-py-fastapi

[![Build Status](https://travis-ci.com/pcrespov/cookiecutter-simcore-py-fastapi.svg?branch=master)](https://travis-ci.com/pcrespov/cookiecutter-simcore-py-fastapi)
[![Requirements Status](https://requires.io/github/pcrespov/cookiecutter-simcore-py-fastapi/requirements.svg?branch=master)](https://requires.io/github/pcrespov/cookiecutter-simcore-py-fastapi?branch=master)
[![license](https://img.shields.io/github/license/pcrespov/cookiecutter-simcore-py-fastapi)](LICENSE)

Cookiecutter template for [osparc-simcore]'s services based in [fastapi].

## Requirements

- git
- python >=3.6
  - `pip install cookiecutter`
- docker

## Usage

To generate a new cookiecutter template layout just type

```cmd
cookiecutter gh:pcrespov/cookiecutter-simcore-py-fastapi
```

and answer the questions.

---

## Development

All recipes for developmet are implemented in the root's [Makefile](Makefile)

```console
make help
```

See also [CHANGELOG](CHANGELOG.md).

---

## Acknoledgements

This template was built upon ideas/snippets borrowed from already existing great [cookiecutter]s such as [gh:ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary), [gh:alexkey/cookiecutter-lux-python](https://github.com/alexkey/cookiecutter-lux-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) or [gh:mdklatt/cookiecutter-python-app](https://github.com/mdklatt/cookiecutter-python-app).

## License

This project is licensed under the terms of the [MIT License](/LICENSE)

<!-- Links below this line !-->
[cookiecutter]:https://cookiecutter.readthedocs.io
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore
[fastapi]:http://fastapi.tiangolo.com/