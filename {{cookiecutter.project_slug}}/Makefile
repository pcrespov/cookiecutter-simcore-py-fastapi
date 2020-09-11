#
# DEVELOPMENT recipes for {{ cookiecutter.project_name }}
#
include ../../scripts/common.Makefile

# Custom variables
APP_NAME         := $(notdir $(CURDIR))
APP_CLI_NAME     := {{ cookiecutter.command_line_interface_bin_name }}
APP_PACKAGE_NAME := $(subst -,_,$(APP_CLI_NAME))
APP_VERSION      := $(shell cat VERSION)
SRC_DIR          := $(abspath $(CURDIR)/src/$(APP_PACKAGE_NAME))

export APP_VERSION

.PHONY: requirements reqs
requirements reqs: ## (or reqs) compiles pip requirements (.in -> .txt)
	@$(MAKE_C) requirements reqs


.PHONY: install-dev install-prod install-ci
install-dev install-prod install-ci: requirements _check_venv_active ## install app in development/production or CI mode
	# installing in $(subst install-,,$@) mode
	pip-sync --quiet requirements/$(subst install-,,$@).txt


PHONY: tests-unit tests-integration tests
tests: tests-unit tests-integration

tests-unit: ## runs unit tests
	# running unit tests
	@pytest -vv \
		--exitfirst \
		--failed-first \
		--durations=10 \
		--pdb \
		$(CURDIR)/tests/unit

tests-integration: ## runs integration tests against local+production images
	# running integration tests local/(service):production images ...
	@export DOCKER_REGISTRY=local; \
	export DOCKER_IMAGE_TAG=production; \
	pytest -vv \
		--exitfirst \
		--failed-first \
		--durations=10 \
		--pdb \
		$(CURDIR)/tests/integration


# DEVELOPMENT ########
.env:
	cp .env-devel $@



.PHONY: up-extra down down-extra run-devel

up-extra: .env down ## starts pg stack fixture
	# resolving $@ under environ $<
	docker-compose -f docker-compose-extra.yml config
	# starting database stack as defined in  ...
	docker-compose -f docker-compose-extra.yml up --detach
	# discovering postgres services
	@export $(shell grep -v '^#' .env | xargs) && sc-pg discover
	@sc-pg info
	# upgrading postgres database to HEAD version
	@sc-pg upgrade


down down-extra: ## stops pg stack fixture
	# stopping extra services
	-@docker-compose -f docker-compose-extra.yml down


run-devel: .env up-extra  ## runs app with services defined in docker-compose-extra.yml
	# start app (within $<) in devel mode with adjacent services
	uvicorn $(APP_PACKAGE_NAME).__main__:the_app \
		--reload --reload-dir $(SRC_DIR) \
		--port=8000 --host=0.0.0.0


run-prod: .env up-extra
	# start app (within $<) in production mode with adjacent services
	$(APP_CLI_NAME)


# BUILD #####################

.PHONY: build build-nc build-devel build-devel-nc build-cache build-cache-nc
build build-nc build-devel build-devel-nc build-cache build-cache-nc: ## docker image build in many flavours
	# building ${APP_NAME} ...
	@$(MAKE_C) ${REPO_BASE_DIR} $@ target=${APP_NAME}


.PHONY: openapi-specs openapi.json
openapi-specs: openapi.json .env
openapi.json:
	# generating openapi specs file
	python3 -c "import json; from $(APP_PACKAGE_NAME).__main__ import *; print( json.dumps(the_app.openapi(), indent=2) )" > $@
