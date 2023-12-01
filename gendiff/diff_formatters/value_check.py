def is_touched_value(value):
    if isinstance(value, dict):
        if value.get('status'):
            return True
    return False
