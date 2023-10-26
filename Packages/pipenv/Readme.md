# Pipenv

```bash
# Installing pipenv
pip install --user pipx
pipx install pipenv
```

```bash
# Init + install packages from requirements.txt
pipenv --python 3.10
```

```bash
# Activate shell (venv)
pipenv shell

# Or use without activating (based on current repo)
pipenv run python ...
```

```bash
# install package (it will be added in Pipfile)
pipenv install requests

# ...and with dev flag
pipenv install --dev black
```

```bash
# listing packages and deps
pipenv graph

# and in reverse order (e.g to resolve conflicts)
pipenv graph --revers
```

```bash
# Updating packges
pipenv update
```

```bash
# Check security vulnerabilities
pipenv check
```
