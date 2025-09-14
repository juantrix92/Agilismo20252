from app.domain.models import Ingrediente
def build_ingrediente(faker):
    return Ingrediente(
        nombre=faker.unique.word().title(),
        valorUnidad=faker.pyfloat(min_value=0.1, max_value=50, right_digits=2),
        unidadMedida=faker.random_element(elements=("g","kg","ml","lt","unid")),
        sitioProveedor=faker.company()
    )
