import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class KeyWords(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String(500), nullable=False)
 
class TrainData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    text = Column(String(10000),nullable=False)

class PhoneNumbers(Base):
    __tablename__ = 'phone_numbers'
    id = Column(Integer,primary_key=True)
    number = Column(String(100),nullable=False)
    
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///database.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
