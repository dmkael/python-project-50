VALID_STATUSES = ['nested', 'added', 'removed', 'same', 'modified']


def is_valid_status(status):
    return any(status == valid_status for valid_status in VALID_STATUSES)
