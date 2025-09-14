import pytest
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infra.db import Base
from app.domain import models

@pytest.fixture(scope="session")
def faker():
    return Faker("es_CO")

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    TestingSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    s = TestingSession()
    yield s
    s.close()
