from models import Dog , Base
from sqlalchemy import (create_engine,Column,Integer, String) 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from testing.conftest import SQLITE_URL

engine = create_engine(SQLITE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()

class Dog (Base):
    __tablename__="dogs"
    id = Column(Integer(),  primary_key=True)
    name = Column(String())
    breed = Column(String()) 

def create_table(Base, engine):
    if __name__== '__main__':

     Base.metadata.create_all(engine)
    

def save(session, dog):
    session.add(dog)
    session.commit()
    return session.query(Dog).first().name

def get_all(session):
    all_dogs = []
    all_dogs = session.query(Dog).all()
    return all_dogs

def find_by_name(session, name):
    return session.query (Dog).filter (Dog.name==name).first()

def find_by_id(session, id):
    return session.query (Dog).filter (Dog.id==id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query (Dog).filter (Dog.name==name and Dog.breed ==breed).first()
    

def update_breed(session, dog, breed):
    dog.breed=breed
    session.query(Dog).update({Dog.breed : breed})
    session.commit()