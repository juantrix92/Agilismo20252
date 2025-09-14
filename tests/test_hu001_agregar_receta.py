import pytest
from app.domain.services import Recetario
from factories.ingrediente_factory import build_ingrediente
from factories.receta_factory import build_receta_completa
from app.domain.services import Recetario

def test_agregar_receta_con_ingredientes(session, faker):
    # Arrange
    svc = Recetario(session)
    ingredientes = [build_ingrediente(faker) for _ in range(3)]
    for i in ingredientes: session.add(i)
    session.commit()
    receta = build_receta_completa(faker, ingredientes)

    # Act
    receta_id = svc.agregarReceta(receta)

    # Assert
    guardada = svc.verReceta(receta_id)
    assert guardada.id == receta_id
    assert len(guardada.ingredientesRel) == len(ingredientes)
