import os


class MissingConfigKeyError(Exception):
    def __init__(self, missing_key):
        self.missing_key = missing_key


def load_config_value(key: str) -> str | None:
    file = os.getenv(key + "_FILE")
    if file is None:
        return _load_from_env(key)

    try:
        with open(file, "rt") as file:
            return file.read()
    except FileNotFoundError:
        raise MissingConfigKeyError(key)


def _load_from_env(key):
    value = os.getenv(key)
    if value is None:
        raise MissingConfigKeyError(key)
    return value
