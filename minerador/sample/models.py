from abc import ABC, abstractmethod


class Feature:

    def __init__(self):
        self.path_name = ""
        self.feature_name = ""
        self.scenarios = []
        self.language = ""
        self.user_story = ""
        self.background = None

    def __str__(self):
        print("FEATURE:")
        print("\t path: " + self.path_name)
        print("\t name: " + self.feature_name)
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

        @abstractmethod
        def execute(self):
            pass

        @abstractmethod
        def set_line(self):
            pass


class SimpleScenario(Scenario):

    def __init__(self):
        self.steps = []
        self.scenario_title = ""
        self.line = None
        self.executed_methods = []

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
            print("\t\t" + step)

        for method in self.executed_methods:
            print(method)

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


class Method:

    def __init__(self):
        self.method_name = ""
        self.class_name = ""
        self.class_path = ""

    def __str__(self):
        print("METHOD:")
        print("\t name: " + self.method_name)
        print("\t class: " + self.class_name)
        print("\t path: " + self.class_path)
        return ''


class Repository:

    def __init__(self):
        self.path = ""
        self.name = ""
        self.owner = ""
        self.country = ""
        self.language = ""
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

        for feature in self.features:
            print(feature)

        return ''

    def setRepository(self, path, name, owner, country, language, features):
        self.path = path
        self.name = name
        self.owner = owner
        self.country = country
        self.language = language
        self.features = features

