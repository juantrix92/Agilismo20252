from app.domain.models import Receta, RecetaIngrediente
def build_receta_completa(faker, ingredientes):
    r = Receta(
        nombre=faker.unique.sentence(nb_words=3),
        tiempoPreparacion=faker.pyfloat(min_value=1, max_value=120, right_digits=1),
        numeroPersonasBase=faker.random_int(min=1, max=8),
        caloriasPorPorcion=faker.random_int(min=50, max=1200),
        instrucciones=faker.paragraph(nb_sentences=3)
    )
    r.ingredientesRel = [
        RecetaIngrediente(ingrediente=i, cantidad=faker.pyfloat(min_value=1, max_value=500, right_digits=2), unidad=i.unidadMedida, costoUnitario=i.valorUnidad)
        for i in ingredientes
    ]
    return r
