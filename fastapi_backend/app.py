from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config import settings
from .db import create_db_and_tables, engine
from .routes import main_router

def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("fastapi_backend", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with Path(__file__).parent.joinpath(*paths).open(
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


description = """
fastapi_backend API helps you do awesome stuff. 🚀
"""

app = FastAPI(
    title="fastapi_backend",
    description=description,
    version=read("VERSION"),
)

if settings.server and settings.server.get("cors_origins", None):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.server.cors_origins,
        allow_credentials=settings.get("server.cors_allow_credentials", True),
        allow_methods=settings.get("server.cors_allow_methods", ["*"]),
        allow_headers=settings.get("server.cors_allow_headers", ["*"]),
    )

app.include_router(main_router, prefix="/api", tags=["api"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)
