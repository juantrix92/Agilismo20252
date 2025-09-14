from sqlalchemy.orm import Session
from app.domain.models import Receta, Ingrediente, RecetaIngrediente

class Recetario:
    def __init__(self, session: Session):
        self.session = session

    # HU001 - Agregar receta
    def agregarReceta(self, receta: Receta) -> int:
        self.session.add(receta)
        self.session.commit()
        return receta.id

    # HU005 - Ver receta
    def verReceta(self, receta_id: int) -> Receta:
        return self.session.query(Receta).filter_by(id=receta_id).first()

    # HU004 - Listar recetas
    def listarRecetas(self):
        q = self.session.query(Receta).order_by(Receta.nombre.asc())
        return [{"id": r.id, "nombre": r.nombre} for r in q.all()]

    # HU009 - Listar ingredientes
    def listarIngredientes(self, orden: str = "id"):
        q = self.session.query(Ingrediente)
        if orden == "nombre":
            q = q.order_by(Ingrediente.nombre.asc())
        elif orden == "valor":
            q = q.order_by(Ingrediente.valorUnidad.asc())
        else:
            q = q.order_by(Ingrediente.id.asc())
        return [
            {"id": i.id, "nombre": i.nombre, "unidad": i.unidadMedida, "valor": i.valorUnidad}
            for i in q.all()
        ]

    # HU011 - Preparar receta para N personas
    def prepararReceta(self, receta_id: int, personas: int):
        r = self.verReceta(receta_id)
        if r is None:
            raise ValueError("Receta no encontrada")
        if personas <= 0:
            raise ValueError("El número de personas debe ser > 0")

        factor = personas / r.numeroPersonasBase
        detalles = []
        costo_total = 0.0

        for ri in r.ingredientesRel:
            cant = ri.cantidad * factor
            costo = cant * ri.costoUnitario
            costo_total += costo
            detalles.append(
                {
                    "ingrediente": ri.ingrediente.nombre,
                    "cantidad": cant,
                    "unidad": ri.unidad,
                    "costo": costo,
                }
            )

        return {
            "receta": r.nombre,
            "personas": personas,
            "costoTotal": round(costo_total, 2),
            "caloriasTotales": r.caloriasPorPorcion * personas,
            "tiempoPreparacion": r.tiempoPreparacion,  # regla simple
            "ingredientes": detalles,
        }
