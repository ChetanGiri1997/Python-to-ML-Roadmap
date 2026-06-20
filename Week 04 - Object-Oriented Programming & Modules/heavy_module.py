
_heavy = None

def get_heavy():
    global _heavy
    if _heavy is None:
        import time
        time.sleep(0.5)          # simulate slow import (e.g. numpy, tensorflow)
        _heavy = {"loaded": True}
    return _heavy

def cheap_func():
    return "no heavy import needed"
