import os
from tempfile import NamedTemporaryFile
from unittest import mock

import pytest

from src.config import MissingConfigKeyError, load_config_value


def test_load_from_env(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        monkeypatch.setenv("MY_KEY", "value")

        assert load_config_value("MY_KEY") == "value"


def test_load_from_env_missing(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        monkeypatch.delenv("MY_KEY", raising=False)

        with pytest.raises(MissingConfigKeyError) as exc_info:
            load_config_value("MY_KEY")

        assert exc_info.value.missing_key == "MY_KEY"


def test_load_from_file(monkeypatch):
    with (
        mock.patch.dict(os.environ, clear=True),
        NamedTemporaryFile("+ta", delete_on_close=False) as file,
    ):
        print(file.name)
        monkeypatch.setenv("MY_KEY_FILE", file.name)
        file.write("toto")
        file.close()

        assert load_config_value("MY_KEY") == "toto"

def test_load_from_file_missing_file(monkeypatch):
     with mock.patch.dict(os.environ, clear=True):
        monkeypatch.setenv("MY_KEY_FILE", "toto")

        with pytest.raises(MissingConfigKeyError) as exc_info:
            load_config_value("MY_KEY")

        assert exc_info.value.missing_key == "MY_KEY"