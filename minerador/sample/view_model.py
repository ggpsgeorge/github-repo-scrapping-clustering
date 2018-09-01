from models import Feature, Method, ScenarioOutline, SimpleScenario, Repository
import json
import os

class ViewModel:

    def __init__(self, token):
        self.token = token


    # Funcao retorna o json da pagina
    def get_json(self, url, token):
        resp = os.popen("curl -H 'Authorization: token " + token + "' " + url).read()
        return json.loads(resp)


    # Funcao que retorna uma lista com as urls de todos os repo do usuario
    def get_repo(self, url, token):
        repo_urls = []

        data = self.get_json(url, token)

        for repo in data:
            repo_urls.append(repo['url'] + '/contents')

        return repo_urls


    def getRepositoryFromPath(self, path):
        repositoryJson = self.get_json(path, self.token)
        ownerJson = self.get_json(repositoryJson['owner']['url'], self.token)
        repository = Repository()
        repository.path = repositoryJson['url']
        repository.name = repositoryJson['name']
        repository.owner = repositoryJson['owner']['login']
        repository.country = ownerJson['location']
        repository.language = repositoryJson['language']

        return repository