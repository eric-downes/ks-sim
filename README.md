# ks-sim
Q: Can Kuramoto-Sivashinsky dendrites dissipate?
See [here](https://twitter.com/johncarlosbaez/status/1450461569414991882) for context.

## Setup on macOS/linux
- Install [python3](https://www.python.org/downloads/) and check that it worked: 
  - `which python` should return a path
  - `python --version` should have a "3." in it; I'm using 3.10.4
- Install [py-pde](https://py-pde.readthedocs.io/en/latest/getting_started.html) package:
```python -m pip install --upgrade py-pde```
- ...
- Profit.

## Runtime

Right now just plots an (x,t)-plot and if in a py shell, returns a MemoryStorage object

### Commandline, from the root of this repository
`python ks.py`

### From jupyter/IPython
`%run -i ks.py`
