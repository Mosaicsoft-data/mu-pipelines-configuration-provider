# mu_pipelines_configuration_provider

## Features


## Tools

### (Lint)
```
pipenv run flake8
pipenv run mypy
pipenv run black .
pipenv run isort .

```

### (Unit Tests)
```
pipenv run pytest --cov --cov-fail-under=80
```

### Pre-Commit Hooks

#### Install the hook
```
pipenv run pre-commit install
```