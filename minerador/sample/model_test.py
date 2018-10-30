from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Repository_test(Base):

    __tablename__ = 'repository'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    name = Column(String)
    owner = Column(String)
    country = Column(String)
    language = Column(String)
    features = relationship("Feature", cascade="all, delete-orphan")

    def __init__(self, path, name, owner, country, language):
        self.path = path
        self.name = name
        self.owner = owner
        self.country = country
        self.language = language


class Feature(Base):

    __tablename__ = 'feature'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    name = Column(String)
    language = Column(String)
    user_story = Column(String)
    repository_id = Column(Integer, ForeignKey('repository.id'))

