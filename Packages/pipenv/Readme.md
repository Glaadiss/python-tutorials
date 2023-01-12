# Pipenv

```
# Installing pipenv
pip install --user pipx
pipx install pipenv
```


# Init + install packages from requirements.txt
pipenv --python 3.10
```

```
# Activate shell (venv)
pipenv shell

# Or use without activating (based on current repo)
pipenv run python ...
```

```
# install package (it will be added in Pipfile)
pipenv install requests

# ...and with dev flag
pipenv install --dev black
```

```
# listing packages and deps
pipenv graph

# and in reverse order (e.g to resolve conflicts)
pipenv graph --revers
```

```
# Updating packges
pipenv update
```

```
# Check security vulnerabilities
pipenv check
```
