def is_touched_key(key):
    mod_keys = ['=eql#', '+add#', '-rem#', '-mod#', '+mod#']
    return any(key.startswith(x) for x in mod_keys)
