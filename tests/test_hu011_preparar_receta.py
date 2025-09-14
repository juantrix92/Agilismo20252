from factories.ingrediente_factory import build_ingrediente
from factories.receta_factory import build_receta_completa
from app.domain.services import Recetario

def test_preparar_receta_calcula_costos_y_calorias(session, faker):
    svc = Recetario(session)
    ing = [build_ingrediente(faker) for _ in range(2)]
    session.add_all(ing); session.flush()
    base = 4
    r = build_receta_completa(faker, ing)
    r.numeroPersonasBase = base
    receta_id = svc.agregarReceta(r)

    resultado = svc.prepararReceta(receta_id=receta_id, personas=8)
    assert resultado["personas"] == 8
    assert resultado["costoTotal"] > 0
    assert resultado["caloriasTotales"] == r.caloriasPorPorcion * 8
    for det in resultado["ingredientes"]:
        assert det["cantidad"] > 0
