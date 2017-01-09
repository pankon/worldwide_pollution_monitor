#!/usr/bin/env python2

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float
from get_user_info import get_ip

Base = declarative_base()

class Point(Base):
    __tablename__ = '_'.join(
        ['point',get_ip().replace('.','_')]
    )
    id = Column(String, primary_key=True)
    Location = Column(String)
    TypeOfSensor = Column(String)
    SensorId = Column(String)
    TestType = Column(String)
    SensorOwner = Column(String)
    SensorValue = Column(Float)
    ReportedTriggerValue = Column(Float)
    ReportedThresholdValue = Column(Float)
    ReportedNormalValue = Column(Float)
    SensorUnits = Column(String)

class Region(Base):
    __tablename__ = '_'.join(
        ['region',get_ip().replace('.','_')]
    )
    id = Column(String, primary_key=True)
    Location = Column(String)
    TypeOfSensor = Column(String)
    TestType = Column(String)
    SensorOwner = Column(String)
    SensorValue = Column(Float)
    LastTenValues = Column(String)

class Country(Base):
    __tablename__ = '_'.join(
        ['country',get_ip().replace('.','_')]
    )
    id = Column(String, primary_key=True)

class World(Base):
    __tablename__ = '_'.join(
        ['world',get_ip().replace('.','_')]
    )
    id = Column(String, primary_key=True)

class CreateDatabase(object):
    # run a bash file that downloads postgresql and sets up
    # localhost accordingly
    pass


def main():
#     engine = create_engine('postgresql+psycopg2://localhost')
#     create_database = CreateDatabase()
#     Point.create(engine) # I think this works

    pass

if __name__ == "__main__":
    main()
