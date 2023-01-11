# Poetry

```
# Init project
poetry init
```

```
# Add package & Create env if none was initialized
poetry add requests

# And dev only
poetry add --group dev black 
```

```
configure access to pypi
poetry config pypi-token.pypi TOKEN
```

```
# Publishing to pypi
# Version defined in pyproject.toml
poetry publish --build
```