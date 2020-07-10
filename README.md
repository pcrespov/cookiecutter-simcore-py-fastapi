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

  Many of the ideas in the service design were taken from the **excellent** work at [fastapi-realworld-example-app](https://github.com/nsidnev/fastapi-realworld-example-app) by *Nik Sidnev* using the **extraordinary** [fastapi](https://fastapi.tiangolo.com/) package by *Sebastian Ramirez*.



<!-- Links below this line !-->
[cookiecutter]:https://cookiecutter.readthedocs.io
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore
[fastapi]:http://fastapi.tiangolo.com/