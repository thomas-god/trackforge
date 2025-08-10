import os
from tempfile import NamedTemporaryFile

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from gpx2mesh import build_mesh

from src.elevation import build_elevation_files_provider

app = FastAPI()

prod = os.getenv("ENV", default="local").lower() == "production"

if not prod:
    load_dotenv()


origins = ["https://trackforge.fr"] if prod else ["http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/track")
async def root(request: Request):
    with NamedTemporaryFile("b+a", delete=False) as file:
        file.write(await request.body())
        file.close()

        elevation_file_provider = build_elevation_files_provider()
        mesh = build_mesh(file.name, elevation_file_provider)

    with NamedTemporaryFile("+ba", suffix=".stl", delete=False) as file:
        mesh.export(file.name)
        file.close()
        return FileResponse(file.name)
