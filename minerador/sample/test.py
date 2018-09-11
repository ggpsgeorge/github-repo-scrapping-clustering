from view_model import ViewModel
import os


token = ""
path = "https://api.github.com/repos/octocat/Hello-World"
path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
path3 = "https://api.github.com/repos/Kfourit/test2"
viewRepository = ViewModel(token)
repository = viewRepository.getRepositoryFromPath(path3)
#feature = viewRepository.get_feature_information(os.getcwd() + os.sep + "dados" + os.sep + "action_item.feature")
print(repository)
#print(feature)
