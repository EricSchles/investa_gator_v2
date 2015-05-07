import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,Float
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

class Ads(Base):
    __tablename__ = 'ads'
    id = Column(Integer,primary_key=True)
    number = Column(String(100),nullable=False)
    title = Column(String(400),nullable=False)
    text_body = Column(String(10000),nullable=True)
    link = Column(String(10000),nullable=False)
    scraped_at = Column(String(10000),nullable=False)
    flagged_for_child_trafficking = Column(Boolean(False),nullable=False)
    flagged_for_trafficking = Column(Boolean(False),nullable=False)
    language = Column(String(1000),nullable=False)
    polarity = Column(Float(0),nullable=False)
    translated_body=Column(String(10000),nullable=True)
    translated_title=Column(String(10000),nullable=False)
    subjectivity=Column(Float(0),nullable=False)
    network=Column(String(10000),nullable=False)

    
if __name__ == '__main__':
    
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///database.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
