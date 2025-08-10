import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from src.elevation import build_elevation_files_provider


def test_mkdir_assets_folder_if_does_not_exist(monkeypatch):
    with mock.patch.dict(os.environ, clear=True), TemporaryDirectory() as tmp_dir:
        monkeypatch.setenv("NASA_USER", "user")
        monkeypatch.setenv("NASA_PWD", "pwd")
        monkeypatch.setenv("NASA_URL", "url")
        assets = Path(tmp_dir) / "assets" / "elevation"
        monkeypatch.setenv("ELEVATION_ASSETS_PATH", str(assets))

        assert not assets.exists()

        build_elevation_files_provider()

        assert assets.exists()
