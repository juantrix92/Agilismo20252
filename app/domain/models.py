from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.infra.db import Base

class Ingrediente(Base):
    __tablename__ = "ingredientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    valorUnidad = Column(Float, nullable=False)
    unidadMedida = Column(String, nullable=False)
    sitioProveedor = Column(String, nullable=True)

class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    tiempoPreparacion = Column(Float, nullable=False)
    numeroPersonasBase = Column(Integer, nullable=False)
    caloriasPorPorcion = Column(Integer, nullable=False)
    instrucciones = Column(String, nullable=True)
    ingredientesRel = relationship("RecetaIngrediente", cascade="all, delete-orphan", back_populates="receta")

class RecetaIngrediente(Base):
    __tablename__ = "receta_ingrediente"
    id = Column(Integer, primary_key=True)
    receta_id = Column(Integer, ForeignKey("recetas.id"))
    ingrediente_id = Column(Integer, ForeignKey("ingredientes.id"))
    cantidad = Column(Float, nullable=False)
    unidad = Column(String, nullable=False)
    costoUnitario = Column(Float, nullable=False)
    receta = relationship("Receta", back_populates="ingredientesRel")
    ingrediente = relationship("Ingrediente")
