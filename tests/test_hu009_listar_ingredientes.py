def test_listar_ingredientes_alfabetico(session, faker):
    svc = Recetario(session)
    ings = [build_ingrediente(faker) for _ in range(10)]
    session.add_all(ings); session.commit()
    lista = svc.listarIngredientes(orden="nombre")
    assert [*lista] == sorted(lista, key=lambda d: d["nombre"])
