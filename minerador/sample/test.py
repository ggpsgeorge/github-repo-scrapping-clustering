from view_model import ViewModel


token = ""
path = "https://api.github.com/repos/octocat/Hello-World"
path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
path3 = "https://github.com/ggpsgeorge/minerador/tree/kfouri/minerador"
viewRepository = ViewModel(token)
repository = viewRepository.getRepositoryFromPath(path3)
print(repository)
