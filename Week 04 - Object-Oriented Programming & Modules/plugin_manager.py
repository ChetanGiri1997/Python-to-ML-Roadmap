
import importlib

_registry = {}

def load(name):
    mod = importlib.import_module(name)
    if not hasattr(mod, "run"):
        raise AttributeError(f"{name} has no run()")
    _registry[name] = mod

def list_plugins():
    return list(_registry.keys())

def execute(name):
    if name not in _registry:
        raise KeyError(f"Plugin '{name}' not registered")
    return _registry[name].run()
