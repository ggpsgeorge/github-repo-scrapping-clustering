from models import Feature, Method, ScenarioOutline, SimpleScenario, Repository


class ViewModel:

    def __init__(self, token):
        self.token = token

    def find_repository_from_path(self, path):
        get_repo(self, path)

        return repository

    # Funcao retorna o json da pagina
    def get_json(self, url):
        resp = os.popen("curl -H 'Authorization: token " + self.token + "' " + url).read()
        return json.loads(resp)

    # Funcao que retorna uma lista com as urls de todos os repo do usuario
    def get_repo(self, url):
        repo_urls = []

        data = get_json(url, self.token)

        for repo in data:
            repo_urls.append(repo['url'] + '/contents')

        return repo_urls
