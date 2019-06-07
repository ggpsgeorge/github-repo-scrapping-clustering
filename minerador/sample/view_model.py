from models import Feature, SimpleScenario, Repository, Step
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
import sqlalchemy
import sqlalchemy as db
import pandas as pd
import json
import os
import subprocess
import requests
#fda78d73c67855294814abfa3a09f301b3843e87
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
        resp = subprocess.Popen("curl -H 'Authorization: token " + self.token + "' " + url, stdout=subprocess.PIPE).communicate()[0].decode('u8')
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
        repository.size = repositoryJson['size']
        repository.created_at = repositoryJson['created_at']
        repository.updated_at = repositoryJson['updated_at']
        repository.forks_count = repositoryJson['forks_count']
        repository.watchers_count = repositoryJson['watchers_count']
        repository.subscribers_count = repositoryJson['subscribers_count']
        repository.email = ownerJson['email']

        dirname = repository.owner + "_" + repository.name

        os.mkdir("dados/" + dirname)

        # now getting the projects features and saving in dirs

        self.download_files(repository.path + '/contents', dirname, "feature")

        # now reading the feature file and saving as an object in the repository object

        features = os.listdir(os.getcwd() + os.sep + "dados" + os.sep + dirname)
        repository.features = []

        for feature in features:
            repository.features.append(self.get_feature_information(os.getcwd() + os.sep + "dados" + os.sep + dirname + os.sep + feature))

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
        try:
            session.commit()
        except (sqlalchemy.exc.SQLAlchemyError, sqlalchemy.exc.DBAPIError) as e:
            print(e)
            session.rollback()
            raise

        session.close()


    def getReposThatContainFeature(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([repositorios.c.idrepository.distinct()])
        query = query.select_from(
            repositorios.join(features, repositorios.columns.idrepository == features.columns.repository_id))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df


    def getTotalNumberOfRepositories(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(repositorios.columns.idrepository)])
        result = connection.execute(query).scalar()
        return result

    def getTotalNumberOfFeatures(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(features.columns.idfeature)])
        result = connection.execute(query).scalar()
        return result

    def getTotalNumberOfScenarios(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(scenarios.columns.idscenario)])
        result = connection.execute(query).scalar()
        return result

    def getTotalNumberOfSteps(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        steps = db.Table('step', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(steps.columns.idstep)])
        result = connection.execute(query).scalar()
        return result


    def getNumberOfReposThatContainFeature(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(features.c.repository_id.distinct())])
        result = connection.execute(query).scalar()
        return result

    def getNumberOfReposPerLanguages(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        #SQL
        query = select([db.func.count(repositorios.columns.idrepository.distinct()).label('Number of Repositories'),
                        repositorios.columns.language])
        query = query.select_from(
            repositorios.join(features, repositorios.columns.idrepository == features.columns.repository_id))
        query = query.group_by(repositorios.columns.language)
        query = query.order_by(db.asc(db.func.count(repositorios.columns.idrepository.distinct())))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df

    def getNumberOfReposPerCountry(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        query = select([db.func.count(repositorios.columns.idrepository.distinct()).label('Number of Repositories'),
                        repositorios.columns.country])
        query = query.select_from(
            repositorios.join(features, repositorios.columns.idrepository == features.columns.repository_id))
        query = query.group_by(repositorios.columns.country)
        query = query.order_by(db.asc(db.func.count(repositorios.columns.idrepository.distinct())))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df

    def getNumberOfScenariosPerRepo(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)

        # SELECT
        query = select([repositorios.columns.name,
                        db.func.count(repositorios.columns.idrepository).label("Number of Scenarios")])

        # JOIN
        query = query.select_from(
            repositorios.join(scenarios.join(features, features.columns.idfeature == scenarios.columns.feature_id),
                              repositorios.columns.idrepository == features.columns.repository_id))

        # GROUP BY and ORDER BY
        query = query.group_by(repositorios.columns.idrepository)
        query = query.order_by(
            db.desc(db.func.count(repositorios.columns.idrepository).label('Number of Scenarios')))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df

    def getNumberOfScenariosPerFeature(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)

        # SELECT
        query = select([features.columns.name,
                        db.func.count(features.columns.idfeature).label("Number of Scenarios")])

        # JOIN
        query = query.select_from(
            scenarios.join(features, features.columns.idfeature == scenarios.columns.feature_id))

        # GROUP BY and ORDER BY
        query = query.group_by(features.columns.idfeature)
        query = query.order_by(
            db.desc(db.func.count(features.columns.idfeature).label('Number of Scenarios')))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df

    def getAverageNumberOfFeaturesPerRepository(self):

        # setting things
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(repositorios.columns.idrepository).label('a1'))
        sums = sums.select_from(
            repositorios.join(features, repositorios.columns.idrepository == features.columns.repository_id))
        sums = sums.group_by(repositorios.columns.idrepository)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageNumberOfScenariosPerRepository(self):

        # setting things
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(repositorios.columns.idrepository).label('a1'))
        sums = sums.select_from(
            repositorios.join(scenarios.join(features, features.columns.idfeature == scenarios.columns.feature_id),
                              repositorios.columns.idrepository == features.columns.repository_id))
        sums = sums.group_by(repositorios.columns.idrepository)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageNumberOfStepsPerRepository(self):

        # setting things
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        steps = db.Table('step', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(repositorios.columns.idrepository).label('a1'))

        # JOIN
        scenarioJoinStep = steps.join(scenarios, steps.c.scenario_id == scenarios.c.idscenario)
        featureJoinScenarioJoinStep = features.join(scenarioJoinStep, features.columns.idfeature == scenarios.columns.feature_id)
        repositoryJoinFeatureJoinScenarioJoinStep = repositorios.join(featureJoinScenarioJoinStep, repositorios.columns.idrepository == features.columns.repository_id)
        sums = sums.select_from(repositoryJoinFeatureJoinScenarioJoinStep)

        # GROUP BY
        sums = sums.group_by(repositorios.columns.idrepository)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageNumberOfScenariosPerFeature(self):

        # setting things
        metadata = db.MetaData()
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(features.columns.idfeature).label('a1'))
        sums = sums.select_from(
            scenarios.join(features, features.columns.idfeature == scenarios.columns.feature_id))
        sums = sums.group_by(features.columns.idfeature)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageNumberOfStepsPerFeature(self):

        # setting things
        metadata = db.MetaData()
        steps = db.Table('step', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(scenarios.columns.idscenario).label('a1'))
        sums = sums.select_from(
            features.join(scenarios.join(steps, steps.columns.scenario_id == scenarios.columns.idscenario),
            features.columns.idfeature == scenarios.columns.feature_id))
        sums = sums.group_by(features.columns.idfeature)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageNumberOfStepsPerScenario(self):

        # setting things
        metadata = db.MetaData()
        steps = db.Table('step', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(scenarios.columns.idscenario).label('a1'))
        sums = sums.select_from(
            scenarios.join(steps, steps.columns.scenario_id == scenarios.columns.idscenario))
        sums = sums.group_by(scenarios.columns.idscenario)

        # query
        average = session.query(db.func.avg(sums.subquery().columns.a1)).scalar()

        session.close()

        return average

    def getAverageSizeOfRepositories(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)

        query = select([db.func.avg(repositorios.c.size)])
        result = connection.execute(query).scalar()
        return result

    def getAverageForksOfRepositories(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)

        query = select([db.func.avg(repositorios.c.forks_count)])
        result = connection.execute(query).scalar()
        return result


    def getAverageWatchersOfRepositories(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)

        query = select([db.func.avg(repositorios.c.watchers_count)])
        result = connection.execute(query).scalar()
        return result

    def getAverageSubscribersOfRepositories(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)

        query = select([db.func.avg(repositorios.c.subscribers_count)])
        result = connection.execute(query).scalar()
        return result

    def getNumberOfReposPerStars(self):

        # setting things
        connection = self.engine.connect()
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)

        # SQL
        #query = select([db.func.count(repositorios.columns.idrepository.distinct()).label('Number of Repositories'),
        #                repositorios.columns.stars])
        query = select([repositorios.columns.idrepository.distinct(), repositorios.columns.stars])
        query = query.select_from(
            repositorios.join(features, repositorios.columns.idrepository == features.columns.repository_id))
        #query = query.group_by(repositorios.columns.stars)
        query = query.order_by(db.asc(repositorios.columns.stars))

        # organizing return
        results = connection.execute(query).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        return df

    def get100ReposMostPopular_StepsPerScenario(self):
        # setting things
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        steps = db.Table('step', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery dos 100 mais famosos
        famososQuery = session.query(repositorios).order_by(repositorios.columns.stars.desc()).limit(100).subquery()

        # query principal
        sums = session.query(scenarios.columns.idscenario.label("idscenario"), db.func.count(steps.columns.idstep).label("Number of Steps"))

        # JOIN
        scenarioJoinStep = steps.join(scenarios, steps.c.scenario_id == scenarios.c.idscenario)
        featureJoinScenarioJoinStep = features.join(scenarioJoinStep,
                                                    features.columns.idfeature == scenarios.columns.feature_id)
        repositoryJoinFeatureJoinScenarioJoinStep = famososQuery.join(featureJoinScenarioJoinStep,
                                                                      famososQuery.columns.idrepository == features.columns.repository_id)
        sums = sums.select_from(repositoryJoinFeatureJoinScenarioJoinStep)

        # GROUP BY
        sums = sums.group_by(scenarios.columns.idscenario)


        # SELECT
        results = sums.all()

        # Pandas organization
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        session.close()
        return df

    def get100ReposMostPopular_ScenarioPerFeature(self):
        # setting things
        metadata = db.MetaData()
        repositorios = db.Table('repository', metadata, autoload=True, autoload_with=self.engine)
        features = db.Table('feature', metadata, autoload=True, autoload_with=self.engine)
        scenarios = db.Table('scenario', metadata, autoload=True, autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # subquery
        sums = session.query(db.func.count(scenarios.columns.idscenario).label('a1'))

        # JOIN
        sums = sums.select_from(
            features.join(features,
                          features.columns.idfeature == scenarios.columns.feature_id))
        sums = sums.group_by(features.columns.idfeature)

        # GROUP BY
        sums = sums.group_by(repositorios.columns.idrepository)

        # ORDER BY
        sums = sums.order_by(repositorios.columns.stars.desc())

        # query
        results = session.query(sums.subquery().columns.a1).limit(100).all()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(5)
        session.close()
        return df



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
        with open(path, mode='r', encoding='UTF8') as file:
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
        with open(path, mode='r', encoding='UTF8') as file:
            file.seek(0)
            lines = file.readlines()

            if lines[initial_line - 1].split()[0].count("Scenario:") >= 1:
                scenario.scenario_title = lines[initial_line - 1].split("Scenario: ", 1)[1].replace('\n', '').replace(':',
                                                                                                                 '')
                scenario.line = initial_line
                scenario.steps = self.get_steps(lines, initial_line + 1, final_line)
            elif lines[initial_line - 1].split().count("Outline:") >= 1:
                scenario.scenario_title = lines[initial_line - 1].split("Scenario Outline: ", 1)[1].replace('\n', '')
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
            #scenario = SimpleScenario()
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
        with open(path, mode='r', encoding='UTF8') as file:
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
        with open(path, mode='r', encoding='UTF8') as file:
            file.seek(0)
            for line_number, line in enumerate(file, 1):
                if "Scenario:" in line:
                    lines.append(line_number)
                elif "Scenario Outline:" in line:
                    lines.append(line_number)


        return lines
