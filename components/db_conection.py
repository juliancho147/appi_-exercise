__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engie = create_engine("mysql+pymysql://root:1234@db:3306/sys")
Session = sessionmaker(bind=engie)
DATABASE = declarative_base()



