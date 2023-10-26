# PIP


## Activate env

```bash
python3 -m venv my_env
source my_env/bin/activate
```

## Installing from various sources

```bash
pip install requests
```

```bash
pip install requests-2.22.0-py2.py3-none-any.whl
```

```bash
# need to include setup.py
pip install git+https://github.com/psf/requests.git
```

```bash
# need to include setup.py
pip install /home/user/src/requests
```

```bash
pip install requests==2.22.0
```

```bash
pip freeze > requirements.txt
```

```bash
pip install -r requirements.txt
```

```bash
pip list
```

```bash
deactivate
```
