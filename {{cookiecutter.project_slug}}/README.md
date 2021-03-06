# {{ cookiecutter.project_slug }}

[![image-size]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }}. "More on itisfoundation/{{ cookiecutter.project_slug }}.:staging-latest image")

[![image-badge]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![image-version]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![image-commit]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")

{{ cookiecutter.project_short_description }}

<!-- Add badges urls here-->
[image-size]:https://img.shields.io/microbadger/image-size/itisfoundation/{{ cookiecutter.project_slug }}./staging-latest.svg?label={{ cookiecutter.project_slug }}.&style=flat
[image-badge]:https://images.microbadger.com/badges/image/itisfoundation/{{ cookiecutter.project_slug }}.svg
[image-version]https://images.microbadger.com/badges/version/itisfoundation/{{ cookiecutter.project_slug }}.svg
[image-commit]:https://images.microbadger.com/badges/commit/itisfoundation/{{ cookiecutter.project_slug }}.svg
<!------------------------->

## Development

Setup environment

```cmd
make devenv
source .venv/bin/activate
cd services/api-service
make install-dev
```

Then

```cmd
make run-devel
```

The latter will start the {{ cookiecutter.project_slug }} service in development-mode together with a postgres db initialized with test data. Open the following sites and use the test credentials ``user=key, password=secret`` to manually test the API:

- http://127.0.0.1:8000/doc: swagger-like api documentation
