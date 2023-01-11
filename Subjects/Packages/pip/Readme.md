# PIP


## Activate env

```
python3 -m venv my_env
source my_env/bin/activate
```

## Installing from various sources

```
pip install requests
```

```
pip install requests-2.22.0-py2.py3-none-any.whl
```

```
# need to include setup.py
pip install git+https://github.com/psf/requests.git
```

```
# need to include setup.py
pip install /home/user/src/requests
```

```
pip install requests==2.22.0
```

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```

```
pip list
```

```
deactivate
```