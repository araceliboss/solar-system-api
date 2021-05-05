import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    planet_foozie = Planet(name="Foozie", description="The fuzziest planet")
    planet_the_bomb = Planet(name="The Bomb", description="Explosive")

    db.session.add_all([planet_foozie, planet_the_bomb])
    db.session.commit()
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    