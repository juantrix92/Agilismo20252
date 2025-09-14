from sqlalchemy.orm import Session
from .models import Receta, Ingrediente, RecetaIngrediente

class Recetario:
    def __init__(self, session: Session):
        self.session = session

    # HU001
    def agregarReceta(self, receta: Receta) -> int:
        self.session.add(receta)
        self.session.commit()
        return receta.id

    # HU005
    def verReceta(self, receta_id: int) -> Receta:
        return self.session.query(Receta).filter_by(id=receta_id).first()

    # HU004
    def listarRecetas(self):
        return [{"id": r.id, "nombre": r.nombre} for r in self.session.query(Receta).all()]

    # HU009
    def listarIngredientes(self, orden="id"):
        q = self.session.query(Ingrediente)
        if orden == "nombre":
            q = q.order_by(Ingrediente.nombre.asc())
        return [{"id": i.id, "nombre": i.nombre, "unidad": i.unidadMedida, "valor": i.valorUnidad} for i in q.all()]

    # HU011
    def prepararReceta(self, receta_id: int, personas: int):
        r = self.verReceta(receta_id)
        factor = personas / r.numeroPersonasBase
        detalles = []
        costo_total = 0.0
        for ri in r.ingredientesRel:
            cant = ri.cantidad * factor
            costo = cant * ri.costoUnitario
            costo_total += costo
            detalles.append({"ingrediente": ri.ingrediente.nombre, "cantidad": cant, "unidad": ri.unidad, "costo": costo})
        return {
            "receta": r.nombre,
            "personas": personas,
            "costoTotal": round(costo_total, 2),
            "caloriasTotales": r.caloriasPorPorcion * personas,
            "tiempoPreparacion": r.tiempoPreparacion,  # o regla de escalado si decides
            "ingredientes": detalles
        }
