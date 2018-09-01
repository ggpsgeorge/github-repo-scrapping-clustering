from view_model import ViewModel


token = "31c01cc17db18206df13b1a4f745fc2400d37433"
path = "https://api.github.com/repos/octocat/Hello-World"
viewRepository = ViewModel(token)
repository = viewRepository.getRepositoryFromPath(path)
print(repository)
