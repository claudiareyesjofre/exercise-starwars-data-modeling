import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    username = Column(String(50),nullable=False)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50),nullable=False)
    email = Column(String(300),nullable=False)
    fono = Column(String(15),nullable=False)
    password = Column(String(10),nullable=False)
    fecha_de_ingreso = Column(String(200),nullable=False)

class Personaje(Base):
    __tablename__ = "personaje"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(200),nullable=False)
    Detalle = Column(String(200),nullable=False)

class Planeta(Base):
    __tablename__ = "planeta"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(200),nullable=False)
    Detalle = Column(String(200),nullable=False)

class PersonajeFavorito(Base):
    __tablename__ = "personajeFavorito"
    id = Column(Integer,primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    personaje_id = Column (Integer, ForeignKey('personaje.id'))

class PlanetaFavorito(Base):
    __tablename__ = "planetafavorito"
    id = Column(Integer,primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    planeta_id = Column (Integer, ForeignKey('planeta.id'))

""" 
class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) """

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
