from factories.ingrediente_factory import build_ingrediente
from factories.receta_factory import build_receta_completa
from app.domain.services import Recetario

def test_listar_recetas_devuelve_nombres_y_id(session, faker):
    svc = Recetario(session)
    # seed
    for _ in range(5):
        ing = [build_ingrediente(faker) for _ in range(2)]
        session.add_all(ing); session.flush()
        r = build_receta_completa(faker, ing)
        svc.agregarReceta(r)
    lista = svc.listarRecetas()
    assert len(lista) >= 5
    assert {"id","nombre"} <= set(lista[0].keys())
