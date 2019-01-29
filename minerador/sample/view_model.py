from models import Feature, SimpleScenario, Repository, Step
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
import os
import requests
from subprocess import PIPE, Popen


class ViewModel():

    def __init__(self, token):
        self.token = token
        self.features = []
        self.num_files = 0
        self.num_func = 0
        try:
            self.engine = create_engine('mysql://root:1234@localhost/foo', echo=False)
            Session = sessionmaker(bind=self.engine)
            session = Session()
            session.query("1").from_statement("SELECT 1").all()
            session.close()
            print("Connected to Data Base")
        except:
            print("Not connected do Data base")


    # Funcao retorna o json da pagina
    def get_json(self, url):
        resp = os.popen("curl -H 'Authorization: token " + self.token + "' " + url).read()
        return json.loads(resp)

    def get_json_requests(self, url):
        resp = requests.get(url, headers={'Authorization': 'token {}'.format(self.token)})
        return resp.json()

    # Function get url in items of the json
    def get_repo_paths(self, query_url):
        paths_urls = []

        data = self.get_json(query_url)

        for paths in data['items']:
            paths_urls.append(paths['url'])

        return paths_urls

    # Funcao que retorna uma lista com as urls de todos os repo do usuario
    def get_repo(self, url):
        repo_urls = []

        data = self.get_json(url)

        for repo in data:
            repo_urls.append(repo['url'] + '/contents')

        return repo_urls


    # Funcao que procura a extensao e retorna para os casos que a extensao seja a correta ou nao
    def find_ext(self, string1, ext):
        lis_string = string1.split('.')
        tam = len(lis_string)

        if tam >= 2:
            if lis_string[tam - 1] == ext:
                return 1
            else:
                return 0
        else:
            return 0

    # Funcao que faz o download dos arquivos em dirs e subdirs com uma extensao especifica
    def download_files(self, url, dirname, extensao):

        dir_urls = []

        data = self.get_json_requests(url)

        for raw in data:

            print("Checking " + raw['name'])

            if self.find_ext(raw['name'], extensao):

                # f.write(os.popen("curl -H 'Authorization: token " + self.token + "' "
                #                     + raw['download_url']).read())
                print("Downloading " + raw['name'])
                resp = requests.get(raw['download_url'], allow_redirects=True, headers={'Authorization': 'token {}'.format(self.token)})

                open("dados/" + dirname + "/" + raw['name'], 'wb').write(resp.content)

            if raw['type'] == "dir":
                dir_urls.append(raw['url'])

        if dir_urls != []:
            for dr in dir_urls:
                self.download_files(dr, dirname, extensao)

    # gets an object repository using its url as parameter
    def getRepositoryFromPath(self, path):
        repositoryJson = self.get_json_requests(path)
        ownerJson = self.get_json_requests(repositoryJson['owner']['url'])
        repository = Repository()
        repository.path = repositoryJson['url']
        repository.name = repositoryJson['name']
        repository.owner = repositoryJson['owner']['login']
        repository.country = ownerJson['location']
        repository.language = repositoryJson['language']
        repository.stars = repositoryJson['stargazers_count']

        dirname = repository.owner + "_" + repository.name

        os.mkdir("dados/" + dirname)

        # now getting the projects features and saving in dirs

        self.download_files(repository.path + '/contents', dirname, "feature")
        # features = os.listdir(os.getcwd() + os.sep + "dados")

        # repository.features = []

        # for feature in features:
        #     repository.features.append(self.get_feature_information(os.getcwd() + os.sep + "dados" + os.sep + feature))
        #     os.remove(os.getcwd() + os.sep + "dados" + os.sep + feature)

        return repository

    def saveRepositoryOnDB(self, repository):

        # create a new session
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # generate database schema
        declarative_base().metadata.create_all(self.engine)

        # persisting data
        session.add(repository)

        # commit and close session
        session.commit()
        session.close()

    #========================================================

    def list_all_features(self, initial_path):
        """
        This method show all BDD features into a specific project, with the scenarios and steps.
        :param initial_path: The base path of this project.
        :return: print all features.
        """

        print('------------------------')
        self.load_infos(initial_path)
        print('Numero de arquivos analisados: ', self.num_files)
        print('Numero de features analisadas:', len(self.features))
        print('------------------------')
        with open('result.json', 'w+') as file:
            json_string = json.dumps(self.features, default=Feature.obj_dict)
            file.write(json_string)

    def get_all_features(self, url):
        """
        This method get all features, scenarios and steps
        :param url: base path of the project.
        :return: a list of Features
        """
        self.load_infos(url)
        return self.features

    def load_infos(self, url):
        """
        This method will instantiate all features with their scenarios
        :param url: base path of the project.
        :return: all features with their scenarios.
        """
        for root, dirs, files in os.walk(url):
            for file in files:
                if file.endswith(".feature"):
                    self.num_files += 1
                    feature = self.get_feature_information(os.path.join(root, file))
                    self.features.append(feature)

    def get_feature_information(self, path):
        """Get all information in a .feature file.
        :param path: the path of the .feature file.
        :return: feature information instantiated.
        """
        feature = Feature()
        feature.language = self.get_language(path)
        feature.path = path
        feature.name = self.get_feature_name(path)
        feature.scenarios = self.get_scenarios(path)
        # feature = self.get_steps(path, feature)
        return feature

    def get_feature_name(self, path):
        """This method get the feature name.
        :param path: the path to this feature file.
        :return: the name of the feature.
        """
        feature_name = ''
        with open(path) as file:
            file.seek(0)
            for line_number, line in enumerate(file, 1):
                if "Feature: " in line:
                    feature_name = line.split("Feature: ", 1)[1].replace('\n', '')
        return feature_name

    def get_steps(self, lines, initial, final):
        """
        This method get all steps into a specific scenario.
        :param lines: Content of the file.
        :param initial: The line of the beginning of this scenario
        :param final: The last line of this scenario.
        :return: a list of Steps.
        """
        key_words = ["When ", "And ", "Given ", "Then "]
        steps = []
        index = initial
        if final is not None:
            while index <= final:
                if any(word in lines[index - 1] for word in key_words):
                    step = Step()
                    step.step = lines[index - 1].replace('\n', '').replace('  ', '')
                    steps.append(step)
                index += 1
        else:
            while index <= len(lines):
                if any(word in lines[index - 1] for word in key_words):
                    step = Step()
                    step.step = lines[index - 1].replace('\n', '').replace('  ', '')
                    steps.append(step)
                index += 1
        return steps

    def read_scenario(self, path, initial_line, final_line):
        """
        This method read a specific scenario.
        :param path: Path of the file containing the scenario.
        :param initial_line: The line of the beginning of this scenario
        :param final_line: Last line of this scenario.
        :return: A scenario instantiated.
        """
        scenario = SimpleScenario()
        with open(path) as file:
            file.seek(0)
            lines = file.readlines()
            scenario.scenario_title = lines[initial_line - 1].split("Scenario: ", 1)[1].replace('\n', '').replace(':',
                                                                                                                 '')
            scenario.line = initial_line
            scenario.steps = self.get_steps(lines, initial_line + 1, final_line)
        return scenario

    def get_scenarios(self, path):
        """This method get all scenarios of a feature.
        :param path: the path to the feature file.
        :return: all scenarios instantiated.
        """
        scenarios = []
        lines_scenarios = self.get_all_scenarios_lines(path)
        count = len(lines_scenarios)

        for index in range(count):
            scenario = SimpleScenario()
            if index + 1 >= count:
                scenario = self.read_scenario(path, lines_scenarios[index], None)
            else:
                scenario = self.read_scenario(path, lines_scenarios[index], lines_scenarios[index + 1] - 1)

            scenarios.append(scenario)
        return scenarios

    def get_language(self, path):
        """Get the language of the .feature file.
        :param path: the path to the .feature file.
        :return: language.
        """
        language = ''
        with open(path) as file:
            file.seek(0)
            for line_number, line in enumerate(file, 1):
                if "#language:" in line:
                    language = line.split("#language:", 1)[1].replace('\n', '')
        return language

    def get_all_scenarios_lines(self, path):
        """
        This method get the lines of each scenario into a specific file.
        :param path: The path of this file.
        :return: The lines.
        """
        lines = []
        with open(path) as file:
            file.seek(0)
            for line_number, line in enumerate(file, 1):
                if "Scenario:" in line:
                    lines.append(line_number)


        return lines
