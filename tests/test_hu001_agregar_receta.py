def test_placeholder_hu001_verde():
    from app.domain.services import Recetario
    assert Recetario().ping() is True
