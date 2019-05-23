from abc import ABC, abstractmethod
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Repository(Base):

    __tablename__ = 'repository'

    idrepository = Column(Integer, primary_key=True)
    path = Column(String)
    name = Column(String)
    owner = Column(String)
    country = Column(String)
    language = Column(String)
    stars = Column(Integer)
    size = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)
    forks_count = Column(Integer)
    watchers_count = Column(Integer)
    subscribers_count = Column(Integer)
    email = Column(String)
    features = relationship("Feature", cascade="all, delete-orphan")

    def __init__(self):
        self.path = ""
        self.name = ""
        self.owner = ""
        self.country = ""
        self.language = ""
        self.stars = 0
        self.size = 0
        self.created_at = ""
        self.updated_at = ""
        self.forks_count = 0
        self.watchers_count = 0
        self.subscribers_count = 0
        self.email = ""
        self.features = []

    def __str__(self):
        print("REPOSITORY:")
        print("\t path: " + self.path)
        print("\t name: " + self.name)
        print("\t owner: " + self.owner)
        if (self.country != None):
            print("\t country: " + self.country)
        else:
            print("\t country: None")
        if(self.language != None):
            print("\t language: " + self.language)
        else:
            print("\t language: None")
        print("\t stars: " + self.stars.__str__())

        for feature in self.features:
            print(feature)

        return ''

    def setRepository(self, path, name, owner, country, language, stars, features):
        self.path = path
        self.name = name
        self.owner = owner
        self.country = country
        self.language = language
        self.stars = stars
        self.features = features


class Feature(Base):

    __tablename__ = 'feature'

    idfeature = Column(Integer, primary_key=True)
    path = Column(String)
    name = Column(String)
    language = Column(String)
    #user_story = Column(String)
    repository_id = Column(Integer, ForeignKey('repository.idrepository'))
    scenarios = relationship("SimpleScenario", cascade="all, delete-orphan")

    def __init__(self):
        self.path = ""
        self.name = ""
        self.language = ""
        self.scenarios = []
        #self.user_story = ""
        #self.background = None

    def __str__(self):
        print("FEATURE:")
        print("\t path: " + self.path)
        print("\t name: " + self.name)
        print("\t language: " + self.language)

        for scenario in self.scenarios:
            print(scenario)

        return ''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Scenario(ABC):

    def __init__(self):
        steps = NotImplemented
        scenario_title = NotImplemented
        line = NotImplemented

        #@abstractmethod
        #def execute(self):
        #    pass

        #@abstractmethod
        #def set_line(self):
        #    pass


class SimpleScenario(Base):

    __tablename__ = 'scenario'

    idscenario = Column(Integer, primary_key=True)
    scenario_title = Column(String)
    line = Column(Integer)
    feature_id = Column(Integer, ForeignKey('feature.idfeature'))
    steps = relationship("Step", cascade="all, delete-orphan")

    def __init__(self):
        self.steps = []
        self.scenario_title = ""
        self.line = 0
        #self.executed_methods = []

    def execute(self):
        pass

    def set_line(self):
        pass

    def __str__(self):
        print("SCENARIO:")
        print("\t title: " + self.scenario_title)
        print("\t line: " + str(self.line))
        print("\t steps: ")

        for step in self.steps:
            print(step)

        #for method in self.executed_methods:
            #print(method)

        return ''


class ScenarioOutline(Scenario):

    def __init__(self):
        self.steps = []
        self.scenario_title = ""
        self.line = None
        self.examples = []
        self.scenario_iterations = []

    def execute(self):
        pass

    def set_line(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

class Step(Base):

    __tablename__ = 'step'

    idstep = Column(Integer, primary_key=True)
    step = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenario.idscenario'))

    def __init__(self):
        self.step = ""

    def __str__(self):
        print("\t\t" + self.step)

        return ''

#class Method:
#
#    def __init__(self):
#        self.method_name = ""
#        self.class_name = ""
#        self.class_path = ""
#
#    def __str__(self):
#        print("METHOD:")
#        print("\t name: " + self.method_name)
#        print("\t class: " + self.class_name)
#        print("\t path: " + self.class_path)
#        return ''
