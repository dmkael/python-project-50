from .unique_keygen import UNIQUE_KEY


def is_touched_value(value):
    if isinstance(value, dict):
        if value.get(UNIQUE_KEY):
            return True
    return False
