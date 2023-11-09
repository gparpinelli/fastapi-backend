import os
import sys
import pytest
from fastapi.testclient import TestClient
from typer.testing import CliRunner

from fastapi_backend import app, settings, db  # noqa
from fastapi_backend.cli import cli  # noqa


# each test runs on cwd to its temp dir
@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    # Get the fixture dynamically by its name.
    tmpdir = request.getfixturevalue("tmpdir")
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    with tmpdir.as_cwd():
        yield


@pytest.fixture(scope="function", name="app")
def _app():
    return app


@pytest.fixture(scope="function", name="cli")
def _cli():
    return cli


@pytest.fixture(scope="function", name="settings")
def _settings():
    return settings


@pytest.fixture(scope="function")
def api_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def cli_client():
    return CliRunner()


def remove_db():
    # Remove the database file
    try:
        os.remove("testing.db")
    except FileNotFoundError:
        pass


@pytest.fixture(scope="session", autouse=True)
def initialize_db(request):
    db.create_db_and_tables(db.engine)
    request.addfinalizer(remove_db)
