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

    def __repr__(self):
        return "<Repository(path='$s', name='%s', owner='%s', country='%s', language='%s')>" % (
                            self.path, self.name, self.owner, self.country, self.language)

class Feature(Base):

    __tablename__ = 'feature'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    name = Column(String)
    language = Column(String)
    user_story = Column(String)
    repository_id = Column(Integer, ForeignKey('repository.id'))


# create an engine
engine = create_engine('mysql://root:1234@localhost/sqlalchemy', echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
