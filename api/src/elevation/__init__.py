import os
from dataclasses import dataclass
from pathlib import Path

from gpx2mesh.elevation.sources import IGetElevationFiles, NasaConnection, NasaProvider

from src.config import load_config_value


@dataclass
class NasaConfig:
    user: str
    pwd: str
    url: str
    assets_path: str


def build_elevation_files_provider() -> IGetElevationFiles:
    config = NasaConfig(
        user=load_config_value("NASA_USER"),
        pwd=load_config_value("NASA_PWD"),
        url=load_config_value("NASA_URL"),
        assets_path=load_config_value(
            "ELEVATION_ASSETS_PATH", default="assets/elevation"
        ),
    )
    connection = NasaConnection(url=config.url, user=config.user, pwd=config.pwd)

    assets = Path(config.assets_path)

    if not assets.exists():
        os.makedirs(assets)

    return NasaProvider(Path(config.assets_path), connection)
