# Poetry

```bash
# Init project
poetry init
```

```bash
# Add package & Create env if none was initialized
poetry add requests

# And dev only
poetry add --group dev black
```

```bash
configure access to pypi
poetry config pypi-token.pypi TOKEN
```

```bash
# Publishing to pypi
# Version defined in pyproject.toml
poetry publish --build
```
