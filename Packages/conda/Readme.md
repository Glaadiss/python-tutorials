# Conda

## Starting env

```bash
conda create --name py310 python=3.10
```

```bash
conda install requests
```

```bash
conda list
```

```bash
conda list --explicit > py310.txt
```

```bash
conda list --revisions
```

```bash
conda env remove --name py310
```

```bash
conda env create --file py310.txt
```

```bash
pipenv graph
```
