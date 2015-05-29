import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#To Do: move this to db_helpers

class CRUD:
    def __init__(self,db,model_obj=None,table=None):
        self.table = table
        self.db = db
        engine = create_engine(db)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.model_obj = model_obj

    def update_model_obj(self,model_obj):
        self.model_obj = model_obj
        
    def update_table(self,table):
        self.table = table
        
    def update_db(self,db):
        self.db = db
        engine = create_engine(db)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self,obj):
        self.session.add(obj)
        self.session.commit()

    def get_all(self):
        q = self.session.query(self.model_obj)
        return q.all()

class PhoneNumbers(Base):
    __tablename__ = 'phone_numbers'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(500), nullable=False)
    
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
    phone_numbers = Column(String(10000),nullable=True)
    title = Column(String(400),nullable=False)
    text_body = Column(String(10000),nullable=True)
    link = Column(String(10000),nullable=False)
    scraped_at = Column(String(10000),nullable=False)
    photos = Column(String(10000),nullable=True) # ToDo, look up how to do this correctly.
    language = Column(String(1000),nullable=False)
    polarity = Column(Float(0),nullable=False)
    translated_body=Column(String(10000),nullable=True)
    translated_title=Column(String(10000),nullable=False)
    subjectivity=Column(Float(0),nullable=False)
    posted_at = Column(String(10000),nullable=True) #ToDo, look up how to do this correctly - make use of DateTime
    
    
if __name__ == '__main__':
    
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///database.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
